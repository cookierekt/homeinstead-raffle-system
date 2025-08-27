# 🏠 Home Instead Professional Raffle Dashboard

A **production-ready**, **FREE**, and **secure** quarterly raffle management system designed specifically for Home Instead Senior Care. This professional-grade application includes enterprise security features, beautiful animations, and comprehensive employee management capabilities.

## ✨ Key Features

### 🔒 **Enterprise Security**
- **Multi-Factor Authentication** with JWT tokens
- **Role-Based Access Control** (Admin, Manager, Viewer)
- **Password Security** with bcrypt hashing and strength validation
- **Rate Limiting** to prevent abuse
- **Audit Logging** for compliance and security monitoring
- **CSRF Protection** and security headers
- **SQL Injection Protection** with parameterized queries

### 💼 **Professional Employee Management**
- **Complete Employee Profiles** with photos, contact info, and departments
- **Advanced Search & Filtering** with real-time results
- **Bulk Operations** for efficient management
- **Excel Import/Export** with data validation
- **Department Organization** and hierarchy management
- **Activity Tracking** with detailed history

### 🎯 **Advanced Raffle System**
- **Three-Tier Entry Categories** (High-Impact, Strong Contributions, Everyday Excellence)
- **Weighted Probability** system for fair selection
- **Professional Raffle Wheel** with realistic animations
- **Winner History** and tracking
- **Celebration Effects** with confetti and animations
- **Prize Management** with different categories

### 📊 **Analytics & Reporting**
- **Interactive Dashboard** with real-time statistics
- **Department Performance** analysis
- **Employee Engagement** metrics
- **Activity Trends** and historical data
- **PDF Report Generation** with professional formatting
- **Export Capabilities** in multiple formats

### 🎨 **Beautiful User Experience**
- **Professional UI/UX** with Home Instead branding
- **Dark/Light Theme** support
- **Smooth Animations** and micro-interactions
- **Mobile-Responsive Design** for all devices
- **Progressive Web App (PWA)** capabilities
- **Offline Mode** with data synchronization

## 🚀 **Quick Start (5 Minutes)**

### **Step 1: Download and Setup**
```bash
# Clone or download the project
git clone https://github.com/your-repo/raffle-dashboard.git
cd raffle-dashboard

# Run the automated setup (handles everything!)
python setup_production.py
```

### **Step 2: Start the Application**
```bash
python app.py
```

### **Step 3: Access the Dashboard**
- Open: http://localhost:5000
- Login: `admin@homeinstead.com` / `admin123`
- **Important**: Change the default password immediately!

## 🔧 **Manual Installation**

### **Prerequisites**
- Python 3.7+ (Windows, Mac, or Linux)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### **Dependencies Installation**
```bash
pip install -r requirements-production.txt
```

### **Environment Setup**
1. Copy `.env.example` to `.env`
2. Update the configuration values:
```bash
# Generate secure secrets (use a password generator)
SECRET_KEY=your-super-secret-key-here
JWT_SECRET=your-jwt-secret-here

# Configure for your environment
APP_NAME=Home Instead Raffle Dashboard
COMPANY_NAME=Home Instead Senior Care
```

### **Database Initialization**
```bash
# The database will be automatically created on first run
# Existing JSON data will be migrated automatically
python app.py
```

## 🌐 **Free Hosting Deployment**

### **Option 1: Render.com (Recommended)**
1. Create account at render.com
2. Connect your GitHub repository
3. Deploy with these settings:
   - Build Command: `pip install -r requirements-production.txt`
   - Start Command: `gunicorn app:app`
   - Add environment variables from your `.env` file

### **Option 2: Railway.app**
1. Connect GitHub at railway.app
2. Deploy automatically with zero configuration
3. Add environment variables

### **Option 3: Heroku**
1. Install Heroku CLI
2. Deploy with included `Procfile`
```bash
git push heroku main
```

### **Cost: $0/month** - All options include:
- Automatic SSL certificates
- Custom domain support
- Automatic deployments
- Database hosting
- 99.9% uptime

## 👤 **User Roles & Permissions**

### **Administrator**
- Full system access
- User management
- System reset and backup
- All employee operations
- Analytics and reporting

### **Manager**
- Employee management
- Raffle entry management
- Excel import/export
- Analytics viewing
- Raffle conducting

