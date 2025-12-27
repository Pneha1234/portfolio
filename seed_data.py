#!/usr/bin/env python
"""
Comprehensive data seeding script for portfolio
Run this after setting up the database to populate with sample data
"""
import os
import sys
import django
from datetime import datetime, date

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import (
    Profile, Skill, AppointmentType, Project, Book, Paper, 
    BlogPost, SiteSettings, StudyNote, StudyChapter
)

def create_profile():
    """Create or update profile"""
    profile, created = Profile.objects.get_or_create(
        name="Neha Pandey",
        defaults={
            'title': "Senior Software Engineer",
            'bio': """Senior Software Engineer with 5+ years of experience designing and delivering scalable backend systems and cloud-native architectures. Proven expertise in building secure APIs, optimizing distributed systems, and leading teams to deliver high-impact solutions.

Passionate about system design, performance optimization, and mentoring the next generation of engineers. I love diving deep into technical papers, exploring new technologies, and sharing insights through writing and speaking.""",
            'email': 'nehapandey408@gmail.com',
            'github_url': 'https://github.com/Pneha1234',
            'linkedin_url': 'https://www.linkedin.com/in/neha-pandey-profile/',
            'medium_url': 'https://medium.com/@nehapandey408',
            'newsletter_url': 'https://www.linkedin.com/newsletters/7338893393860657152/',
            'newsletter_title': 'Tech Insights Weekly',
            'newsletter_description': 'Weekly deep dives into software engineering, system design patterns, and career growth strategies. Join 500+ tech professionals staying ahead of industry trends.',
            'calendly_url': 'https://calendly.com/nehapandey408',
        }
    )
    print(f"{'Created' if created else 'Updated'} profile: {profile.name}")
    return profile

