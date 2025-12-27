# 📧 Email Setup Guide - Portfolio Contact Form

Your portfolio contact form is now configured to send emails directly to **nehapandey408@gmail.com**!

## ✅ What's Already Configured

- **Contact Form**: Saves all messages to database
- **Email Notifications**: Configured to send to nehapandey408@gmail.com
- **Confirmation Emails**: Automatic replies to form submitters
- **Admin Panel**: View and manage all contact messages
- **Development Mode**: Currently using console backend (emails shown in terminal)

## 🔧 Quick Setup for Real Emails

### Step 1: Enable Gmail App Password
1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable **2-Step Verification**
3. Go to [App Passwords](https://myaccount.google.com/apppasswords)
4. Create app password for "Portfolio Website"
5. Copy the 16-character password

### Step 2: Configure Email Settings
1. Open: `portfolio_project/email_settings.py`
2. Replace `'your-app-password'` with your Gmail app password
3. Change `USE_PRODUCTION_EMAIL = True`

### Step 3: Test Email Setup
```bash
# Test email configuration
python manage.py test_email

# Test contact form
python test_contact_form.py
```

## 📋 Current Features

### Contact Form Functionality
- ✅ **Form Validation**: Checks all required fields
- ✅ **Database Storage**: All messages saved automatically
- ✅ **Email Notifications**: Sent to nehapandey408@gmail.com
- ✅ **Confirmation Emails**: Sent to form submitters
- ✅ **Error Handling**: Graceful failure handling
- ✅ **Admin Management**: View messages in admin panel

### Email Content
**Notification Email (to you):**
```
Subject: Portfolio Contact: [User's Subject]

New contact form submission from your portfolio website:

From: user@example.com
Subject: User's subject

Message:
User's message content

---
This message was sent from your portfolio contact form.
You can reply directly to user@example.com
```

**Confirmation Email (to user):**
```
Subject: Thank you for contacting Neha Pandey

Hi there,

Thank you for reaching out through my portfolio website. 
I've received your message about "[subject]" and will get 
back to you as soon as possible.

Best regards,
Neha Pandey
Senior Software Engineer
```

## 🧪 Testing

### Test Contact Form
1. **Start Server**: `python run_server.py`
2. **Visit**: http://127.0.0.1:8000/#contact
3. **Fill Form**: Enter test data and submit
4. **Check Results**:
   - Console output (development mode)
   - Gmail inbox (production mode)
   - Admin panel for saved messages

### Test Commands
```bash
# Test email configuration
python manage.py test_email

# Test contact form via script
python test_contact_form.py

# View contact messages in admin
# Go to: http://127.0.0.1:8000/admin/
# Login: admin / admin
# Navigate: Portfolio → Contact Messages
```

## 🔄 Development vs Production

### Development Mode (Current)
- **Backend**: Console (emails shown in terminal)
- **Testing**: Perfect for development and testing
- **Setup**: No Gmail configuration needed

### Production Mode
- **Backend**: Gmail SMTP
- **Real Emails**: Sent to nehapandey408@gmail.com
- **Setup**: Requires Gmail app password

## 📁 File Structure

```
portfolio_project/
├── email_settings.py          # Email configuration
├── settings.py               # Main Django settings
portfolio/
├── views.py                  # Contact form handler
├── models.py                 # ContactMessage model
├── management/commands/
│   └── test_email.py        # Email testing command
templates/portfolio/
├── index.html               # Contact form template
test_contact_form.py         # Contact form test script
EMAIL_SETUP_GUIDE.md         # This guide
```

## 🔒 Security Notes

- ✅ **App Passwords**: More secure than regular passwords
- ✅ **Environment Variables**: Recommended for production
- ✅ **No Hardcoded Secrets**: Passwords not in version control
- ✅ **Error Handling**: Graceful failure without exposing details

## 🚀 Ready to Use!

Your contact form is ready to receive messages! 

**Current Status**: Development mode (console emails)
**To Enable Real Emails**: Follow Step 2 above to configure Gmail

**Admin Panel**: http://127.0.0.1:8000/admin/
**Contact Form**: http://127.0.0.1:8000/#contact

All contact messages are automatically saved to the database and can be viewed in the admin panel, regardless of email configuration!