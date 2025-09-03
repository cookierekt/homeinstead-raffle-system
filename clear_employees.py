#!/usr/bin/env python3
"""
Clear all employee data from the database
"""
import sqlite3
import os

def clear_employees():
    """Clear all employees from the database"""
    print("Clearing all employee data...")
    
    db_path = './data/raffle_database.db'
    
    if not os.path.exists(db_path):
        print(f"Database file does not exist: {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        
        # Check current employee count
        cursor = conn.execute("SELECT COUNT(*) as count FROM employees")
        current_count = cursor.fetchone()['count']
        print(f"Current employee count: {current_count}")
        
        if current_count == 0:
            print("No employees to delete")
            conn.close()
            return
        
        # Delete all activities first (due to foreign key constraints)
        cursor = conn.execute("DELETE FROM activities")
        activities_deleted = cursor.rowcount
        print(f"Deleted {activities_deleted} activity records")
        
        # Delete all raffle history
        cursor = conn.execute("DELETE FROM raffle_history")
        raffle_deleted = cursor.rowcount
        print(f"Deleted {raffle_deleted} raffle history records")
        
        # Delete all employees
        cursor = conn.execute("DELETE FROM employees")
        employees_deleted = cursor.rowcount
        print(f"Deleted {employees_deleted} employee records")
        
        # Reset auto-increment counters
        conn.execute("DELETE FROM sqlite_sequence WHERE name='employees'")
        conn.execute("DELETE FROM sqlite_sequence WHERE name='activities'") 
        conn.execute("DELETE FROM sqlite_sequence WHERE name='raffle_history'")
        
        # Commit all changes
        conn.commit()
        
        # Verify deletion
        cursor = conn.execute("SELECT COUNT(*) as count FROM employees")
        final_count = cursor.fetchone()['count']
        print(f"Final employee count: {final_count}")
        
        conn.close()
        print("✓ All employee data cleared successfully!")
        
    except Exception as e:
        print(f"Error clearing employees: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    clear_employees()