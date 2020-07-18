from django.contrib import admin
from app.models import Department, Applicant, Vacancy, Resume
# Register your models here.

admin.site.register(Department)
admin.site.register(Applicant)
admin.site.register(Vacancy)
admin.site.register(Resume)