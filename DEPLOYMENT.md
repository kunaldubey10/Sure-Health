# Sure Health - Deployment Guide

## 🚀 Quick Deployment Steps

### Prerequisites
- GitHub account
- Git installed on your computer
- Your repository pushed to GitHub

---

## Option 1: Deploy on Render (Recommended - FREE)

### Step-by-Step:

1. **Push to GitHub** (if not already done)
```bash
cd "c:\Users\KUNAL KUMAR DUBEY\Sure-Health"
git add .
git commit -m "Ready for deployment"
git push origin main
```

2. **Go to Render**
   - Visit: https://render.com
   - Click "Get Started" or "Sign Up"
   - Sign up with GitHub

3. **Create New Web Service**
   - Click "New +" button
   - Select "Web Service"
   - Connect your GitHub repository: `kunaldubey10/Sure-Health`
   - Click "Connect"

4. **Configure Service**
   - **Name**: `sure-health` (or any name you prefer)
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Root Directory**: Leave blank
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn flask_app:app`
   - **Instance Type**: `Free`

5. **Deploy**
   - Click "Create Web Service"
   - Wait 5-10 minutes for deployment
   - Your app will be live at: `https://sure-health.onrender.com`

---

## Option 2: Deploy on Railway (FREE)

### Step-by-Step:

1. **Go to Railway**
   - Visit: https://railway.app
   - Click "Start a New Project"
   - Login with GitHub

2. **Deploy from GitHub**
   - Click "Deploy from GitHub repo"
   - Select: `kunaldubey10/Sure-Health`
   - Click "Deploy Now"

3. **Add Domain**
   - Go to Settings
   - Click "Generate Domain"
   - Your app will be live at: `https://sure-health.up.railway.app`

**That's it!** Railway automatically detects Python and deploys.

---

## Option 3: Deploy on PythonAnywhere (FREE)

### Step-by-Step:

1. **Create Account**
   - Visit: https://www.pythonanywhere.com
   - Sign up for free account

2. **Upload Code**
   - Go to "Files" tab
   - Create new directory: `sure-health`
   - Upload all your files

3. **Install Dependencies**
   - Go to "Consoles" tab
   - Start Bash console
   ```bash
   cd sure-health
   pip install --user -r requirements.txt
   ```

4. **Configure Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Select "Python 3.10"

5. **Edit WSGI File**
   Click on WSGI configuration file, replace content with:
   ```python
   import sys
   import os
   
   project_home = '/home/YOUR_USERNAME/sure-health'
   if project_home not in sys.path:
       sys.path = [project_home] + sys.path
   
   os.chdir(project_home)
   
   from flask_app import app as application
   ```

6. **Set Working Directory**
   - In Web tab, set:
   - **Source code**: `/home/YOUR_USERNAME/sure-health`
   - **Working directory**: `/home/YOUR_USERNAME/sure-health`

7. **Reload**
   - Click "Reload" button
   - Visit: `https://YOUR_USERNAME.pythonanywhere.com`

---

## Option 4: Deploy on Vercel (For Frontend)

**Note**: Vercel is great for frontend but Flask needs serverless functions.

1. **Install Vercel CLI**
```bash
npm install -g vercel
```

2. **Create vercel.json**
Already created in your project

3. **Deploy**
```bash
vercel
```

---

## 🔧 Important Notes

### Environment Variables
If you need to add environment variables (API keys, secrets):

**Render**:
- Go to Environment tab
- Add key-value pairs

**Railway**:
- Go to Variables tab
- Add variables

**PythonAnywhere**:
- Edit WSGI file to include environment variables

### Custom Domain
All platforms support custom domains:
1. Buy domain (GoDaddy, Namecheap, etc.)
2. Add CNAME record pointing to your deployment URL
3. Configure in platform settings

### SSL Certificate
All platforms provide FREE SSL certificates automatically!

---

## 📊 Platform Comparison

| Platform | Free Tier | Auto Deploy | Custom Domain | SSL | Ease |
|----------|-----------|-------------|---------------|-----|------|
| **Render** | ✅ 750hrs/month | ✅ | ✅ | ✅ | ⭐⭐⭐⭐⭐ |
| **Railway** | ✅ $5 credit | ✅ | ✅ | ✅ | ⭐⭐⭐⭐⭐ |
| **PythonAnywhere** | ✅ Limited | ❌ | ⚠️ Paid | ✅ | ⭐⭐⭐ |
| **Vercel** | ✅ Unlimited | ✅ | ✅ | ✅ | ⭐⭐⭐⭐ |

---

## 🎯 Recommended: Render

**Why Render?**
- ✅ Easiest to use
- ✅ Free tier is generous (750 hours/month)
- ✅ Automatic deploys from GitHub
- ✅ Free SSL certificate
- ✅ Custom domain support
- ✅ Good for Flask apps

---

## 🐛 Troubleshooting

### Port Issues
Make sure flask_app.py has:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

### Model Not Loading
Ensure `insurance_model.pkl` is in root directory and pushed to GitHub.

### Static Files Not Loading
Check that `static/` folder is properly structured and pushed to GitHub.

---

## 📞 Need Help?

Contact the Sure Health team:
- Avinash: avinashkumarjnv05@gmail.com
- Harsh: harshvardhansingh8171@gmail.com
- Kunal: kunaldubeyslp@gmail.com

---

## 🎉 Post-Deployment Checklist

- [ ] Website loads correctly
- [ ] All pages are accessible
- [ ] Navigation works
- [ ] BMI Calculator functions
- [ ] Insurance Predictor works
- [ ] Emergency numbers are clickable
- [ ] Hospital finder opens Google Maps
- [ ] Mental Health section displays
- [ ] Mobile responsive design works
- [ ] Forms submit properly

---

**Good Luck! 🚀**

Your Sure Health website is now ready to help people around the world!
