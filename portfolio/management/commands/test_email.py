from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings


class Command(BaseCommand):
    help = 'Test email configuration by sending a test email'

    def add_arguments(self, parser):
        parser.add_argument(
            '--to',
            type=str,
            default='nehapandey408@gmail.com',
            help='Email address to send test email to'
        )

    def handle(self, *args, **options):
        recipient_email = options['to']
        
        self.stdout.write('Testing email configuration...')
        self.stdout.write(f'Email Backend: {settings.EMAIL_BACKEND}')
        self.stdout.write(f'Email Host: {getattr(settings, "EMAIL_HOST", "Not configured")}')
        self.stdout.write(f'From Email: {settings.DEFAULT_FROM_EMAIL}')
        self.stdout.write(f'To Email: {recipient_email}')
        
        try:
            send_mail(
                subject='Portfolio Website - Email Test',
                message='''
This is a test email from your Django portfolio website.

If you receive this email, your email configuration is working correctly!

Email settings:
- Backend: {}
- Host: {}
- From: {}

Best regards,
Your Portfolio Website
                '''.format(
                    settings.EMAIL_BACKEND,
                    getattr(settings, 'EMAIL_HOST', 'Console'),
                    settings.DEFAULT_FROM_EMAIL
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient_email],
                fail_silently=False,
            )
            
            self.stdout.write(
                self.style.SUCCESS(f'✅ Test email sent successfully to {recipient_email}')
            )
            
            if settings.EMAIL_BACKEND == 'django.core.mail.backends.console.EmailBackend':
                self.stdout.write(
                    self.style.WARNING('📧 Using console backend - check terminal output above for email content')
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS('📧 Using SMTP backend - check your inbox!')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Failed to send test email: {e}')
            )
            self.stdout.write(
                self.style.WARNING('💡 Check your email configuration in portfolio_project/email_settings.py')
            )