# 🚀 **Quick Start Guide - Home Instead Raffle Dashboard**

## **Step 1: Install Python (if not already installed)**

### **Windows:**
1. Go to https://www.python.org/downloads/
2. Download Python 3.8 or newer
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Click "Install Now"

### **Verify Installation:**
```bash
python --version
# Should show: Python 3.8.x or higher
```

## **Step 2: Run the Automated Setup**

Open Command Prompt or PowerShell in your project folder and run:

```bash
cd "C:\Users\bir_k\Documents\raffle-dashboard\raffle-dashboard"
python setup_production.py
```

This will:
- Install all required packages automatically
- Set up the secure database
- Create default admin user
- Configure everything for you

## **Step 3: Start the Application**

```bash
python app.py
```

You should see:
```
🏠 Home Instead Raffle Dashboard Starting...
✅ Database initialized
✅ Security features enabled
🌐 Running on http://localhost:5000
```

## **Step 4: Access Your Dashboard**

1. Open your web browser
2. Go to: http://localhost:5000
3. Login with:
   - **Email**: admin@homeinstead.com
   - **Password**: admin123
4. **IMPORTANT**: Change this password immediately!

---

## **Alternative: Manual Setup**

If the automated setup doesn't work:

### **1. Install Dependencies:**
```bash
pip install Flask python-dotenv bcrypt PyJWT Flask-Limiter openpyxl
```

### **2. Create Environment File:**
Copy `.env.example` to `.env` and update the values

### **3. Run Application:**
```bash
python app.py
```

---

## **Troubleshooting**

### **"Python not found" Error:**
- Install Python from python.org
- Make sure "Add to PATH" was checked during installation
- Try `py` instead of `python`

### **"Module not found" Error:**
```bash
pip install -r requirements-production.txt
```

### **"Permission denied" Error:**
- Run Command Prompt as Administrator
- Or use: `python -m pip install [package]`

### **Port already in use:**
The app will try different ports automatically, or you can specify:
```bash
set PORT=5001
python app.py
```

---

## **🎉 You're Ready!**

Once running, you'll have:
✅ Secure login system
✅ Employee management
✅ Professional raffle system  
✅ Analytics dashboard
✅ Excel import/export
✅ Mobile-responsive design
✅ Automated backups

**Default Login**: admin@homeinstead.com / admin123
**Dashboard URL**: http://localhost:5000

---

## **Next Steps:**

1. **Change default password**
2. **Add your employees** (or import from Excel)
3. **Start tracking raffle entries**
4. **Conduct your first raffle!**

**For FREE hosting**: Check README.md for Render.com, Railway, and Heroku deployment guides.

---

*Need help? Check the README.md file for detailed documentation.*