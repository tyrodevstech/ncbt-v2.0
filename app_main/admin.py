from django.contrib import admin
from .models import *


admin.site.register(Contact)

class FooterInformationModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(FooterInformationModel, FooterInformationModelAdmin)


class NoticeAdmin(admin.ModelAdmin):
    list_display = ("title", "date",)

admin.site.register(Notice, NoticeAdmin)


class RoutineModelInlineAdmin(admin.TabularInline):
    model = RoutineModel
    extra = 1


class AdministrationModelAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "designation", "joining_date")

admin.site.register(AdministrationModel, AdministrationModelAdmin)


class ContactInformationModelAdmin(admin.ModelAdmin):
    list_display = ("contact_info_type", "phone", "email", "work")

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 2:
            return False
        else:
            return True

admin.site.register(ContactInformationModel, ContactInformationModelAdmin)


class RoutineModelAdmin(admin.ModelAdmin):
    list_display = ("course", "title", "semester", "year", "created_at")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "course":
            kwargs["queryset"] = CourseModel.objects.all()  # Replace YourAuthorModel with your actual Author model
            kwargs["empty_label"] = "Select a course"  # Customize the empty label
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(RoutineModel, RoutineModelAdmin)



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

    inlines = [RoutineModelInlineAdmin]


admin.site.register(CourseModel, CourseModelAdmin)


class HistoryModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(HistoryModel, HistoryModelAdmin)


class AboutInformationModelAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_title", "sub_title")

admin.site.register(AboutInformationModel, AboutInformationModelAdmin)

admin.site.register(CodeOfConduct)