# Portfolio Admin Guide

## Getting Started

### 1. Access Admin Panel
- URL: `http://127.0.0.1:8000/admin/`
- Default Login: `admin` / `admin`
- **Important**: Change the password after first login!

### 2. Admin Dashboard Overview
The admin panel provides full control over your portfolio content:

- **Profile**: Your personal information and social links
- **Projects**: GitHub repositories and personal projects
- **Books**: Your reading list with ratings and reviews
- **Papers**: Research papers you've read with notes
- **Blog Posts**: Your Medium articles and blog content
- **Appointments**: Manage appointment types and bookings
- **Contact Messages**: Messages from your contact form
- **Site Settings**: Global site configuration

## Content Management

### Profile Management
1. Go to **Portfolio > Profiles**
2. Click on your profile to edit
3. Update:
   - Personal information (name, title, bio)
   - Profile image
   - Contact details (email, phone)
   - Social media links (GitHub, LinkedIn, Medium)
   - Resume URL
   - Calendly URL (for appointment booking integration)

### Adding Projects
1. Go to **Portfolio > Projects**
2. Click **Add Project**
3. Fill in:
   - Title and description (supports rich text)
   - GitHub URL (required)
   - Live demo URL (optional)
   - Project image
   - Technologies (comma-separated)
   - Featured status (shows on homepage)
   - Display order

### Managing Books
1. Go to **Portfolio > Books**
2. Add books with:
   - Title and author
   - Category (Technical, Business, etc.)
   - Goodreads URL
   - Notes URL (optional)
   - Cover image
   - Rating (1-5 stars)
   - Review (rich text)
   - Featured status

### Research Papers
1. Go to **Portfolio > Papers**
2. Add papers with:
   - Title and authors
   - Category (Databases, AI, Systems, etc.)
   - Paper URL
   - Notes URL (optional)
   - Summary and key insights
   - Featured status

### Blog Posts
1. Go to **Portfolio > Blog Posts**
2. Add posts with:
   - Title and description
   - Medium URL
   - Featured image
   - Tags (comma-separated)
   - Publication date
   - Featured status

### Appointments Management

#### Appointment Types
1. Go to **Portfolio > Appointment Types**
2. Create different types of consultations:
   - Name (e.g., "Technical Consultation")
   - Description (what the appointment covers)
   - Duration (15, 30, 45, 60, 90, or 120 minutes)
   - Price (in USD, 0 for free)
   - Calendly event type (optional integration)
   - Active status and display order

#### Managing Appointments
1. Go to **Portfolio > Appointments**
2. View and manage appointment requests:
   - Client information (name, email, phone, company)
   - Appointment type and purpose
   - Preferred and scheduled dates
   - Status (pending, confirmed, completed, cancelled, no_show)
   - Calendly event ID and Google Meet links
   - Internal notes

#### Appointment Features
- **Email Notifications**: Automatic emails sent to nehapandey408@gmail.com
- **Client Confirmations**: Confirmation emails sent to clients
- **Calendly Integration**: Optional direct booking through Calendly
- **Status Tracking**: Track appointment lifecycle
- **Google Calendar**: Integration ready (add Google Calendar ID in Site Settings)

### Contact Messages
- View messages from your contact form
- Mark as read/unread
- Cannot be manually added (form submissions only)

### Site Settings
1. Go to **Portfolio > Site Settings**
2. Configure:
   - Site title and meta description
   - Google Analytics ID
   - Footer text

## Admin Features

### Rich Text Editor
- Use CKEditor for descriptions, bios, and reviews
- Supports formatting, links, and basic HTML
- Upload images directly in the editor

### Image Management
- Upload images for projects, books, and profile
- Automatic resizing and optimization
- Supported formats: JPG, PNG, GIF

### Content Organization
- **Featured**: Mark content to appear on homepage
- **Order**: Set display order (lower numbers first)
- **Categories**: Organize books and papers by type
- **Tags**: Add searchable tags to blog posts

