from django.contrib import admin
from .models import *


admin.site.register(Teacher)
admin.site.register(Contact)
admin.site.register(Notice)
admin.site.register(FooterInformationModel)
admin.site.register(RoutineModel)
admin.site.register(ContactInformationModel)


# ----------- new addition 2.0 ----------

class AdmissionModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(AdmissionModel, AdmissionModelAdmin)


class HeaderSliderAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "active")

admin.site.register(HeaderSliderModel, HeaderSliderAdmin)


class CounterModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(CounterModel, CounterModelAdmin)


class FounderModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(FounderModel, FounderModelAdmin)


class FacilityModelAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_important")

admin.site.register(FacilityModel, FacilityModelAdmin)


class StudentActivitiesModelAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "is_active")
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 2:
            return False
        else:
            return True

admin.site.register(StudentActivitiesModel, StudentActivitiesModelAdmin)


class CourseModelAdmin(admin.ModelAdmin):
    list_display = ("course_name", "code_name", "total_student", "total_student_seat")

admin.site.register(CourseModel, CourseModelAdmin)
