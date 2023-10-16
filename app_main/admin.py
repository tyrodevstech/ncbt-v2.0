from django.contrib import admin
from .models import *


admin.site.register(Teacher)
admin.site.register(Contact)
admin.site.register(Notice)
admin.site.register(FooterInformationModel)
admin.site.register(ContactInformationModel)
admin.site.register(NoticeImages)


class AdmissionModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(AdmissionModel, AdmissionModelAdmin)
