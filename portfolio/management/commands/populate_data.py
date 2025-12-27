from django.core.management.base import BaseCommand
from portfolio.models import (Profile, Project, Book, Paper, BlogPost, SiteSettings, 
                             StudyNote, StudyChapter, AppointmentType)
from datetime import date


class Command(BaseCommand):
    help = 'Populate the database with initial portfolio data'

    def handle(self, *args, **options):
        self.stdout.write('Populating database with initial data...')

        # Create Profile
        profile, created = Profile.objects.get_or_create(
            defaults={
                'name': 'Neha Pandey',
                'title': 'Senior Software Engineer',
                'bio': '''<p>Senior Software Engineer with 5+ years of experience designing and delivering scalable backend systems and cloud-native architectures.</p>
                
                <p>Proven expertise in building secure APIs, optimizing distributed systems, and leading teams to deliver high-impact solutions. Skilled in AWS, Python frameworks (FastAPI, Django, Flask), and Generative AI (LLMs, prompt engineering, fine-tuning).</p>
                
                <p>Passionate about system design, technical excellence, and mentoring engineers.</p>''',
                'email': 'nehapandey408@gmail.com',
                'phone': '+977-9844298042',
                'github_url': 'https://github.com/Pneha1234',
                'linkedin_url': 'https://www.linkedin.com/in/neha-pandey-dev/',
                'medium_url': 'https://medium.com/@nehapandey408',
                'resume_url': 'https://drive.google.com/file/d/1yKUeSk6wJWc3ajlMoTA7jpVVM09-lz4O/view?usp=drive_link'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Profile created'))

        # Create CPython Study Notes
        cpython_study, created = StudyNote.objects.get_or_create(
            book_title='CPython Internals',
            defaults={
                'book_author': 'Anthony Shaw',
                'book_description': '''<p>A comprehensive guide to understanding how Python works under the hood. From the lexical analysis to bytecode execution, this book covers the complete journey of Python code execution.</p>
                
                <p>Perfect for Python developers who want to understand the internals of the language and contribute to CPython development.</p>''',
                'book_cover_url': 'https://images-na.ssl-images-amazon.com/images/I/41J9XjNbXzL._SX331_BO1,204,203,200_.jpg',
                'total_chapters': 8,
                'completed_chapters': 3,
                'featured': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('CPython study notes created'))

            # Create chapters for CPython study
            chapters_data = [
                {
                    'chapter_number': 1,
                    'title': 'Introduction to CPython',
                    'description': 'Overview of Python\'s architecture, the role of CPython, and how it differs from other Python implementations. Understanding the compilation pipeline from source to bytecode.',
                    'status': 'completed',
                    'notes_url': 'https://medium.com/@nehapandey408/cpython-interpreter-from-source-code-to-execution-36f9084705e0',
                    'order': 1
                },
                {
                    'chapter_number': 2,
                    'title': 'Lexical Analysis & Parsing',
                    'description': 'Deep dive into how Python source code is tokenized and parsed. Understanding the Grammar file, AST generation, and the role of the parser in the compilation process.',
                    'status': 'completed',
                    'order': 2
                },
                {
                    'chapter_number': 3,
                    'title': 'The Compiler',
                    'description': 'How the AST is compiled into bytecode. Understanding the compilation phases, optimization passes, and the bytecode instruction set.',
                    'status': 'completed',
                    'order': 3
                },
                {
                    'chapter_number': 4,
                    'title': 'The Interpreter Loop',
                    'description': 'The heart of CPython - the bytecode interpreter. Understanding the evaluation loop, stack operations, and how Python executes bytecode instructions.',
                    'status': 'in_progress',
                    'order': 4
                },
                {
                    'chapter_number': 5,
                    'title': 'Objects & Types',
                    'description': 'Deep dive into Python\'s object model. Understanding PyObject, reference counting, type objects, and how Python manages memory for different data types.',
                    'status': 'planned',
                    'order': 5
                },
                {
                    'chapter_number': 6,
                    'title': 'Memory Management',
                    'description': 'Understanding Python\'s memory management, garbage collection, reference counting, and how CPython handles memory allocation and deallocation.',
                    'status': 'planned',
                    'order': 6
                },
                {
                    'chapter_number': 7,
                    'title': 'Concurrency & Threading',
                    'description': 'The Global Interpreter Lock (GIL), threading in Python, and how CPython handles concurrent execution. Understanding the trade-offs and limitations.',
                    'status': 'planned',
                    'order': 7
                },
                {
                    'chapter_number': 8,
                    'title': 'Extending CPython',
                    'description': 'Building C extensions, understanding the Python C API, and how to extend CPython with native code for performance-critical applications.',
                    'status': 'planned',
                    'order': 8
                }
            ]

            for chapter_data in chapters_data:
                StudyChapter.objects.create(
                    study_note=cpython_study,
                    **chapter_data
                )
            
            self.stdout.write(self.style.SUCCESS('CPython chapters created'))

        # Create Projects
        projects_data = [
            {
                'title': 'AWS Kinesis Data Tools',
                'description': 'Python utilities and examples for scalable data streaming and analytics using AWS Kinesis.',
                'github_url': 'https://github.com/Pneha1234/Kinesis',
                'technologies': 'Python, AWS Kinesis, Data Streaming, Analytics',
                'featured': True,
                'order': 1
            },
            {
                'title': 'AWS Cloud Workshop',
                'description': 'Hands-on resources and code samples for learning AWS cloud infrastructure, automation, and DevOps best practices.',
                'github_url': 'https://github.com/Pneha1234/aws_workshop',
                'technologies': 'AWS, DevOps, Infrastructure, Automation',
                'featured': True,
                'order': 2
            },
            {
                'title': 'Python Interview Prep',
                'description': 'Curated Python interview questions and answers to help you prepare for technical interviews and coding rounds.',
                'github_url': 'https://github.com/Pneha1234/Python-Interview',
                'technologies': 'Python, Interview Prep, Algorithms, Data Structures',
                'featured': True,
                'order': 3
            },
            {
                'title': 'LeetCode Solutions',
                'description': 'Comprehensive solutions to popular LeetCode problems, with explanations and code for Python learners.',
                'github_url': 'https://github.com/Pneha1234/LeetCode',
                'technologies': 'Python, Algorithms, Problem Solving, LeetCode',
                'featured': True,
                'order': 4
            }
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'Project "{project.title}" created')

        # Create Books
        books_data = [
            {
                'title': 'CPython Internals',
                'author': 'Anthony Shaw',
                'category': 'technical',
                'goodreads_url': 'https://www.goodreads.com/book/show/53412684-cpython-internals',
                'notes_url': '/static/cpython-notes.html',
                'rating': 5,
                'featured': True,
                'order': 1
            },
            {
                'title': 'Atomic Habits',
                'author': 'James Clear',
                'category': 'personal_development',
                'goodreads_url': 'https://www.goodreads.com/book/show/40121378-atomic-habits',
                'rating': 5,
                'featured': True,
                'order': 2
            },
            {
                'title': 'The Pragmatic Programmer',
                'author': 'Andrew Hunt, David Thomas',
                'category': 'technical',
                'goodreads_url': 'https://www.goodreads.com/book/show/4099.The_Pragmatic_Programmer',
                'rating': 5,
                'featured': True,
                'order': 3
            }
        ]

        for book_data in books_data:
            book, created = Book.objects.get_or_create(
                title=book_data['title'],
                defaults=book_data
            )
            if created:
                self.stdout.write(f'Book "{book.title}" created')

        # Create Papers
        papers_data = [
            {
                'title': 'Bigtable: A Distributed Storage System for Structured Data',
                'authors': 'Fay Chang, Jeffrey Dean, Sanjay Ghemawat, Wilson C. Hsieh, Deborah A. Wallach, Mike Burrows, Tushar Chandra, Andrew Fikes, Robert E. Gruber',
                'category': 'databases',
                'paper_url': 'https://research.google/pubs/bigtable-a-distributed-storage-system-for-structured-data/',
                'featured': True,
                'order': 1
            },
            {
                'title': 'F1: A Distributed SQL Database That Scales',
                'authors': 'Jeff Shute, Radek Vingralek, Bart Samwel, Ben Handy, Chad Whipkey, Eric Rollins, Mircea Oancea, Kyle Littlefield, David Menestrina, Stephan Ellner, John Cieslewicz, Ian Rae, Traian Stancescu, Himani Apte',
                'category': 'databases',
                'paper_url': 'https://research.google/pubs/f1-a-distributed-sql-database-that-scales/',
                'featured': True,
                'order': 2
            },
            {
                'title': 'The Google File System (GFS)',
                'authors': 'Sanjay Ghemawat, Howard Gobioff, Shun-Tak Leung',
                'category': 'systems',
                'paper_url': 'https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf',
                'featured': True,
                'order': 3
            },
            {
                'title': 'CPU/Memory Article',
                'authors': 'Ulrich Drepper',
                'category': 'systems',
                'paper_url': 'https://people.freebsd.org/~lstewart/articles/cpumemory.pdf',
                'featured': True,
                'order': 4
            },
            {
                'title': 'In praise of empathic AI',
                'authors': 'Various Authors',
                'category': 'ai',
                'paper_url': 'https://arxiv.org/abs/2106.01301',
                'featured': True,
                'order': 5
            }
        ]

        for paper_data in papers_data:
            paper, created = Paper.objects.get_or_create(
                title=paper_data['title'],
                defaults=paper_data
            )
            if created:
                self.stdout.write(f'Paper "{paper.title}" created')

        # Create Blog Posts
        blog_posts_data = [
            {
                'title': 'CPython Interpreter: From Source Code to Execution',
                'description': 'A deep dive into how the CPython interpreter works, from parsing source code to executing instructions.',
                'medium_url': 'https://medium.com/@nehapandey408/cpython-interpreter-from-source-code-to-execution-36f9084705e0',
                'tags': 'Python, CPython, Interpreter, Programming',
                'published_date': date(2023, 8, 15),
                'featured': True,
                'order': 1
            },
            {
                'title': 'Introduction to Operating Systems',
                'description': 'An overview of operating system concepts, architecture, and why they matter for developers.',
                'medium_url': 'https://medium.com/@nehapandey408/introduction-to-operating-systems-d4138a3d1282',
                'tags': 'Operating Systems, Computer Science, Programming',
                'published_date': date(2023, 7, 20),
                'featured': True,
                'order': 2
            },
            {
                'title': 'Why Do We Need a Garbage Collector? A Comprehensive Explanation',
                'description': 'Explains the importance of garbage collection in programming languages and how it works under the hood.',
                'medium_url': 'https://medium.com/@nehapandey408/why-do-we-need-a-garbage-collector-a-comprehensive-explanation-e1434d2d9765',
                'tags': 'Garbage Collection, Memory Management, Programming',
                'published_date': date(2023, 6, 10),
                'featured': True,
                'order': 3
            }
        ]

        for blog_data in blog_posts_data:
            blog_post, created = BlogPost.objects.get_or_create(
                title=blog_data['title'],
                defaults=blog_data
            )
            if created:
                self.stdout.write(f'Blog post "{blog_post.title}" created')

        # Create Site Settings
        site_settings, created = SiteSettings.objects.get_or_create(
            defaults={
                'site_title': 'Neha Pandey | Portfolio',
                'meta_description': 'Senior Software Engineer with 5+ years of experience designing and delivering scalable backend systems and cloud-native architectures.',
                'footer_text': 'All rights reserved.'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Site settings created'))

        # Create Appointment Types
        appointment_types_data = [
            {
                'name': 'Technical Consultation',
                'description': 'Get expert advice on system design, architecture decisions, or technical challenges. Perfect for discussing scalable solutions, cloud architecture, or code reviews.',
                'duration': 60,
                'price': 150.00,
                'calendly_event_type': 'technical-consultation',
                'order': 1
            },
            {
                'name': 'Career Mentoring',
                'description': 'One-on-one career guidance for software engineers. Discuss career paths, interview preparation, skill development, and professional growth strategies.',
                'duration': 45,
                'price': 100.00,
                'calendly_event_type': 'career-mentoring',
                'order': 2
            },
            {
                'name': 'Code Review Session',
                'description': 'Detailed code review and feedback session. I\'ll review your code, provide suggestions for improvement, and discuss best practices.',
                'duration': 30,
                'price': 75.00,
                'calendly_event_type': 'code-review',
                'order': 3
            },
            {
                'name': 'Quick Q&A',
                'description': 'Short session for quick questions about programming, technology choices, or getting unstuck on a specific problem.',
                'duration': 15,
                'price': 0.00,  # Free
                'calendly_event_type': 'quick-qa',
                'order': 4
            },
            {
                'name': 'System Design Interview Prep',
                'description': 'Practice system design interviews with real-world scenarios. Get feedback on your approach and learn industry best practices.',
                'duration': 90,
                'price': 200.00,
                'calendly_event_type': 'system-design-prep',
                'order': 5
            }
        ]

        for apt_data in appointment_types_data:
            appointment_type, created = AppointmentType.objects.get_or_create(
                name=apt_data['name'],
                defaults=apt_data
            )
            if created:
                self.stdout.write(f'Appointment type "{appointment_type.name}" created')

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))