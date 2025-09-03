#!/usr/bin/env python3
"""
Check activities in the database
"""
import sqlite3
import os

def check_activities():
    """Check the database for activities"""
    print("Checking database for activities...")
    
    db_path = './data/raffle_database.db'
    
    if not os.path.exists(db_path):
        print(f"Database file does not exist: {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        
        # Check if activities table exists
        cursor = conn.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='activities'
        """)
        
        table_exists = cursor.fetchone()
        if not table_exists:
            print("ERROR: activities table does not exist")
            conn.close()
            return
        
        print("activities table exists")
        
        # Get table schema
        cursor = conn.execute("PRAGMA table_info(activities)")
        columns = cursor.fetchall()
        print("Table columns:")
        for col in columns:
            print(f"  {col['name']} ({col['type']})")
        
        # Count total activities
        cursor = conn.execute("SELECT COUNT(*) as count FROM activities")
        total = cursor.fetchone()['count']
        print(f"\nTotal activities in database: {total}")
        
        if total > 0:
            print(f"\nRecent activities:")
            cursor = conn.execute("""
                SELECT a.id, a.employee_id, e.name, a.activity_name, a.activity_category, 
                       a.entries_awarded, a.created_at 
                FROM activities a
                JOIN employees e ON a.employee_id = e.id
                ORDER BY a.created_at DESC 
                LIMIT 10
            """)
            
            activities = cursor.fetchall()
            for act in activities:
                print(f"  ID: {act['id']}, Employee: {act['name']}, Activity: {act['activity_name']}, Entries: {act['entries_awarded']}, Created: {act['created_at']}")
        
        conn.close()
        
    except Exception as e:
        print(f"Database error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check_activities()