"""
Email configuration for the portfolio project.
This file contains email settings that can be imported into settings.py
"""

# For development - shows emails in console
DEVELOPMENT_EMAIL_CONFIG = {
    'EMAIL_BACKEND': 'django.core.mail.backends.console.EmailBackend',
}

# For production - sends real emails via Gmail SMTP
PRODUCTION_EMAIL_CONFIG = {
    'EMAIL_BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
    'EMAIL_HOST': 'smtp.gmail.com',
    'EMAIL_PORT': 587,
    'EMAIL_USE_TLS': True,
    'EMAIL_HOST_USER': 'nehapandey408@gmail.com',
    'EMAIL_HOST_PASSWORD': 'your-app-password',  # Replace with your Gmail app password
    'DEFAULT_FROM_EMAIL': 'nehapandey408@gmail.com',
    'CONTACT_EMAIL': 'nehapandey408@gmail.com',
}

# You can switch between configurations by changing this
USE_PRODUCTION_EMAIL = False  # Set to True when you have Gmail app password

# Apply the configuration
if USE_PRODUCTION_EMAIL:
    EMAIL_CONFIG = PRODUCTION_EMAIL_CONFIG
else:
    EMAIL_CONFIG = DEVELOPMENT_EMAIL_CONFIG