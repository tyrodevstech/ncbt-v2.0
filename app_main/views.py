from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .form import *
from .models import *

# Create your views here.


def index_view(request):
    context = {
        "notice": Notice.objects.all().order_by("-date")[:4],
        "sliders": HeaderSliderModel.objects.all(),
        "courses":  CourseModel.objects.all(),
        "counter": CounterModel.objects.first(),
        "founder": FounderModel.objects.first(),
        "important_facilities": FacilityModel.objects.filter(is_important=True)[:3],
        "facilities": FacilityModel.objects.filter(is_important=False),
        "activities": StudentActivitiesModel.objects.filter(is_active=True),
        "authorities": AdministrationModel.objects.filter(show_on_home=True,active=True),
    }
    return render(request, "app_main/index.html", context)


def about_us_view(request):
    context = {
        'history': HistoryModel.objects.first(),
        'about_info': AboutInformationModel.objects.all(),
        'conducts': CodeOfConduct.objects.all(),
    }
    return render(request, "app_main/about_us.html", context)


def course_view(request):
    return render(request, "app_main/course.html")


def admission_view(request):
    context = {
        "admission": AdmissionModel.objects.first(),
    }
    return render(request, "app_main/admission.html", context)


def administration_view(request, type):
    administration_qs =AdministrationModel.objects.filter(type=type,active=True)
    administration_paginator = Paginator(administration_qs, 12)
    page = request.GET.get("page")

    try:
        administration = administration_paginator.page(page)
    except PageNotAnInteger:
        administration = administration_paginator.page(1)
    except EmptyPage:
        administration = administration_paginator.page(administration_paginator.num_pages)

    context = {
        "administration": administration,
        }
    return render(request, "app_main/administration.html", context)


def notices_view(request):
    notice_queryset = Notice.objects.all().order_by("-date")
    notice_paginator = Paginator(notice_queryset, 6)
    page = request.GET.get("page")

    try:
        notices = notice_paginator.page(page)
    except PageNotAnInteger:
        notices = notice_paginator.page(1)
    except EmptyPage:
        notices = notice_paginator.page(notice_paginator.num_pages)

    context = {
        "notices": notices,
    }
    return render(request, "app_main/notices.html", context)


def notice_details_view(request, pk):
    context = {"notice": get_object_or_404(Notice, id=pk)}
    return render(request, "app_main/notice_details.html", context)


def course_details_view(request, slug):
    context = {
        "course": get_object_or_404(CourseModel, slug=slug)
    }
    return render(request, "app_main/course_details.html", context)


def founder_view(request):
    context = {
        "founder": FounderModel.objects.first(),
    }
    return render(request, "app_main/founder.html", context)


def contact_us_view(request):
    info = ContactInformationModel.objects.first()
    form = ContactForm()
    email = request.GET.get("email", "")
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contactus")

    context = {
        "form": form,
        "info": info,
        "email": email,
    }
    return render(request, "app_main/contact_us.html", context)


def custom_page_not_found_view(request, exception=None):
    return render(request, "404.html", {})
