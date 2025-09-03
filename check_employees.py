#!/usr/bin/env python3
"""
Check if employees exist in the database
"""
import sqlite3
import os
from database import DatabaseManager

def check_database():
    """Check the database for employees"""
    print("Checking database for employees...")
    
    db_path = './data/raffle_database.db'
    
    if not os.path.exists(db_path):
        print(f"Database file does not exist: {db_path}")
        return
    
    print(f"Database file exists: {db_path}")
    print(f"Database size: {os.path.getsize(db_path)} bytes")
    
    try:
        # Try to connect to database
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        
        # Check if employees table exists
        cursor = conn.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='employees'
        """)
        
        table_exists = cursor.fetchone()
        if not table_exists:
            print("ERROR: employees table does not exist")
            conn.close()
            return
        
        print("employees table exists")
        
        # Get table schema
        cursor = conn.execute("PRAGMA table_info(employees)")
        columns = cursor.fetchall()
        print("Table columns:")
        for col in columns:
            print(f"  {col['name']} ({col['type']})")
        
        # Count total employees
        cursor = conn.execute("SELECT COUNT(*) as count FROM employees")
        total = cursor.fetchone()['count']
        print(f"\nTotal employees in database: {total}")
        
        if total > 0:
            print(f"\nFirst 10 employees:")
            cursor = conn.execute("""
                SELECT id, name, total_entries, created_at 
                FROM employees 
                ORDER BY created_at DESC 
                LIMIT 10
            """)
            
            employees = cursor.fetchall()
            for emp in employees:
                print(f"  ID: {emp['id']}, Name: {emp['name']}, Entries: {emp['total_entries']}, Created: {emp['created_at']}")
        
        conn.close()
        
    except Exception as e:
        print(f"Database error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check_database()