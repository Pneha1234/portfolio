#!/usr/bin/env python
"""
Email Setup Guide for Portfolio Contact Form

This script helps you configure Gmail SMTP for the contact form.
"""

def main():
    print("📧 Email Setup Guide for Portfolio Contact Form")
    print("=" * 60)
    
    print("\n🔧 Gmail SMTP Configuration Steps:")
    print("\n1. Enable 2-Factor Authentication on your Gmail account:")
    print("   - Go to: https://myaccount.google.com/security")
    print("   - Turn on 2-Step Verification")
    
    print("\n2. Generate an App Password:")
    print("   - Go to: https://myaccount.google.com/apppasswords")
    print("   - Select 'Mail' and 'Other (custom name)'")
    print("   - Enter 'Portfolio Website' as the name")
    print("   - Copy the 16-character password")
    
    print("\n3. Update Django Settings:")
    print("   - Open: portfolio_project/settings.py")
    print("   - Find: EMAIL_HOST_PASSWORD = 'your-app-password'")
    print("   - Replace 'your-app-password' with your generated app password")
    
    print("\n4. For Development Testing:")
    print("   - You can use console backend to see emails in terminal")
    print("   - Change EMAIL_BACKEND to 'django.core.mail.backends.console.EmailBackend'")
    
    print("\n5. Environment Variables (Recommended for Production):")
    print("   - Create a .env file with:")
    print("     EMAIL_HOST_PASSWORD=your-app-password-here")
    print("   - Install python-decouple: pip install python-decouple")
    print("   - Update settings.py to use: config('EMAIL_HOST_PASSWORD')")
    
    print("\n📋 Current Configuration:")
    print("   - Email Host: smtp.gmail.com")
    print("   - Port: 587")
    print("   - TLS: Enabled")
    print("   - From Email: nehapandey408@gmail.com")
    print("   - Contact Email: nehapandey408@gmail.com")
    
    print("\n✅ Features Enabled:")
    print("   - Contact form submissions saved to database")
    print("   - Email notifications sent to nehapandey408@gmail.com")
    print("   - Confirmation emails sent to form submitters")
    print("   - Admin panel to view all contact messages")
    
    print("\n🧪 Testing:")
    print("   1. Start the server: python run_server.py")
    print("   2. Go to: http://127.0.0.1:8000/#contact")
    print("   3. Fill out and submit the contact form")
    print("   4. Check your Gmail inbox for the notification")
    print("   5. Check admin panel for saved messages")
    
    print("\n⚠️  Security Notes:")
    print("   - Never commit app passwords to version control")
    print("   - Use environment variables for production")
    print("   - Consider using Django's email backends for different environments")
    
    print("\n🔍 Troubleshooting:")
    print("   - If emails don't send, check the Django console for error messages")
    print("   - Verify 2FA is enabled on your Gmail account")
    print("   - Make sure the app password is correct (16 characters, no spaces)")
    print("   - Check Gmail's 'Less secure app access' settings if needed")

if __name__ == '__main__':
    main()