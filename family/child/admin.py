from django.contrib import admin
from child.models import  Branch, Semester,Subject,Course
# Register your models here.
admin.site.register(Branch)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Course)