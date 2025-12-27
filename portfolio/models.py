from django.db import models
from django.urls import reverse
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, default="Neha Pandey")
    title = models.CharField(max_length=200, default="Senior Software Engineer")
    bio = models.TextField(help_text="This is your 'About Me' section content")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    medium_url = models.URLField(blank=True)
    newsletter_url = models.URLField(blank=True, help_text="LinkedIn newsletter or other newsletter URL")
    newsletter_title = models.CharField(max_length=200, blank=True, help_text="Newsletter title (e.g., 'Tech Insights Weekly')")
    newsletter_description = models.TextField(blank=True, help_text="Brief description of your newsletter content")
    resume_url = models.URLField(blank=True)
    # Calendly integration
    calendly_url = models.URLField(blank=True, help_text="Your Calendly scheduling link")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Technical skills to display in the About section"""
    CATEGORY_CHOICES = [
        ('languages', 'Programming Languages'),
        ('frameworks', 'Frameworks & Libraries'),
        ('databases', 'Databases'),
        ('cloud_devops', 'Cloud & DevOps'),
        ('tools', 'Tools & Technologies'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100, help_text="e.g., 'Python', 'Django', 'AWS'")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='languages')
    icon_class = models.CharField(max_length=100, blank=True, help_text="DevIcon class (e.g., 'devicon-python-plain', 'devicon-django-plain')")
    proficiency_level = models.IntegerField(
        choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Expert')],
        default=3,
        help_text="Your skill level (1-4)"
    )
    years_experience = models.IntegerField(blank=True, null=True, help_text="Years of experience (optional)")
    is_featured = models.BooleanField(default=True, help_text="Show on homepage")
    order = models.IntegerField(default=0, help_text="Display order within category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'order', 'name']
        unique_together = ['name', 'category']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

    def get_proficiency_display_text(self):
        levels = {1: 'Beginner', 2: 'Intermediate', 3: 'Advanced', 4: 'Expert'}
        return levels.get(self.proficiency_level, 'Unknown')


class AppointmentType(models.Model):
    """Different types of appointments available"""
    DURATION_CHOICES = [
        (15, '15 minutes'),
        (30, '30 minutes'),
        (45, '45 minutes'),
        (60, '1 hour'),
        (90, '1.5 hours'),
        (120, '2 hours'),
    ]

    name = models.CharField(max_length=100, help_text="e.g., 'Technical Consultation', 'Career Advice'")
    description = models.TextField(help_text="What this appointment is for")
    duration = models.IntegerField(choices=DURATION_CHOICES, default=30)
    calendly_event_type = models.CharField(max_length=200, blank=True, help_text="Calendly event type URL slug")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Price in USD (0 for free)")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.duration} min)"

    def get_price_display(self):
        if self.price == 0:
            return "Free"
        return f"${self.price}"


class Appointment(models.Model):
    """Track appointments booked through the system"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    ]

    appointment_type = models.ForeignKey(AppointmentType, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    purpose = models.TextField(help_text="What would you like to discuss?")
    preferred_date = models.DateTimeField(blank=True, null=True)
    scheduled_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    calendly_event_id = models.CharField(max_length=200, blank=True)
    google_meet_link = models.URLField(blank=True)
    notes = models.TextField(blank=True, help_text="Internal notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_name} - {self.appointment_type.name}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.URLField()
    live_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]


class Book(models.Model):
    CATEGORY_CHOICES = [
        ('technical', 'Technical'),
        ('business', 'Business'),
        ('personal_development', 'Personal Development'),
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='technical')
    goodreads_url = models.URLField()
    notes_url = models.URLField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='books/', blank=True, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, null=True)
    review = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.title} by {self.author}"


class StudyNote(models.Model):
    """Model for managing study notes like CPython Internals"""
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('planned', 'Planned'),
    ]

    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    book_description = models.TextField(blank=True)
    book_cover_url = models.URLField(blank=True, help_text="URL to book cover image")
    total_chapters = models.IntegerField(default=0)
    completed_chapters = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', '-updated_at']

    def __str__(self):
        return f"{self.book_title} - Study Notes"

    def get_progress_percentage(self):
        if self.total_chapters == 0:
            return 0
        return int((self.completed_chapters / self.total_chapters) * 100)


class StudyChapter(models.Model):
    """Individual chapters for study notes"""
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('planned', 'Planned'),
    ]

    study_note = models.ForeignKey(StudyNote, on_delete=models.CASCADE, related_name='chapters')
    chapter_number = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
    notes_url = models.URLField(blank=True, help_text="Link to detailed notes")
    code_examples_url = models.URLField(blank=True, help_text="Link to code examples")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['study_note', 'order', 'chapter_number']
        unique_together = ['study_note', 'chapter_number']

    def __str__(self):
        return f"Chapter {self.chapter_number}: {self.title}"


class Paper(models.Model):
    CATEGORY_CHOICES = [
        ('databases', 'Databases & Storage Systems'),
        ('systems', 'Systems & Performance'),
        ('ai', 'AI & Machine Learning'),
        ('distributed', 'Distributed Systems'),
        ('security', 'Security'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=500)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    paper_url = models.URLField()
    notes_url = models.URLField(blank=True, null=True)
    summary = models.TextField(blank=True)
    key_insights = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    medium_url = models.URLField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    tags = models.CharField(max_length=300, help_text="Comma-separated list of tags")
    featured = models.BooleanField(default=False)
    published_date = models.DateField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-published_date']

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]


class ContactMessage(models.Model):
    sender_email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.subject} - {self.sender_email}"


class SiteSettings(models.Model):
    site_title = models.CharField(max_length=100, default="Neha Pandey | Portfolio")
    meta_description = models.TextField(default="Senior Software Engineer with 5+ years of experience")
    google_analytics_id = models.CharField(max_length=50, blank=True)
    footer_text = models.CharField(max_length=200, default="All rights reserved.")
    # Google Calendar integration
    google_calendar_id = models.CharField(max_length=200, blank=True, help_text="Your Google Calendar ID for appointments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"