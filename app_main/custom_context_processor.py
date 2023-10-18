from app_main.models import (
    ContactInformationModel,
    FooterInformationModel,
    CourseModel
)


def miscellaneous_common_data(request):
    contact = ContactInformationModel.objects.all().last()
    footer = FooterInformationModel.objects.all().last()
    courses = CourseModel.objects.all()

    context = {
        "contact": contact,
        "footer": footer,
        "courses": courses,
    }
    return context
