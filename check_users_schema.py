#!/usr/bin/env python3
"""
Check users table schema
"""
import sqlite3
import os

def check_users_schema():
    """Check the schema of users table"""
    print("Checking users table schema...")
    
    db_path = './data/raffle_database.db'
    
    if not os.path.exists(db_path):
        print(f"Database file does not exist: {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        
        # Get table schema
        cursor = conn.execute("PRAGMA table_info(users)")
        columns = cursor.fetchall()
        
        print("Users table columns:")
        for col in columns:
            print(f"  {col[1]} ({col[2]}) - NOT NULL: {col[3]}, DEFAULT: {col[4]}")
        
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_users_schema()