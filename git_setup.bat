@echo off
REM Portfolio Git Setup Script for Windows
REM This script initializes the repository and pushes to GitHub

echo 🚀 Setting up Portfolio Git Repository
echo ======================================

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git is not installed. Please install Git first.
    pause
    exit /b 1
)

REM Initialize git repository if not already initialized
if not exist ".git" (
    echo 📦 Initializing Git repository...
    git init
) else (
    echo ✅ Git repository already initialized
)

REM Add all files
echo 📁 Adding files to Git...
git add .

REM Create initial commit
echo 💾 Creating initial commit...
git commit -m "🎉 Initial commit: Professional Django Portfolio

✨ Features:
- Modern responsive design with teal color scheme
- Django admin panel for content management
- Tech stack icons with DevIcons integration
- Skills showcase with proficiency levels
- Project portfolio with GitHub integration
- Blog integration with Medium
- Newsletter subscription (LinkedIn)
- Appointment booking system with Calendly
- Contact form with email notifications
- Books and research papers sections
- Comprehensive data seeding
- Production-ready deployment scripts

🛠 Tech Stack:
- Django 4.2.7
- Bootstrap 5
- DevIcons
- SQLite/PostgreSQL ready
- Gmail SMTP integration

🚀 Ready for production deployment!"

REM Add remote origin
echo 🔗 Adding remote repository...
git remote remove origin 2>nul
git remote add origin https://github.com/Pneha1234/portfolio.git

REM Push to GitHub
echo ⬆️  Pushing to GitHub...
git branch -M main
git push -u origin main

echo.
echo 🎉 Repository setup complete!
echo 📍 Your portfolio is now available at:
echo    https://github.com/Pneha1234/portfolio
echo.
echo 🌐 Next steps:
echo 1. Visit your repository: https://github.com/Pneha1234/portfolio
echo 2. Clone on new machine: git clone https://github.com/Pneha1234/portfolio.git
echo 3. Run setup: python deploy.py
echo 4. Start server: python manage.py runserver
echo.
echo ✅ All done! Your professional portfolio is ready! 🚀
pause