def create_skills():
    """Create technical skills with icons"""
    skills_data = [
        # Programming Languages
        {'name': 'Python', 'category': 'languages', 'icon_class': 'devicon-python-plain', 'proficiency_level': 4, 'years_experience': 5, 'order': 1},
        {'name': 'JavaScript', 'category': 'languages', 'icon_class': 'devicon-javascript-plain', 'proficiency_level': 3, 'years_experience': 4, 'order': 2},
        {'name': 'TypeScript', 'category': 'languages', 'icon_class': 'devicon-typescript-plain', 'proficiency_level': 3, 'years_experience': 3, 'order': 3},
        {'name': 'SQL', 'category': 'languages', 'icon_class': 'devicon-postgresql-plain', 'proficiency_level': 4, 'years_experience': 5, 'order': 4},
        {'name': 'Java', 'category': 'languages', 'icon_class': 'devicon-java-plain', 'proficiency_level': 3, 'years_experience': 3, 'order': 5},
        {'name': 'Go', 'category': 'languages', 'icon_class': 'devicon-go-plain', 'proficiency_level': 2, 'years_experience': 1, 'order': 6},
        
        # Frameworks & Libraries
        {'name': 'Django', 'category': 'frameworks', 'icon_class': 'devicon-django-plain', 'proficiency_level': 4, 'years_experience': 4, 'order': 1},
        {'name': 'FastAPI', 'category': 'frameworks', 'icon_class': 'devicon-fastapi-plain', 'proficiency_level': 3, 'years_experience': 2, 'order': 2},
        {'name': 'React', 'category': 'frameworks', 'icon_class': 'devicon-react-original', 'proficiency_level': 3, 'years_experience': 3, 'order': 3},
        {'name': 'Node.js', 'category': 'frameworks', 'icon_class': 'devicon-nodejs-plain', 'proficiency_level': 3, 'years_experience': 3, 'order': 4},
        {'name': 'Flask', 'category': 'frameworks', 'icon_class': 'devicon-flask-original', 'proficiency_level': 3, 'years_experience': 2, 'order': 5},
        
        # Databases
        {'name': 'PostgreSQL', 'category': 'databases', 'icon_class': 'devicon-postgresql-plain', 'proficiency_level': 4, 'years_experience': 4, 'order': 1},
        {'name': 'MySQL', 'category': 'databases', 'icon_class': 'devicon-mysql-plain', 'proficiency_level': 3, 'years_experience': 3, 'order': 2},
        {'name': 'Redis', 'category': 'databases', 'icon_class': 'devicon-redis-plain', 'proficiency_level': 3, 'years_experience': 3, 'order': 3},
        {'name': 'MongoDB', 'category': 'databases', 'icon_class': 'devicon-mongodb-plain', 'proficiency_level': 3, 'years_experience': 2, 'order': 4},
        {'name': 'Elasticsearch', 'category': 'databases', 'icon_class': 'devicon-elasticsearch-plain', 'proficiency_level': 2, 'years_experience': 2, 'order': 5},
        
        # Cloud & DevOps
        {'name': 'AWS', 'category': 'cloud_devops', 'icon_class': 'devicon-amazonwebservices-original', 'proficiency_level': 4, 'years_experience': 4, 'order': 1},
        {'name': 'Docker', 'category': 'cloud_devops', 'icon_class': 'devicon-docker-plain', 'proficiency_level': 3, 'years_experience': 3, 'order': 2},
        {'name': 'Kubernetes', 'category': 'cloud_devops', 'icon_class': 'devicon-kubernetes-plain', 'proficiency_level': 3, 'years_experience': 2, 'order': 3},
        {'name': 'CI/CD', 'category': 'cloud_devops', 'icon_class': 'devicon-github-original', 'proficiency_level': 3, 'years_experience': 3, 'order': 4},
        {'name': 'Terraform', 'category': 'cloud_devops', 'icon_class': 'devicon-terraform-plain', 'proficiency_level': 2, 'years_experience': 1, 'order': 5},
        
        # Tools & Technologies
        {'name': 'Git', 'category': 'tools', 'icon_class': 'devicon-git-plain', 'proficiency_level': 4, 'years_experience': 5, 'order': 1},
        {'name': 'Linux', 'category': 'tools', 'icon_class': 'devicon-linux-plain', 'proficiency_level': 3, 'years_experience': 4, 'order': 2},
        {'name': 'REST APIs', 'category': 'tools', 'icon_class': 'fas fa-exchange-alt', 'proficiency_level': 4, 'years_experience': 4, 'order': 3},
        {'name': 'GraphQL', 'category': 'tools', 'icon_class': 'devicon-graphql-plain', 'proficiency_level': 2, 'years_experience': 1, 'order': 4},
    ]
    
    created_count = 0
    for skill_data in skills_data:
        skill, created = Skill.objects.get_or_create(
            name=skill_data['name'],
            category=skill_data['category'],
            defaults=skill_data
        )
        if created:
            created_count += 1
    
    print(f"Created {created_count} skills, total: {Skill.objects.count()}")

def create_appointment_types():
    """Create appointment types"""
    appointment_types = [
        {
            'name': 'Technical Consultation',
            'description': 'Discuss technical challenges, architecture decisions, or get advice on your software projects.',
            'duration': 30,
            'price': 0,
            'order': 1,
            'is_active': True
        },
        {
            'name': 'Career Mentoring',
            'description': 'Get guidance on career development, interview preparation, or transitioning into tech roles.',
            'duration': 45,
            'price': 0,
            'order': 2,
            'is_active': True
        },
        {
            'name': 'Code Review Session',
            'description': 'Review your code, discuss best practices, and get feedback on your implementation.',
            'duration': 60,
            'price': 0,
            'order': 3,
            'is_active': True
        },
        {
            'name': 'System Design Discussion',
            'description': 'Explore system architecture, scalability patterns, and design trade-offs for your project.',
            'duration': 60,
            'price': 0,
            'order': 4,
            'is_active': True
        },
        {
            'name': 'Quick Q&A',
            'description': 'Short session for quick questions, clarifications, or brief technical discussions.',
            'duration': 15,
            'price': 0,
            'order': 5,
            'is_active': True
        }
    ]
    
    created_count = 0
    for apt_data in appointment_types:
        apt_type, created = AppointmentType.objects.get_or_create(
            name=apt_data['name'],
            defaults=apt_data
        )
        if created:
            created_count += 1
    
    print(f"Created {created_count} appointment types, total: {AppointmentType.objects.count()}")

