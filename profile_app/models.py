from django.db import models


class ProfileSection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    route_to = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.title}, {self.order}, {self.route_to}"


class AboutMe(models.Model):
    my_job_title = models.CharField(max_length=100, default="Python Developer")
    short_version = models.TextField(default="Default About Me, short")

    def __str__(self):
        return f"{self.my_job_title}"


class ExperiencesModel(models.Model):
    title = models.TextField()
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(default=None, null=True, blank=True)
    company_icon = models.ImageField(default="default_company.jpg", upload_to="users_pics")
    tasks = models.TextField()
    link_to_company = models.URLField()

    def __str__(self):
        return f"{self.title}@{self.company}"


class EducationModel(models.Model):
    title = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    thesis_title = models.CharField(max_length=100)
    thesis_description = models.TextField()
    university_link = models.URLField()
    university_icon = models.ImageField(default="default_university.jpg", upload_to="user_pics")

    def __str__(self):
        return f"{self.title}@{self.university}"


class CertificatesModel(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    end_date = models.DateField()
    duration = models.CharField(max_length=20)
    certificate_authority = models.CharField(max_length=30)
    certificate_link = models.URLField()
    ca_icon = models.ImageField(default="Udemy.png", upload_to="user_pics")

    def __str__(self):
        return f"{self.title}@{self.certificate_authority}"


class SkillsModel(models.Model):
    title = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    experiences = models.TextField()
    level = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['-level']

    def __str__(self):
        return f"{self.title}@{self.area}-{self.level}"


class ProjectsModel(models.Model):
    title = models.TextField()
    order = models.IntegerField()
    description = models.TextField()
    github_link = models.URLField()

    def __str__(self):
        return self.title
