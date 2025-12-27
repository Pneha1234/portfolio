# 🚀 Professional Portfolio Website

A modern, full-stack portfolio website built with Django, featuring a clean design, admin panel for content management, and professional features like appointment booking and newsletter integration.

![Portfolio Preview](https://img.shields.io/badge/Django-4.2.7-green) ![Python](https://img.shields.io/badge/Python-3.9+-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

### 🎨 **Modern Design**
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile
- **Teal Color Scheme**: Professional and modern visual identity
- **Smooth Animations**: Hover effects and transitions throughout
- **Tech Stack Icons**: Beautiful DevIcons for technical skills

### 📊 **Content Management**
- **Django Admin Panel**: Full CRUD operations for all content
- **Skills Management**: Categorized technical skills with proficiency levels
- **Project Showcase**: Featured projects with GitHub integration
- **Blog Integration**: Medium blog posts with automatic formatting
- **Reading Lists**: Books and research papers with ratings and notes

### 💼 **Professional Features**
- **Appointment Booking**: Calendly integration for consultations
- **Contact Form**: Email notifications with form validation
- **Newsletter Subscription**: LinkedIn newsletter integration
- **Resume Integration**: Downloadable resume with profile links
- **SEO Optimized**: Meta tags and structured data

### 🛠 **Technical Stack**
- **Backend**: Django 4.2.7, Python 3.9+
- **Database**: SQLite (easily configurable for PostgreSQL)
- **Frontend**: Bootstrap 5, Custom CSS, DevIcons
- **Email**: Gmail SMTP integration
- **Deployment**: Docker-ready, easy deployment scripts

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Pneha1234/portfolio.git
   cd portfolio
   ```

2. **Run the setup script**
   ```bash
   python deploy.py
   ```
   This will:
   - Create a virtual environment
   - Install dependencies
   - Run database migrations
   - Create a superuser (admin/admin123)
   - Seed sample data

3. **Start the development server**
   ```bash
   source portfolio_env/bin/activate
   python manage.py runserver
   ```

4. **Visit your portfolio**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
portfolio/
├── portfolio/                 # Main Django app
│   ├── models.py             # Database models
│   ├── views.py              # View logic
│   ├── admin.py              # Admin configuration
│   └── management/           # Custom commands
├── templates/                # HTML templates
│   └── portfolio/
├── static/                   # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── portfolio_project/        # Django project settings
├── seed_data.py             # Data seeding script
├── deploy.py                # Setup automation
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🎯 Key Models

### **Profile**
- Personal information, social links, newsletter details
- Editable from admin panel

### **Skill**
- Technical skills with categories, proficiency levels, and icons
- Supports DevIcons for visual representation

### **Project**
- Portfolio projects with GitHub links and technology tags
- Featured projects appear on homepage

### **AppointmentType**
- Consultation types with duration and descriptions
- Integrates with Calendly for booking

### **Book & Paper**
- Reading lists with ratings, reviews, and external links
- Categorized for easy browsing

## ⚙️ Configuration

### **Email Setup**
1. Copy `.env.example` to `.env`
2. Update email settings in `portfolio_project/email_settings.py`
3. Configure Gmail app password for SMTP

### **Customization**
- **Colors**: Update CSS variables in `static/css/style.css`
- **Content**: Use Django admin panel at `/admin/`
- **Skills**: Add DevIcon classes for new technologies
- **Social Links**: Update profile model with your URLs

## 📧 Email Configuration

The portfolio includes a contact form with email notifications. To set up:

1. **Gmail Setup**:
   - Enable 2-factor authentication
   - Generate an app password
   - Update `email_settings.py` with your credentials

2. **Test Email**:
   ```bash
   python portfolio/management/commands/test_email.py
   ```

## 🎨 Customization Guide

### **Adding New Skills**
1. Go to Admin Panel → Skills
2. Add skill name, category, and DevIcon class
3. Set proficiency level and experience years

### **DevIcon Classes**
- Python: `devicon-python-plain`
- Django: `devicon-django-plain`
- AWS: `devicon-amazonwebservices-original`
- Find more at: https://devicon.dev/

### **Color Scheme**
Update CSS variables in `static/css/style.css`:
```css
:root {
  --primary-color: #0891b2;    /* Teal */
  --secondary-color: #059669;   /* Green */
  --accent-color: #06b6d4;      /* Light blue */
}
```

## 🚀 Deployment

### **Local Development**
```bash
python manage.py runserver
```

### **Production Deployment**
1. Update `settings.py` for production
2. Set `DEBUG = False`
3. Configure allowed hosts
4. Use PostgreSQL for database
5. Set up static file serving

### **Docker Deployment**
```dockerfile
# Dockerfile included for containerized deployment
docker build -t portfolio .
docker run -p 8000:8000 portfolio
```

## 📊 Admin Panel Features

### **Content Management**
- ✅ Profile information and social links
- ✅ Technical skills with icons and proficiency
- ✅ Projects with GitHub integration
- ✅ Books and papers with ratings
- ✅ Blog posts and newsletter settings
- ✅ Appointment types and bookings
- ✅ Contact messages and site settings

### **User-Friendly Interface**
- Organized fieldsets and filters
- Inline editing for quick updates
- Search functionality across models
- Rich text editing for descriptions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Django**: Web framework
- **Bootstrap**: CSS framework
- **DevIcons**: Technology icons
- **Font Awesome**: General icons
- **Calendly**: Appointment booking integration

## 📞 Support

If you have questions or need help:
- 📧 Email: nehapandey408@gmail.com
- 💼 LinkedIn: https://www.linkedin.com/in/neha-pandey-profile/
- 📝 Newsletter: https://www.linkedin.com/newsletters/7338893393860657152/
- 🐙 GitHub: https://github.com/Pneha1234

---

**Built with ❤️ and Django**