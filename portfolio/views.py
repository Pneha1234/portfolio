from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .models import (Profile, Project, Book, Paper, BlogPost, ContactMessage, 
                     SiteSettings, AppointmentType, Appointment, Skill)
import json


def home(request):
    """Main portfolio page"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    try:
        site_settings = SiteSettings.objects.first()
    except SiteSettings.DoesNotExist:
        site_settings = None
    
    # Get featured and recent content
    projects = Project.objects.filter(featured=True)[:4]
    books = Book.objects.filter(featured=True)[:3]
    papers = Paper.objects.filter(featured=True)[:6]
    blog_posts = BlogPost.objects.filter(featured=True)[:3]
    
    # Get skills grouped by category
    skills_by_category = {}
    skills = Skill.objects.filter(is_featured=True).order_by('category', 'order', 'name')
    for skill in skills:
        category = skill.get_category_display()
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)
    
    context = {
        'profile': profile,
        'site_settings': site_settings,
        'projects': projects,
        'books': books,
        'papers': papers,
        'blog_posts': blog_posts,
        'skills_by_category': skills_by_category,
    }
    
    return render(request, 'portfolio/index.html', context)


def projects_list(request):
    """All projects page"""
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'page_title': 'All Projects'
    }
    return render(request, 'portfolio/projects.html', context)


def books_list(request):
    """All books page"""
    books = Book.objects.all()
    categories = Book.CATEGORY_CHOICES
    
    # Filter by category if specified
    category = request.GET.get('category')
    if category:
        books = books.filter(category=category)
    
    context = {
        'books': books,
        'categories': categories,
        'selected_category': category,
        'page_title': 'My Bookshelf'
    }
    return render(request, 'portfolio/books.html', context)


def papers_list(request):
    """All papers page"""
    papers = Paper.objects.all()
    categories = Paper.CATEGORY_CHOICES
    
    # Filter by category if specified
    category = request.GET.get('category')
    if category:
        papers = papers.filter(category=category)
    
    context = {
        'papers': papers,
        'categories': categories,
        'selected_category': category,
        'page_title': 'Research Papers'
    }
    return render(request, 'portfolio/papers.html', context)


def blog_list(request):
    """All blog posts page"""
    blog_posts = BlogPost.objects.all()
    context = {
        'blog_posts': blog_posts,
        'page_title': 'Blog Posts'
    }
    return render(request, 'portfolio/blog.html', context)


def appointments(request):
    """Appointments booking page"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    appointment_types = AppointmentType.objects.filter(is_active=True)
    
    context = {
        'profile': profile,
        'appointment_types': appointment_types,
        'page_title': 'Book an Appointment'
    }
    return render(request, 'portfolio/appointments.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def appointment_submit(request):
    """Handle appointment booking form submission"""
    try:
        data = json.loads(request.body)
        
        # Extract form data
        appointment_type_id = data.get('appointment_type')
        client_name = data.get('client_name')
        client_email = data.get('client_email')
        client_phone = data.get('client_phone', '')
        company = data.get('company', '')
        purpose = data.get('purpose')
        preferred_date = data.get('preferred_date')
        
        # Validate required fields
        if not all([appointment_type_id, client_name, client_email, purpose]):
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all required fields.'
            }, status=400)
        
        # Get appointment type
        try:
            appointment_type = AppointmentType.objects.get(id=appointment_type_id, is_active=True)
        except AppointmentType.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Invalid appointment type selected.'
            }, status=400)
        
        # Parse preferred date if provided
        preferred_datetime = None
        if preferred_date:
            from datetime import datetime
            try:
                preferred_datetime = datetime.fromisoformat(preferred_date.replace('Z', '+00:00'))
            except ValueError:
                pass
        
        # Create appointment
        appointment = Appointment.objects.create(
            appointment_type=appointment_type,
            client_name=client_name,
            client_email=client_email,
            client_phone=client_phone,
            company=company,
            purpose=purpose,
            preferred_date=preferred_datetime,
            status='pending'
        )
        
        # Send email notification
        try:
            # Email to you (Neha)
            email_subject = f"New Appointment Request: {appointment_type.name}"
            email_message = f"""
New appointment request from your portfolio website:

Client: {client_name}
Email: {client_email}
Phone: {client_phone}
Company: {company}
Appointment Type: {appointment_type.name} ({appointment_type.duration} minutes)
Purpose: {purpose}
Preferred Date: {preferred_datetime.strftime('%B %d, %Y at %I:%M %p') if preferred_datetime else 'Not specified'}

You can manage this appointment in your admin panel.

---
Appointment ID: {appointment.id}
"""
            
            send_mail(
                subject=email_subject,
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            
            # Confirmation email to client
            confirmation_subject = f"Appointment Request Received - {appointment_type.name}"
            confirmation_message = f"""
Hi {client_name},

Thank you for requesting an appointment through my portfolio website. I've received your request for a {appointment_type.name} session.

Details:
- Appointment Type: {appointment_type.name} ({appointment_type.duration} minutes)
- Purpose: {purpose}
- Preferred Date: {preferred_datetime.strftime('%B %d, %Y at %I:%M %p') if preferred_datetime else 'To be scheduled'}

I'll review your request and get back to you within 24 hours to confirm the appointment details and send you a calendar invite.

Best regards,
Neha Pandey
Senior Software Engineer

---
This is an automated confirmation. You can reply to this email if you have any questions.
"""
            
            send_mail(
                subject=confirmation_subject,
                message=confirmation_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[client_email],
                fail_silently=True,
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Thank you! Your appointment request has been submitted successfully. I\'ll get back to you within 24 hours to confirm the details.'
            })
            
        except Exception as e:
            # If email fails, still save the appointment
            return JsonResponse({
                'success': True,
                'message': 'Your appointment request has been saved. I\'ll get back to you soon to confirm the details.'
            })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid data format.'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'An error occurred. Please try again.'
        }, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def contact_submit(request):
    """Handle contact form submission with email sending"""
    try:
        data = json.loads(request.body)
        sender_email = data.get('sender')
        subject = data.get('subject')
        message = data.get('message')
        
        if not all([sender_email, subject, message]):
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all fields.'
            }, status=400)
        
        # Save contact message to database
        contact_message = ContactMessage.objects.create(
            sender_email=sender_email,
            subject=subject,
            message=message
        )
        
        # Send email notification
        try:
            # Email to you (Neha)
            email_subject = f"Portfolio Contact: {subject}"
            email_message = f"""
New contact form submission from your portfolio website:

From: {sender_email}
Subject: {subject}

Message:
{message}

---
This message was sent from your portfolio contact form.
You can reply directly to {sender_email}
"""
            
            send_mail(
                subject=email_subject,
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            
            # Optional: Send confirmation email to sender
            confirmation_subject = "Thank you for contacting Neha Pandey"
            confirmation_message = f"""
Hi there,

Thank you for reaching out through my portfolio website. I've received your message about "{subject}" and will get back to you as soon as possible.

Best regards,
Neha Pandey
Senior Software Engineer

---
This is an automated confirmation. Please do not reply to this email.
"""
            
            send_mail(
                subject=confirmation_subject,
                message=confirmation_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[sender_email],
                fail_silently=True,  # Don't fail if confirmation email fails
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Thank you! Your message has been sent successfully. I\'ll get back to you soon.'
            })
            
        except BadHeaderError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid header found. Please check your input.'
            }, status=400)
            
        except Exception as e:
            # If email fails, still save the message but inform user
            return JsonResponse({
                'success': True,
                'message': 'Your message has been saved. I\'ll get back to you soon.'
            })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid data format.'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'An error occurred. Please try again.'
        }, status=500)