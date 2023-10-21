from django.shortcuts import get_object_or_404
from app_main.models import (
    ContactInformationModel,
    FooterInformationModel,
    CourseModel
)


def miscellaneous_common_data(request):
    main_campus = get_object_or_404(ContactInformationModel, contact_info_type = "Main Campus")
    dhaka_office = get_object_or_404(ContactInformationModel, contact_info_type = "Dhaka Office")
    footer = FooterInformationModel.objects.all().last()
    courses = CourseModel.objects.all()

    context = {
        "main_campus": main_campus,
        "dhaka_office": dhaka_office,
        "footer": footer,
        "courses": courses,
    }
    return context