### Bulk Actions
- Select multiple items for bulk operations
- Mark as featured/unfeatured
- Delete multiple items at once

### Search and Filtering
- Search content by title, description, or tags
- Filter by categories, featured status, or dates
- Sort by any column

## Best Practices

### Content Quality
- Write clear, engaging descriptions
- Use high-quality images (recommended: 800x600px)
- Keep technology lists concise and relevant
- Update content regularly

### SEO Optimization
- Use descriptive titles and meta descriptions
- Include relevant keywords in content
- Optimize image alt text
- Keep URLs clean and descriptive

### Performance
- Compress images before uploading
- Limit featured content to 3-6 items per section
- Use external links for large files (PDFs, videos)

### Security
- Change default admin password immediately
- Use strong passwords
- Regularly backup your database
- Keep Django updated

## Troubleshooting

### Common Issues

**Can't access admin panel**
- Check if server is running: `python manage.py runserver`
- Verify URL: `http://127.0.0.1:8000/admin/`
- Clear browser cache

**Images not displaying**
- Check file permissions in `media/` folder
- Verify `MEDIA_URL` and `MEDIA_ROOT` settings
- Ensure images are properly uploaded

**Rich text editor not working**
- Check CKEditor configuration in settings
- Clear browser cache
- Try different browser

**Contact form not working**
- Check email configuration in settings
- Verify CSRF token in form
- Check server logs for errors

### Getting Help
1. Check Django admin documentation
2. Review error logs in terminal
3. Use Django's built-in debugging tools
4. Check the `README.md` for setup instructions

## Backup and Maintenance

### Regular Backups
```bash
# Backup database
python manage.py dumpdata > backup.json

# Backup media files
cp -r media/ backup_media/
```

### Updates
```bash
# Update dependencies
pip install -r requirements.txt --upgrade

# Run migrations after updates
python manage.py migrate
```

### Monitoring
- Check contact messages regularly
- Update content to keep site fresh
- Monitor site performance and loading times
- Review and respond to user feedback

## Email Configuration

### Setting Up Gmail for Contact Form

The contact form can send emails directly to nehapandey408@gmail.com. Here's how to set it up:

#### 1. Gmail App Password Setup
1. **Enable 2-Factor Authentication**:
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Turn on 2-Step Verification

2. **Generate App Password**:
   - Go to [App Passwords](https://myaccount.google.com/apppasswords)
   - Select 'Mail' and 'Other (custom name)'
   - Enter 'Portfolio Website'
   - Copy the 16-character password

#### 2. Configure Email Settings
1. **Open**: `portfolio_project/email_settings.py`
2. **Find**: `'EMAIL_HOST_PASSWORD': 'your-app-password'`
3. **Replace**: with your generated app password
4. **Set**: `USE_PRODUCTION_EMAIL = True`

#### 3. Test Email Configuration
```bash
# Test with console backend (development)
python manage.py test_email

# Test with Gmail SMTP (production)
python manage.py test_email --to your-email@example.com
```

#### 4. Email Features
- **Contact Form**: Saves messages to database
- **Email Notifications**: Sent to nehapandey408@gmail.com
- **Confirmation Emails**: Sent to form submitters
- **Admin Panel**: View all contact messages

#### 5. Development vs Production
- **Development**: Uses console backend (emails shown in terminal)
- **Production**: Uses Gmail SMTP (real emails sent)
- **Switch**: Change `USE_PRODUCTION_EMAIL` in `email_settings.py`

### Email Setup (Production)
Update `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

### Google Analytics
1. Get tracking ID from Google Analytics
2. Add to **Site Settings > Google Analytics ID**
3. Tracking code will be automatically added

### Custom Styling
- Modify `static/css/style.css` for custom styles
- Add new CSS files to `static/css/`
- Update templates in `templates/portfolio/`

Remember: Always test changes in development before deploying to production!