def create_projects():
    """Create sample projects"""
    projects = [
        {
            'title': 'AWS Kinesis Data Tools',
            'description': 'Python utilities and examples for scalable data streaming and analytics using AWS Kinesis. Built comprehensive tools for real-time data processing with error handling and monitoring.',
            'github_url': 'https://github.com/Pneha1234/Kinesis',
            'technologies': 'Python, AWS Kinesis, Boto3, Docker, CloudWatch',
            'featured': True,
            'order': 1
        },
        {
            'title': 'AWS Cloud Workshop',
            'description': 'Hands-on resources and code samples for learning AWS cloud infrastructure and DevOps practices. Includes Terraform configurations and CI/CD pipelines.',
            'github_url': 'https://github.com/Pneha1234/aws_workshop',
            'technologies': 'AWS, Terraform, Docker, CI/CD, CloudFormation',
            'featured': True,
            'order': 2
        },
        {
            'title': 'Python Interview Prep',
            'description': 'Curated Python interview questions and answers for technical interview preparation. Covers algorithms, data structures, and system design concepts.',
            'github_url': 'https://github.com/Pneha1234/Python-Interview',
            'technologies': 'Python, Algorithms, Data Structures, System Design',
            'featured': True,
            'order': 3
        },
        {
            'title': 'Distributed Cache System',
            'description': 'High-performance distributed caching system built with Redis and Python. Implements consistent hashing and automatic failover.',
            'github_url': 'https://github.com/Pneha1234/distributed-cache',
            'technologies': 'Python, Redis, Docker, Kubernetes, Monitoring',
            'featured': True,
            'order': 4
        }
    ]
    
    created_count = 0
    for project_data in projects:
        project, created = Project.objects.get_or_create(
            title=project_data['title'],
            defaults=project_data
        )
        if created:
            created_count += 1
    
    print(f"Created {created_count} projects, total: {Project.objects.count()}")

def create_books():
    """Create sample books"""
    books = [
        {
            'title': 'CPython Internals',
            'author': 'Anthony Shaw',
            'category': 'technical',
            'goodreads_url': 'https://www.goodreads.com/book/show/53412684-cpython-internals',
            'notes_url': '/static/cpython-notes.html',
            'rating': 5,
            'review': 'Excellent deep dive into Python internals. Essential reading for Python developers.',
            'featured': True,
            'order': 1
        },
        {
            'title': 'Designing Data-Intensive Applications',
            'author': 'Martin Kleppmann',
            'category': 'technical',
            'goodreads_url': 'https://www.goodreads.com/book/show/23463279-designing-data-intensive-applications',
            'rating': 5,
            'review': 'The definitive guide to building scalable, reliable systems. A must-read for backend engineers.',
            'featured': True,
            'order': 2
        },
        {
            'title': 'Atomic Habits',
            'author': 'James Clear',
            'category': 'personal_development',
            'goodreads_url': 'https://www.goodreads.com/book/show/40121378-atomic-habits',
            'rating': 5,
            'review': 'Practical framework for building good habits and breaking bad ones.',
            'featured': True,
            'order': 3
        }
    ]
    
    created_count = 0
    for book_data in books:
        book, created = Book.objects.get_or_create(
            title=book_data['title'],
            defaults=book_data
        )
        if created:
            created_count += 1
    
    print(f"Created {created_count} books, total: {Book.objects.count()}")

