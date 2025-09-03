# 🧭 **Find Settings in Render Dashboard - Step by Step**

## 🔍 **Where to Find the Options**

### **Step 1: Access Your Service**
1. **Go to**: https://dashboard.render.com
2. **Sign in** to your account
3. **Click on your service** (should be named something like "raffle-dashboard" or "home-instead-raffle")

### **Step 2: Find the Settings Tab**
Once you click on your service, you'll see several tabs at the top:
- **Overview** (default tab)
- **Events**  
- **Logs**
- **Settings** ← **This is what you need!**
- **Environment**

**Click on "Settings" tab**

### **Step 3: Locate Build & Deploy Section**
In the Settings tab, scroll down to find:
- **Build & Deploy** section (usually near the top)
- You'll see:
  - **Build Command**
  - **Start Command** ← **This is what we need to change!**

### **Step 4: Find Environment Tab**
For environment variables:
- **Click "Environment" tab** (next to Settings)
- **Or** look for **"Environment Variables"** section in Settings

---

## 📱 **Visual Guide - What You Should See**

### **Main Dashboard View:**
```
🏠 Dashboard > Services > [Your Service Name]

Tabs: Overview | Events | Logs | Settings | Environment
```

### **Settings Tab View:**
```
⚙️ Settings

Build & Deploy
├── Build Command: pip install -r requirements.txt
├── Start Command: gunicorn app:app          ← Change this!
└── Root Directory: (blank)

Other sections below...
```

### **Environment Tab View:**
```
🌍 Environment

Environment Variables:
[+ Add Environment Variable]

SECRET_KEY = ************
NODE_ENV = production
```

---

## 🎯 **Exact Steps to Change Start Command**

### **Method 1: Through Settings Tab**
1. **Dashboard** → **Your Service** → **Settings** tab
2. **Scroll to "Build & Deploy"** section
3. **Find "Start Command"** field
4. **Change from**: `gunicorn app:app`
5. **Change to**: `gunicorn app_simple:app`
6. **Click "Save Changes"** button at bottom
7. **Service will redeploy automatically**

### **Method 2: Through Deploy Section**
Some Render accounts show it differently:
1. **Your Service** → **Deploy** tab
2. **Look for "Deploy Configuration"**
3. **Find "Start Command"**
4. **Update and save**

---

## 🔧 **Alternative: Manual Redeploy**

If you can't find Settings, try manual redeploy:

### **Step 1: Create New File**
Add this file to your GitHub repo as `app_working.py`:

```python
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>🏠 Home Instead Raffle Dashboard</h1>
    <h2>✅ Render Deployment Working!</h2>
    <p>Your service is live and running properly.</p>
    <a href="/health">Health Check</a>
    '''

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "message": "Working on Render!"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

### **Step 2: Update Start Command**
Change to: `gunicorn app_working:app`

---

## 🆘 **Can't Find Settings?**

### **Different Render Interface Versions:**

**If you see "Deploy" instead of "Settings":**
- **Click "Deploy" tab**
- **Look for "Configuration"**
- **Find "Start Command"**

**If you see a gear icon ⚙️:**
- **Click the gear icon**
- **Should open settings**

**If you see "Service Details":**
- **Click "Edit Service" or "Configure"**
- **Should show build settings**

---

## 📞 **Quick Alternative Solutions**

### **Solution 1: Redeploy from Scratch**
1. **Delete current service** in Render
2. **Create new service**
3. **Connect same GitHub repo**
4. **Set start command**: `gunicorn app_simple:app`

### **Solution 2: Use Different File**
1. **Rename** `app.py` to `app_main.py` in GitHub
2. **Rename** `app_simple.py` to `app.py` in GitHub  
3. **Render will redeploy automatically**
4. **Keep start command**: `gunicorn app:app`

### **Solution 3: Try Railway Instead**
If Render interface is confusing:
1. **Go to**: https://railway.app
2. **Connect GitHub repo**
3. **Deploy with one click** (auto-configures)

---

## 📱 **What to Look For**

You're looking for:
- ⚙️ **Settings** or **Configure** button/tab
- 🔧 **Build Command** and **Start Command** fields
- 🌍 **Environment Variables** section
- 🚀 **Deploy** or **Redeploy** button

**The key is finding where Render shows your service configuration!**

---

## ✅ **Once You Find It**

When you locate the Start Command field:
1. **Current value**: `gunicorn app:app`
2. **Change to**: `gunicorn app_simple:app`  
3. **Save**
4. **Wait 2 minutes**
5. **Visit your URL** - should work!

**Which interface are you seeing in Render? Can you describe what tabs or buttons you see when you click on your service?**