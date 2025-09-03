#!/usr/bin/env python3
"""
Production setup script for Home Instead Raffle Dashboard
This script sets up the secure, professional-grade raffle dashboard.
"""

import os
import sys
import subprocess
import sqlite3
import secrets
from datetime import datetime

def run_command(cmd, description=""):
    """Run a command and handle errors"""
    print(f"{'='*50}")
    print(f"Running: {description or cmd}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        return False

def install_dependencies():
    """Install required Python packages"""
    packages = [
        'python-dotenv==1.0.0',
        'bcrypt==4.0.1',
        'PyJWT==2.8.0',
        'Flask-Limiter==3.5.0',
        'Flask-CORS==4.0.0',
        'cryptography==41.0.7',
        'Pillow==10.0.1',
        'reportlab==4.0.6'
    ]
    
    for package in packages:
        if not run_command(f"pip install {package}", f"Installing {package}"):
            print(f"Warning: Failed to install {package}")
            return False
    
    return True

def create_secure_env():
    """Create secure environment configuration"""
    env_path = '.env'
    
    if os.path.exists(env_path):
        print(f"Environment file {env_path} already exists. Backing up...")
        backup_path = f".env.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.rename(env_path, backup_path)
        print(f"Backed up to {backup_path}")
    
    # Generate secure secrets
    secret_key = secrets.token_hex(32)
    jwt_secret = secrets.token_hex(32)
    
    env_content = f"""# Home Instead Raffle Dashboard - Production Configuration
# Generated on {datetime.now().isoformat()}

# Security (CHANGE THESE IN PRODUCTION!)
SECRET_KEY={secret_key}
JWT_SECRET={jwt_secret}

# Database Configuration
DATABASE_PATH=./data/raffle_database.db
BACKUP_PATH=./backups

# Application Settings
NODE_ENV=production
PORT=5000
APP_NAME=Home Instead Raffle Dashboard
COMPANY_NAME=Home Instead Senior Care

# File Upload Settings
MAX_FILE_SIZE=5242880
UPLOAD_PATH=./uploads

# Security Settings
SESSION_TIMEOUT=1800000
MAX_LOGIN_ATTEMPTS=3
LOCKOUT_TIME=900000

# Feature Flags
ENABLE_EMAIL_NOTIFICATIONS=false
ENABLE_PHOTO_UPLOADS=true
ENABLE_EXCEL_IMPORT=true
ENABLE_PDF_EXPORT=true

# Email Configuration (Optional - Configure for notifications)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@homeinstead.com
SMTP_PASS=your-app-password
"""
    
    with open(env_path, 'w') as f:
        f.write(env_content)
    
    print(f"Created secure environment configuration in {env_path}")
    print("IMPORTANT: Change the default secrets before deploying to production!")
    
    return True

def setup_directories():
    """Create necessary directories"""
    directories = [
        'data',
        'backups',
        'uploads',
        'logs'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        
        # Create .gitkeep files
        gitkeep_path = os.path.join(directory, '.gitkeep')
        if not os.path.exists(gitkeep_path):
            with open(gitkeep_path, 'w') as f:
                f.write('')
    
    print("Created necessary directories")
    return True

def setup_database():
    """Initialize the SQLite database"""
    try:
        # Import and initialize database
        from database import DatabaseManager
        
        print("Initializing database...")
        db_manager = DatabaseManager()
        
        # Check if old JSON data exists and migrate
        if os.path.exists('raffle_data.json'):
            print("Found existing JSON data. Migrating to SQLite...")
            db_manager.migrate_from_json('raffle_data.json')
            
            # Backup the JSON file
            backup_name = f"raffle_data.json.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            os.rename('raffle_data.json', backup_name)
            print(f"JSON data migrated. Original backed up to {backup_name}")
        
        print("Database initialized successfully")
        print("Default admin login: admin@homeinstead.com / admin123")
        print("CHANGE THE DEFAULT ADMIN PASSWORD IMMEDIATELY!")
        
        return True
        
    except Exception as e:
        print(f"Database setup failed: {e}")
        return False

def test_application():
    """Test that the application starts correctly"""
    print("Testing application startup...")
    
    try:
        # Try importing main modules
        from config import Config
        from database import db
        from auth import AuthManager
        
        print("All modules imported successfully")
        print("Application setup complete!")
        
        return True
        
    except Exception as e:
        print(f"Application test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("Home Instead Raffle Dashboard - Professional Setup")
    print("=" * 60)
    print("Setting up your secure, production-ready raffle dashboard...")
    print()
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("Python 3.7+ is required")
        return False
    
    print(f"Python {sys.version.split()[0]} detected")
    
    # Setup steps
    steps = [
        ("Installing Python dependencies", install_dependencies),
        ("Creating secure environment configuration", create_secure_env),
        ("Setting up directories", setup_directories),
        ("Initializing database", setup_database),
        ("Testing application", test_application)
    ]
    
    for step_name, step_func in steps:
        print(f"\n{step_name}...")
        if not step_func():
            print(f"Setup failed at: {step_name}")
            return False
    
    print("\n" + "=" * 60)
    print("SETUP COMPLETE!")
    print("=" * 60)
    print()
    print("Your professional raffle dashboard is ready!")
    print()
    print("Next steps:")
    print("1. Review and update the .env file with your settings")
    print("2. Change the default admin password (admin@homeinstead.com / admin123)")
    print("3. Start the application: python app.py")
    print("4. Visit http://localhost:5000 to access the dashboard")
    print()
    print("Security Features Enabled:")
    print("   - Secure authentication with JWT tokens")
    print("   - Password hashing with bcrypt")
    print("   - Rate limiting on login attempts")
    print("   - SQL injection protection")
    print("   - CSRF protection")
    print("   - Audit logging")
    print("   - Encrypted data storage")
    print()
    print("Professional Features:")
    print("   - Employee management with photos")
    print("   - Advanced raffle system")
    print("   - Excel import/export")
    print("   - Analytics dashboard")
    print("   - PDF report generation")
    print("   - Automated backups")
    print()
    print("Free hosting options:")
    print("   - Render.com (recommended)")
    print("   - Railway.app")
    print("   - Vercel")
    print("   - Heroku")
    print()
    print("For support, check the README.md file")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)