# 🔧 **Render Deployment Fix - Step by Step**

## 🚨 **Common Render Issues & Solutions**

### **1. Check Build Logs First**
1. **Go to Render Dashboard** → Your Service
2. **Click "Logs"** tab
3. **Look for errors** in the build process

**Common Error Messages:**

#### **"ModuleNotFoundError: No module named 'xyz'"**
**Fix**: Update requirements.txt
```bash
Flask==2.3.3
gunicorn==21.2.0
python-dotenv==1.0.0
bcrypt==4.0.1
PyJWT==2.8.0
Flask-Limiter==3.5.0
openpyxl==3.1.2
Werkzeug==2.3.7
flask-cors==4.0.0
cryptography==41.0.7
```

#### **"Application failed to start"**
**Fix**: Wrong start command
- **Correct**: `gunicorn app:app`
- **Not**: `python app.py`

#### **"Port already in use" or "Can't bind to port"**
**Fix**: Add environment variable
- `PORT` = `10000` (or let Render auto-assign)

---

## 🎯 **Correct Render Configuration**

### **Service Settings:**
```
Name: home-instead-raffle
Environment: Python 3
Region: Ohio (US East) - fastest for most users
Branch: main
Root Directory: (leave blank)
```

### **Build & Deploy:**
```
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app --bind 0.0.0.0:$PORT
```

### **Environment Variables:** (CRITICAL!)
```
SECRET_KEY = [Click "Generate" for random key]
JWT_SECRET = [Click "Generate" for random key]
NODE_ENV = production
PYTHON_VERSION = 3.9
DATABASE_PATH = ./data/raffle_database.db
BACKUP_PATH = ./backups
UPLOAD_PATH = ./uploads
```

---

## 🔍 **Debugging Steps**

### **Step 1: Test Health Check**
After deployment, visit:
```
https://your-app-name.onrender.com/health
```

**Should show:**
```json
{"status": "healthy", "message": "Home Instead Raffle Dashboard is running"}
```

**If this fails** → App isn't starting properly

### **Step 2: Check Service Status**
In Render Dashboard:
- **Green dot** = Service running
- **Red dot** = Service failed
- **Yellow dot** = Service starting

### **Step 3: View Live Logs**
In Render Dashboard → Logs tab:
- **Build logs** = Installation process  
- **Deploy logs** = App startup process
- **Service logs** = Runtime errors

---

## ⚡ **Quick Fixes**

### **Fix 1: Update Start Command**
If app won't start, try these commands:

**Option A (Recommended):**
```
gunicorn app:app --bind 0.0.0.0:$PORT
```

**Option B (Alternative):**
```
python -m gunicorn app:app --bind 0.0.0.0:$PORT
```

**Option C (Last Resort):**
```
python app.py
```

### **Fix 2: Add Missing Files**
Ensure your repository has:
```
✅ app.py
✅ requirements.txt
✅ config.py  
✅ database.py
✅ auth.py
✅ templates/
✅ static/
✅ .env.example (not .env - that's local only)
```

### **Fix 3: Simplify Requirements**
Create minimal requirements.txt:
```
Flask==2.3.3
gunicorn==21.2.0
python-dotenv==1.0.0
bcrypt==4.0.1
PyJWT==2.8.0
openpyxl==3.1.2
```

### **Fix 4: Add Procfile (Backup)**
Create `Procfile` in root:
```
web: gunicorn app:app
```

---

## 🛡️ **Advanced Troubleshooting**

### **Database Issues:**
If you see database errors:
1. **Add environment variable**: `DATABASE_PATH = /tmp/raffle_database.db`
2. **Or use in-memory**: `DATABASE_PATH = :memory:`

### **Permission Issues:**
If you see permission errors:
1. **Change upload path**: `UPLOAD_PATH = /tmp/uploads`
2. **Or disable uploads**: `ENABLE_PHOTO_UPLOADS = false`

### **Import Issues:**
If imports fail, try this in app.py:
```python
# Add at the very top
import sys
import os
sys.path.append(os.path.dirname(__file__))

# Then your normal imports
from flask import Flask, render_template
# etc...
```

---

## 🔄 **Redeploy Steps**

### **Manual Redeploy:**
1. **Go to Render Dashboard**
2. **Click your service**
3. **Click "Manual Deploy"**
4. **Select "Deploy latest commit"**

### **Force Redeploy:**
1. **Make small change** to README.md
2. **Commit and push** to GitHub
3. **Render will auto-deploy**

---

## 🎯 **Working Example Config**

**Copy this exact configuration:**

**Render Service Settings:**
```
Name: raffle-dashboard
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Root Directory: (blank)
```

**Environment Variables:**
```
SECRET_KEY = abc123secretkey456def
JWT_SECRET = xyz789jwtsecret321abc  
NODE_ENV = production
PYTHON_VERSION = 3.9
```

**requirements.txt:**
```
Flask==2.3.3
gunicorn==21.2.0
python-dotenv==1.0.0
bcrypt==4.0.1
PyJWT==2.8.0
openpyxl==3.1.2
```

---

## 🆘 **Still Not Working?**

### **Share These Details:**
1. **Your Render app URL**
2. **Error message** from build logs
3. **Your current** build/start commands
4. **Environment variables** you've set

### **Alternative: Try Railway**
If Render keeps failing, try Railway.app:
1. **Go to railway.app**
2. **Connect GitHub repo**  
3. **Click "Deploy"**
4. **Done!** (Auto-configures everything)

### **Last Resort: Heroku**
```bash
git add .
git commit -m "Deploy to Heroku"
heroku create your-raffle-dashboard
git push heroku main
```

---

## ✅ **Success Checklist**

When working properly, you should see:
- ✅ **Build succeeds** (green checkmark)
- ✅ **Service starts** (green dot)
- ✅ **Health check works** (`/health` returns JSON)
- ✅ **Login page loads** (`/` redirects to `/login`)
- ✅ **No errors in logs**

Your Render deployment should be working soon! 🚀