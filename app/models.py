from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=False)
    department = models.ForeignKey(Department, related_name='vacancies', on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now=False, auto_now_add=False)
    updated_at = models.TimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Applicant(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255,blank=False, null=False)
    phone1 = models.CharField(max_length=255,blank=False, null=False)
    phone2 = models.CharField(max_length=255,blank=True, null=True, default=None)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return str(self.id)


class Resume(models.Model):
    pdf = models.FileField(upload_to='media/resumes/%Y/%m/%d/')
    applicant = models.ForeignKey(Applicant, related_name='resumes', on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, related_name='resumes', on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.id)