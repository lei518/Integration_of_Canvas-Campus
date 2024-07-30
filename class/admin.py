from django.contrib import admin
from .models import Course, Student, Enrollment, Assignment, Submission
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # You can customize the admin interface here
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Assignment)
admin.site.register(Submission)
# Register your models here.
