# 🔧 **Fix "Not Found" Deployment Error**

## 🚨 **Common Causes & Solutions**

### **1. Missing Dependencies**
**Problem**: Platform can't install Python packages
**Solution**: Update requirements file

Create/update `requirements.txt`:
```
Flask==2.3.3
gunicorn==21.2.0
python-dotenv==1.0.0
bcrypt==4.0.1
PyJWT==2.8.0
Flask-Limiter==3.5.0
openpyxl==3.1.2
Werkzeug==2.3.7
```

### **2. Wrong Start Command**
**Problem**: Platform can't start your Flask app
**Solutions by Platform**:

**Render.com:**
```
Start Command: gunicorn app:app
```

**Railway:**
```
Start Command: gunicorn app:app --host 0.0.0.0 --port $PORT
```

**Heroku:**
```
Procfile: web: gunicorn app:app
```

**Netlify:**
```
Netlify doesn't support Flask directly - use Render instead
```

### **3. Missing Environment Variables**
**Problem**: App crashes due to missing config
**Required Variables**:
```
SECRET_KEY=your-secret-key-here
JWT_SECRET=your-jwt-secret-here
NODE_ENV=production
DATABASE_PATH=./data/raffle_database.db
```

### **4. Database Issues**
**Problem**: SQLite database can't be created
**Solution**: Update app.py to handle deployment

Add this to your app.py:
```python
# Add at the top after imports
import os
from pathlib import Path

# Ensure directories exist
Path("data").mkdir(exist_ok=True)
Path("backups").mkdir(exist_ok=True)
Path("uploads").mkdir(exist_ok=True)
```

### **5. Port Configuration**
**Problem**: App not listening on correct port
**Solution**: Update app.py ending:

```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('NODE_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)
```

---

## 🎯 **Platform-Specific Fixes**

### **Render.com Fix:**
1. **Build Command**: `pip install -r requirements.txt`
2. **Start Command**: `gunicorn app:app`
3. **Add Environment Variables**:
   ```
   SECRET_KEY = [Generate random]
   JWT_SECRET = [Generate random] 
   NODE_ENV = production
   PYTHON_VERSION = 3.9
   ```

### **Railway Fix:**
1. **No build command needed**
2. **Add railway.json** in root:
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "gunicorn app:app --host 0.0.0.0 --port $PORT"
  }
}
```

### **Heroku Fix:**
1. **Create Procfile**:
```
web: gunicorn app:app
```

2. **Create runtime.txt**:
```
python-3.9.18
```

### **Vercel Fix:**
Vercel is tricky for Flask. Use this vercel.json:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "./app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/"
    }
  ]
}
```

---

## 🔍 **Debugging Steps**

### **1. Check Build Logs**
Look for these errors:
- `Module not found` → Missing dependencies
- `Permission denied` → File permissions issue
- `Port already in use` → Port configuration issue
- `Database error` → Database path/permissions issue

### **2. Test Locally First**
```bash
# Test your app works locally
cd your-project-folder
pip install -r requirements.txt
python app.py

# Should show:
# * Running on http://localhost:5000
```

### **3. Check File Structure**
Ensure you have:
```
raffle-dashboard/
├── app.py              # ✅ Main Flask file
├── requirements.txt    # ✅ Dependencies
├── Procfile           # ✅ For Heroku
├── runtime.txt        # ✅ Python version
├── config.py          # ✅ Configuration
├── database.py        # ✅ Database code
├── auth.py           # ✅ Authentication
├── templates/         # ✅ HTML templates
└── static/           # ✅ CSS/JS files
```

---

## 🚀 **Quick Fix Commands**

### **Update Your Files:**

**1. Fix requirements.txt**
```bash
echo "Flask==2.3.3
gunicorn==21.2.0
python-dotenv==1.0.0
bcrypt==4.0.1
PyJWT==2.8.0
Flask-Limiter==3.5.0
openpyxl==3.1.2
Werkzeug==2.3.7" > requirements.txt
```

**2. Fix Procfile**
```bash
echo "web: gunicorn app:app" > Procfile
```

**3. Fix runtime.txt**
```bash
echo "python-3.9.18" > runtime.txt
```

**4. Test locally**
```bash
pip install -r requirements.txt
python app.py
```

---

## ✅ **Working Deployment Config**

**For Render.com (Recommended):**
```
Repository: Your GitHub repo
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Environment Variables:
  SECRET_KEY = [auto-generate]
  JWT_SECRET = [auto-generate]
  NODE_ENV = production
  PYTHON_VERSION = 3.9
```

**For Railway:**
```
Just connect GitHub repo - Railway auto-detects everything!
Add environment variables in dashboard.
```

**For Heroku:**
```bash
git add .
git commit -m "Fix deployment"
heroku create your-app-name
git push heroku main
```

---

## 🆘 **Still Getting "Not Found"?**

**Share these details:**
1. **Which platform** are you using? (Render/Railway/Heroku/etc.)
2. **Error message** from build logs
3. **Your current config** (build command, start command)

**Most Common Fix:**
Change start command to: `gunicorn app:app --host 0.0.0.0 --port $PORT`

Your dashboard should be working online soon! 🎉