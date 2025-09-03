#!/usr/bin/env python3
"""
Update admin user credentials
"""
import sqlite3
import bcrypt
import os

def update_admin_credentials():
    """Update admin user with new credentials"""
    print("Updating admin credentials...")
    
    db_path = './data/raffle_database.db'
    
    if not os.path.exists(db_path):
        print(f"Database file does not exist: {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        
        # Check current admin users
        cursor = conn.execute("SELECT email, role FROM users WHERE role = 'admin'")
        current_admins = cursor.fetchall()
        print(f"Current admin users:")
        for admin in current_admins:
            print(f"  - {admin['email']}")
        
        # Delete existing admin users
        cursor = conn.execute("DELETE FROM users WHERE role = 'admin'")
        deleted_count = cursor.rowcount
        print(f"Deleted {deleted_count} admin users")
        
        # Create new admin user
        new_email = 'homecare@homeinstead.com'
        new_password = 'Homeinstead3042'
        password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        conn.execute('''
            INSERT INTO users (email, password_hash, role, name, is_active)
            VALUES (?, ?, ?, ?, ?)
        ''', (new_email, password_hash, 'admin', 'Administrator', 1))
        
        # Commit changes
        conn.commit()
        
        # Verify new admin user
        cursor = conn.execute("SELECT email, role, is_active FROM users WHERE role = 'admin'")
        new_admin = cursor.fetchone()
        
        if new_admin:
            print(f"New admin user created successfully:")
            print(f"  Email: {new_admin['email']}")
            print(f"  Role: {new_admin['role']}")
            print(f"  Active: {new_admin['is_active']}")
        else:
            print("ERROR: Failed to create new admin user")
        
        conn.close()
        print("Admin credentials updated successfully!")
        
    except Exception as e:
        print(f"Error updating admin credentials: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    update_admin_credentials()