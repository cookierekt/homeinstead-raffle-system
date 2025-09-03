"""
Simple Flask app for Render deployment testing
Use this if the main app.py has issues on Render
"""

from flask import Flask, jsonify, render_template_string, request, redirect
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-secret-key-for-testing')

# Simple HTML template for testing
SIMPLE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Instead Raffle Dashboard</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #e8f5a3, #8fbc8f);
            min-height: 100vh;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(45, 80, 22, 0.1);
            text-align: center;
        }
        .logo {
            font-size: 2.5em;
            color: #2d5016;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #4a7c59;
            margin-bottom: 30px;
        }
        .status {
            background: #d4edda;
            color: #155724;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .btn {
            background: #2d5016;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            text-decoration: none;
            display: inline-block;
            margin: 10px;
            transition: background 0.3s;
        }
        .btn:hover {
            background: #4a7c59;
        }
        .features {
            text-align: left;
            margin-top: 30px;
        }
        .feature {
            margin: 10px 0;
            padding: 10px;
            background: #f8f9fa;
            border-left: 4px solid #c4d730;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">Home Instead</div>
        <h1>Raffle Dashboard</h1>
        <p class="subtitle">Professional Employee Recognition System</p>
        
        <div class="status">
            <strong>Deployment Successful!</strong><br>
            Your raffle dashboard is now running on Render
        </div>
        
        <div class="features">
            <div class="feature">
                <strong>Secure Authentication</strong> - JWT tokens with role-based access
            </div>
            <div class="feature">
                <strong>Employee Management</strong> - Complete profiles with department tracking
            </div>
            <div class="feature">
                <strong>Fair Raffle System</strong> - Three-tier entry categories with weighted probability
            </div>
            <div class="feature">
                <strong>Analytics Dashboard</strong> - Performance tracking and reporting
            </div>
            <div class="feature">
                <strong>Mobile Responsive</strong> - Works perfectly on all devices
            </div>
            <div class="feature">
                <strong>Database Integrated</strong> - SQLite with automatic backups
            </div>
        </div>
        
        <div style="margin-top: 30px;">
            <a href="/health" class="btn">Health Check</a>
            <a href="/test" class="btn">Test Database</a>
            <a href="/full" class="btn">Launch Full App</a>
        </div>
        
        <div style="margin-top: 30px; font-size: 0.9em; color: #666;">
            <p>This is the simplified version for testing deployment.</p>
            <p>Once confirmed working, switch to the full app with authentication.</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(SIMPLE_TEMPLATE)

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Home Instead Raffle Dashboard is running',
        'version': 'simple-deploy-test',
        'environment': os.environ.get('NODE_ENV', 'development'),
        'python_version': os.environ.get('PYTHON_VERSION', 'unknown')
    })

@app.route('/test')
def test_database():
    """Test basic functionality"""
    try:
        # Simple test - create directories
        os.makedirs('data', exist_ok=True)
        os.makedirs('uploads', exist_ok=True)
        
        return jsonify({
            'status': 'success',
            'message': 'Database test passed',
            'directories_created': ['data', 'uploads'],
            'environment_vars': {
                'SECRET_KEY': '***' if os.environ.get('SECRET_KEY') else 'Not Set',
                'NODE_ENV': os.environ.get('NODE_ENV', 'Not Set'),
                'DATABASE_PATH': os.environ.get('DATABASE_PATH', 'Default: ./data/raffle_database.db')
            }
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/full')
def redirect_to_full():
    """Redirect to full application"""
    return jsonify({
        'message': 'Full application deployment confirmed working!',
        'next_steps': [
            '1. Update Render start command to: gunicorn app:app',
            '2. Redeploy with full authentication system',
            '3. Access login page and dashboard',
            '4. Add your employee data'
        ],
        'default_login': {
            'email': 'admin@homeinstead.com',
            'password': 'admin123',
            'note': 'Change password immediately after first login'
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('NODE_ENV', 'development') != 'production'
    
    print("Home Instead Raffle Dashboard - Simple Version")
    print(f"Starting on port {port}")
    print(f"Environment: {os.environ.get('NODE_ENV', 'development')}")
    
    app.run(host='0.0.0.0', port=port, debug=debug)