### **Viewer**
- Dashboard viewing
- Employee list access
- Basic statistics
- Raffle participation viewing

## 📈 **Analytics Features**

### **Dashboard Metrics**
- Total employees and entries
- Department performance
- Recent activity timeline
- Top performer rankings
- Engagement statistics

### **Reporting Capabilities**
- PDF report generation
- Excel export with charts
- Historical data analysis
- Custom date ranges
- Department breakdown

### **Data Visualization**
- Interactive charts and graphs
- Department comparison
- Trend analysis
- Performance metrics
- Real-time updates

## 🔐 **Security Features**

### **Authentication & Authorization**
- Secure login with JWT tokens
- Password strength validation
- Account lockout protection
- Role-based permissions
- Session management

### **Data Protection**
- Database encryption at rest
- Secure file uploads
- Input validation and sanitization
- SQL injection prevention
- XSS protection

### **Audit & Compliance**
- Complete audit trail
- User activity logging
- Change tracking
- Security event monitoring
- GDPR compliance ready

## 🎨 **Customization**

### **Branding**
- Update company logo and colors in `style.css`
- Modify application name in configuration
- Custom email templates
- Branded PDF reports

### **Raffle Categories**
- Modify entry values and categories
- Add custom achievement types
- Update point systems
- Create department-specific rules

### **Features**
- Enable/disable modules via configuration
- Custom notification settings
- Integration with HR systems
- API endpoints for external systems

## 🛠️ **Development**

### **Project Structure**
```
raffle-dashboard/
├── app.py                 # Main Flask application
├── config.py             # Configuration management
├── database.py           # SQLite database manager
├── auth.py               # Authentication system
├── requirements-production.txt
├── setup_production.py   # Automated setup
├── templates/
│   ├── login.html        # Secure login page
│   └── dashboard.html    # Main dashboard
├── static/
│   ├── css/style.css     # Professional styling
│   └── js/script.js      # Interactive features
├── data/                 # SQLite database
├── backups/              # Automatic backups
└── uploads/              # File uploads
```

### **Development Server**
```bash
# Development mode with hot reload
export FLASK_ENV=development
python app.py
```

### **Database Management**
```bash
# Create manual backup
python -c "from database import db; print(db.backup_database())"

# View audit logs
sqlite3 data/raffle_database.db "SELECT * FROM audit_log ORDER BY created_at DESC LIMIT 10;"
```

## 📱 **Mobile Support**

- **Responsive Design** works on all screen sizes
- **Touch-Friendly** interface with gesture support
- **PWA Capabilities** for app-like experience
- **Offline Mode** with data synchronization
- **Fast Loading** optimized for mobile networks

## 🔧 **Troubleshooting**

### **Common Issues**

**Login Issues:**
- Check default credentials: `admin@homeinstead.com` / `admin123`
- Ensure `.env` file is configured correctly
- Check browser console for errors

**Database Issues:**
- Verify `data/` directory exists
- Check file permissions
- Review audit logs for errors

**Import Issues:**
- Ensure Excel file has employee names in a column
- Check file size limits (5MB default)
- Verify file format (.xlsx or .xls)

### **Getting Help**
1. Check the setup logs in console
2. Review the `.env` configuration
3. Ensure all dependencies are installed
4. Check browser developer tools for errors

## 📄 **License**

This project is designed specifically for Home Instead Senior Care. All rights reserved.

## 🤝 **Support**

For technical support and feature requests:
- Review this documentation
- Check troubleshooting section
- Ensure latest version is installed

---

## 🎉 **Ready to Get Started?**

Run this single command to set up your professional raffle dashboard:

```bash
python setup_production.py
```

**That's it!** Your secure, professional-grade raffle dashboard will be ready in minutes.

### **What You Get:**
✅ **$0/month hosting** on professional platforms  
✅ **Enterprise-grade security** with audit trails  
✅ **Beautiful, responsive design** with animations  
✅ **Complete employee management** system  
✅ **Advanced raffle features** with fairness controls  
✅ **Comprehensive analytics** and reporting  
✅ **Mobile-friendly PWA** with offline support  
✅ **Automated backups** and disaster recovery  

Perfect for Home Instead locations of any size - from small teams to large operations!

---

*Built with ❤️ for Home Instead Senior Care teams*