def create_papers():
    """Create sample research papers"""
    papers = [
        {
            'title': 'Bigtable: A Distributed Storage System for Structured Data',
            'authors': 'Fay Chang, Jeffrey Dean, Sanjay Ghemawat, Wilson C. Hsieh, Deborah A. Wallach, Mike Burrows, Tushar Chandra, Andrew Fikes, Robert E. Gruber',
            'category': 'databases',
            'paper_url': 'https://research.google/pubs/bigtable-a-distributed-storage-system-for-structured-data/',
            'summary': 'Google\'s distributed storage system for managing structured data at scale.',
            'featured': True,
            'order': 1
        },
        {
            'title': 'The Google File System',
            'authors': 'Sanjay Ghemawat, Howard Gobioff, Shun-Tak Leung',
            'category': 'systems',
            'paper_url': 'https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf',
            'summary': 'Scalable distributed file system for large distributed data-intensive applications.',
            'featured': True,
            'order': 2
        },
        {
            'title': 'MapReduce: Simplified Data Processing on Large Clusters',
            'authors': 'Jeffrey Dean, Sanjay Ghemawat',
            'category': 'distributed',
            'paper_url': 'https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/',
            'summary': 'Programming model for processing large data sets with parallel, distributed algorithms.',
            'featured': True,
            'order': 3
        }
    ]
    
    created_count = 0
    for paper_data in papers:
        paper, created = Paper.objects.get_or_create(
            title=paper_data['title'],
            defaults=paper_data
        )
        if created:
            created_count += 1
    
    print(f"Created {created_count} papers, total: {Paper.objects.count()}")

def create_blog_posts():
    """Create sample blog posts"""
    blog_posts = [
        {
            'title': 'CPython Interpreter: From Source Code to Execution',
            'description': 'A deep dive into how the CPython interpreter works, from parsing source code to executing instructions.',
            'medium_url': 'https://medium.com/@nehapandey408/cpython-interpreter-from-source-code-to-execution-36f9084705e0',
            'published_date': date(2023, 8, 15),
            'tags': 'Python, CPython, Interpreter, Performance',
            'featured': True,
            'order': 1
        },
        {
            'title': 'Introduction to Operating Systems',
            'description': 'An overview of operating system concepts, architecture, and why they matter for developers.',
            'medium_url': 'https://medium.com/@nehapandey408/introduction-to-operating-systems-d4138a3d1282',
            'published_date': date(2023, 7, 20),
            'tags': 'Operating Systems, Computer Science, Systems Programming',
            'featured': True,
            'order': 2
        },
        {
            'title': 'Why Do We Need a Garbage Collector?',
            'description': 'Explains the importance of garbage collection in programming languages and how it works under the hood.',
            'medium_url': 'https://medium.com/@nehapandey408/why-do-we-need-a-garbage-collector-a-comprehensive-explanation-e1434d2d9765',
            'published_date': date(2023, 6, 10),
            'tags': 'Memory Management, Garbage Collection, Programming Languages',
            'featured': True,
            'order': 3
        }
    ]
    
    created_count = 0
    for post_data in blog_posts:
        post, created = BlogPost.objects.get_or_create(
            title=post_data['title'],
            defaults=post_data
        )
        if created:
            created_count += 1
    
    print(f"Created {created_count} blog posts, total: {BlogPost.objects.count()}")

def create_site_settings():
    """Create site settings"""
    settings, created = SiteSettings.objects.get_or_create(
        site_title="Neha Pandey | Senior Software Engineer",
        defaults={
            'meta_description': 'Senior Software Engineer with 5+ years of experience in Python, Django, AWS, and distributed systems. Passionate about system design and mentoring.',
            'footer_text': 'Built with Django and passion for clean code.',
            'google_analytics_id': '',  # Add your GA ID here
        }
    )
    print(f"{'Created' if created else 'Updated'} site settings")

def main():
    """Run all data seeding functions"""
    print("🌱 Starting data seeding...")
    print("=" * 50)
    
    create_profile()
    create_skills()
    create_appointment_types()
    create_projects()
    create_books()
    create_papers()
    create_blog_posts()
    create_site_settings()
    
    print("=" * 50)
    print("✅ Data seeding completed successfully!")
    print("\n📊 Summary:")
    print(f"   • Profile: {Profile.objects.count()}")
    print(f"   • Skills: {Skill.objects.count()}")
    print(f"   • Appointment Types: {AppointmentType.objects.count()}")
    print(f"   • Projects: {Project.objects.count()}")
    print(f"   • Books: {Book.objects.count()}")
    print(f"   • Papers: {Paper.objects.count()}")
    print(f"   • Blog Posts: {BlogPost.objects.count()}")
    print(f"   • Site Settings: {SiteSettings.objects.count()}")

if __name__ == '__main__':
    main()