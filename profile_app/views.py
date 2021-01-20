from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import View
from django.http import FileResponse, Http404
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import get_template
from .models import (ProfileSection, AboutMe, ExperiencesModel,
                     EducationModel, CertificatesModel, SkillsModel, ProjectsModel)
from .MyForms import ContactForm
from .PdfRenderer import render_to_pdf


def home(request):
    sections = ProfileSection.objects.order_by("order")
    about_me_ = AboutMe.objects.first()
    context_ = {'sections': sections, "about_me": about_me_}
    return render(request, 'profile_app/home.html', context=context_)


class ExperimentsListView(ListView):
    template_name = 'profile_app/experiences.html'
    model = ExperiencesModel
    context_object_name = "experiences"
    ordering = ['-start_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ind = 0
        for experience in context.get(self.context_object_name):
            tasks = experience.tasks.split(";")
            context[self.context_object_name][ind].tasks = tasks
            ind += 1
        return context


class EducationListView(ListView):
    template_name = 'profile_app/educations.html'
    model = EducationModel
    context_object_name = "educations"
    ordering = ['-start_date']


class CertificationListView(ListView):
    template_name = 'profile_app/certifications.html'
    model = CertificatesModel
    context_object_name = "certificates"
    ordering = ['-end_date']


class SkillsListView(ListView):
    template_name = 'profile_app/skills.html'
    model = SkillsModel
    context_object_name = "skills"
    ordering = ['-level']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["progressbar_width"] = []
        ind = 0
        for skill in context.get(self.context_object_name):
            context[self.context_object_name][ind].level = skill.level * 10
            experiences = skill.experiences.split(";")
            context[self.context_object_name][ind].experiences = experiences
            ind += 1
        return context


class ResumeView(ListView):
    template_name = 'profile_app/resume.html'
    context_object_name = "resume"
    queryset = ExperiencesModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experiences'] = ExperiencesModel.objects.all().order_by('-start_date')
        context['skills'] = SkillsModel.objects.order_by('level').reverse()
        context['educations'] = EducationModel.objects.all()
        context['about_me'] = AboutMe.objects.first()
        context['projects'] = ProjectsModel.objects.all().order_by("-order")

        ind = 0
        for experience in context.get('experiences'):
            tasks = experience.tasks.split(";")
            context['experiences'][ind].tasks = tasks
            ind += 1

        context["progressbar_width"] = []
        ind = 0
        for skill in context.get("skills"):
            context["skills"][ind].level = skill.level * 10
            experiences = skill.experiences.split(";")
            context["skills"][ind].experiences = experiences
            ind += 1
        
        context["ResumeSkills"] = {"Programming": [],
                                   "WebFrameworks": [],
                                   "DevOps": [],
                                   "Other": []}
        for skill in context.get("skills"):
            if skill.area == "Programming":
                context["ResumeSkills"]["Programming"].append(skill)
            elif skill.area == "Web Frameworks":
                context["ResumeSkills"]["WebFrameworks"].append(skill)
            elif skill.area == "DevOps":
                context["ResumeSkills"]["DevOps"].append(skill)
            else:
                context["ResumeSkills"]["Other"].append(skill)

        return context


class ResumePdfView(ListView):
    template_name = 'profile_app/resume-pdf-plain.html'
    context_object_name = "resume"
    queryset = ExperiencesModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experiences'] = ExperiencesModel.objects.all().order_by("-start_date")
        context['skills'] = SkillsModel.objects.order_by('level').reverse()
        context['educations'] = EducationModel.objects.all()
        context['about_me'] = AboutMe.objects.first()
        context['projects'] = ProjectsModel.objects.all().order_by("-order")

        ind = 0
        for experience in context.get('experiences'):
            tasks = experience.tasks.split(";")
            context['experiences'][ind].tasks = tasks
            ind += 1

        context["progressbar_width"] = []
        ind = 0
        for skill in context.get("skills"):
            context["skills"][ind].level = skill.level * 10
            experiences = skill.experiences.split(";")
            context["skills"][ind].experiences = experiences
            ind += 1

        context["ResumeSkills"] = {"Programming": [],
                                   "WebFrameworks": [],
                                   "DevOps": [],
                                   "Other": []}
        for skill in context.get("skills"):
            if skill.area == "Programming":
                context["ResumeSkills"]["Programming"].append(skill)
            elif skill.area == "Web Frameworks":
                context["ResumeSkills"]["WebFrameworks"].append(skill)
            elif skill.area == "DevOps":
                context["ResumeSkills"]["DevOps"].append(skill)
            else:
                context["ResumeSkills"]["Other"].append(skill)
        
        return context


def resume_pdf_view(request):
    try:
        return FileResponse(open("profile_app/static/profile_app/TaherAmlaki-Resume.pdf", "rb"), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()


def contact_me(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_email = form.cleaned_data['contact_email']
            contact_name = form.cleaned_data['contact_name']
            subject = f"Blog=> {form.cleaned_data['subject']}"
            message = form.cleaned_data['message']
            try:
                message = f"name={contact_name}\n" \
                          f"Email={contact_email}\n" \
                          f"subject={subject}\n" \
                          f"message={message}"
                send_mail(subject=subject, message=message, from_email='taheramlakiblog@gmail.com', recipient_list=['taheramlakiblog@gmail.com'])
                messages.success(request, f"Thank you {contact_name}, your message was sent successfully")
                return redirect('blog-home')
            except BadHeaderError:
                messages.error(request, f"Sorry, Could not send the message. Maybe the form is not valid")
    return render(request, 'profile_app/contact_me.html', {'form': form})

