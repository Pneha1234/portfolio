from django.contrib import admin
from django.utils.html import format_html
from django import forms
from .models import (Profile, Project, Book, Paper, BlogPost, ContactMessage, 
                     SiteSettings, StudyNote, StudyChapter, AppointmentType, Appointment, Skill)


class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        }


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency_level', 'years_experience', 'is_featured', 'order']
    list_filter = ['category', 'proficiency_level', 'is_featured']
    search_fields = ['name']
    list_editable = ['is_featured', 'order', 'proficiency_level']
    ordering = ['category', 'order', 'name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'icon_class', 'proficiency_level', 'years_experience')
        }),
        ('Display Options', {
            'fields': ('is_featured', 'order')
        }),
    )
    
    def get_proficiency_display_text(self, obj):
        return obj.get_proficiency_display_text()
    get_proficiency_display_text.short_description = 'Proficiency'


@admin.register(AppointmentType)
class AppointmentTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'get_price_display', 'is_active', 'order']
    list_filter = ['is_active', 'duration']
    search_fields = ['name', 'description']
    list_editable = ['is_active', 'order']
    ordering = ['order', 'name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'duration', 'price')
        }),
        ('Calendly Integration', {
            'fields': ('calendly_event_type',),
            'description': 'Optional: Calendly event type URL slug for direct integration'
        }),
        ('Display Options', {
            'fields': ('is_active', 'order')
        }),
    )
    
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'description':
            kwargs['widget'] = forms.Textarea(attrs={'rows': 4, 'cols': 80})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'appointment_type', 'client_email', 'status', 'scheduled_date', 'created_at']
    list_filter = ['status', 'appointment_type', 'created_at']
    search_fields = ['client_name', 'client_email', 'company', 'purpose']
    list_editable = ['status']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Client Information', {
            'fields': ('client_name', 'client_email', 'client_phone', 'company')
        }),
        ('Appointment Details', {
            'fields': ('appointment_type', 'purpose', 'preferred_date', 'scheduled_date')
        }),
        ('Status & Integration', {
            'fields': ('status', 'calendly_event_id', 'google_meet_link')
        }),
        ('Internal Notes', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in ['purpose', 'notes']:
            kwargs['widget'] = forms.Textarea(attrs={'rows': 4, 'cols': 80})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ['name', 'title', 'email', 'updated_at']
    fields = ['name', 'title', 'bio', 'profile_image', 'email', 'phone', 
              'github_url', 'linkedin_url', 'medium_url', 'newsletter_url', 'newsletter_title', 'newsletter_description', 'resume_url', 'calendly_url']
    
    def has_add_permission(self, request):
        # Only allow one profile instance
        return not Profile.objects.exists()


class StudyChapterInline(admin.TabularInline):
    model = StudyChapter
    extra = 1
    fields = ['chapter_number', 'title', 'status', 'notes_url', 'code_examples_url', 'order']
    ordering = ['order', 'chapter_number']


@admin.register(StudyNote)
class StudyNoteAdmin(admin.ModelAdmin):
    list_display = ['book_title', 'book_author', 'completed_chapters', 'total_chapters', 'get_progress', 'featured']
    list_filter = ['featured', 'created_at']
    search_fields = ['book_title', 'book_author']
    list_editable = ['featured']
    inlines = [StudyChapterInline]
    
    fieldsets = (
        ('Book Information', {
            'fields': ('book_title', 'book_author', 'book_description', 'book_cover_url')
        }),
        ('Progress Tracking', {
            'fields': ('total_chapters', 'completed_chapters')
        }),
        ('Display Options', {
            'fields': ('featured',)
        }),
    )
    
    def get_progress(self, obj):
        progress = obj.get_progress_percentage()
        color = '#28a745' if progress > 70 else '#ffc107' if progress > 30 else '#dc3545'
        return format_html(
            '<div style="width: 100px; background: #e9ecef; border-radius: 10px; height: 20px;">'
            '<div style="width: {}%; background: {}; height: 100%; border-radius: 10px; text-align: center; color: white; font-size: 12px; line-height: 20px;">'
            '{}%</div></div>',
            progress, color, progress
        )
    get_progress.short_description = 'Progress'


@admin.register(StudyChapter)
class StudyChapterAdmin(admin.ModelAdmin):
    list_display = ['study_note', 'chapter_number', 'title', 'status', 'order']
    list_filter = ['status', 'study_note']
    search_fields = ['title', 'study_note__book_title']
    list_editable = ['status', 'order']
    ordering = ['study_note', 'order', 'chapter_number']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order', 'created_at']
    list_filter = ['featured', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['featured', 'order']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'image')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Details', {
            'fields': ('technologies', 'featured', 'order')
        }),
    )
    
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'description':
            kwargs['widget'] = forms.Textarea(attrs={'rows': 6, 'cols': 80})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'rating', 'featured', 'order']
    list_filter = ['category', 'rating', 'featured', 'created_at']
    search_fields = ['title', 'author', 'review']
    list_editable = ['featured', 'order', 'rating']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'category', 'cover_image')
        }),
        ('Links & Review', {
            'fields': ('goodreads_url', 'notes_url', 'rating', 'review')
        }),
        ('Display Options', {
            'fields': ('featured', 'order')
        }),
    )
    
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'review':
            kwargs['widget'] = forms.Textarea(attrs={'rows': 6, 'cols': 80})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'order', 'created_at']
    list_filter = ['category', 'featured', 'created_at']
    search_fields = ['title', 'authors', 'summary']
    list_editable = ['featured', 'order']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Paper Information', {
            'fields': ('title', 'authors', 'category')
        }),
        ('Links & Content', {
            'fields': ('paper_url', 'notes_url', 'summary', 'key_insights')
        }),
        ('Display Options', {
            'fields': ('featured', 'order')
        }),
    )
    
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in ['summary', 'key_insights']:
            kwargs['widget'] = forms.Textarea(attrs={'rows': 6, 'cols': 80})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'featured', 'order']
    list_filter = ['featured', 'published_date', 'created_at']
    search_fields = ['title', 'description', 'tags']
    list_editable = ['featured', 'order']
    ordering = ['order', '-published_date']
    date_hierarchy = 'published_date'
    
    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'description', 'image', 'published_date')
        }),
        ('Links & Tags', {
            'fields': ('medium_url', 'tags')
        }),
        ('Display Options', {
            'fields': ('featured', 'order')
        }),
    )
    
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'description':
            kwargs['widget'] = forms.Textarea(attrs={'rows': 6, 'cols': 80})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'sender_email', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['subject', 'sender_email', 'message']
    list_editable = ['is_read']
    readonly_fields = ['sender_email', 'subject', 'message', 'created_at']
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        return False  # Prevent manual addition of contact messages


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_title', 'updated_at']
    fields = ['site_title', 'meta_description', 'google_analytics_id', 'footer_text', 'google_calendar_id']
    
    def has_add_permission(self, request):
        # Only allow one site settings instance
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


# Customize admin site header and title
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"