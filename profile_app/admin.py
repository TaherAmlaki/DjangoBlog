from django.contrib import admin
from .models import (ProfileSection, AboutMe, ExperiencesModel, EducationModel,
                     CertificatesModel, SkillsModel, MotivationModel)


admin.site.register(ProfileSection)
admin.site.register(AboutMe)
admin.site.register(ExperiencesModel)
admin.site.register(EducationModel)
admin.site.register(CertificatesModel)
admin.site.register(SkillsModel)
admin.site.register(MotivationModel)
