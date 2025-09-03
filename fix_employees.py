#!/usr/bin/env python3
"""
Fix employees is_active field
"""
import sqlite3
import os

def fix_employees():
    """Fix the is_active field for all employees"""
    print("Fixing employee is_active field...")
    
    db_path = './data/raffle_database.db'
    
    if not os.path.exists(db_path):
        print(f"Database file does not exist: {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        
        # Check current status
        cursor = conn.execute("SELECT COUNT(*) as total FROM employees")
        total = cursor.fetchone()['total']
        
        cursor = conn.execute("SELECT COUNT(*) as active FROM employees WHERE is_active = 1")
        active = cursor.fetchone()['active']
        
        cursor = conn.execute("SELECT COUNT(*) as inactive FROM employees WHERE is_active = 0 OR is_active IS NULL")
        inactive = cursor.fetchone()['inactive']
        
        print(f"Current status:")
        print(f"  Total employees: {total}")
        print(f"  Active employees: {active}")
        print(f"  Inactive/NULL employees: {inactive}")
        
        if inactive > 0:
            print(f"\nUpdating {inactive} employees to active status...")
            
            # Update all employees to be active
            cursor = conn.execute("UPDATE employees SET is_active = 1 WHERE is_active = 0 OR is_active IS NULL")
            conn.commit()
            
            print(f"Updated {cursor.rowcount} employees")
            
            # Verify the fix
            cursor = conn.execute("SELECT COUNT(*) as active FROM employees WHERE is_active = 1")
            new_active = cursor.fetchone()['active']
            print(f"New active count: {new_active}")
        
        else:
            print("All employees are already active")
        
        conn.close()
        print("Employee status fix completed!")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    fix_employees()