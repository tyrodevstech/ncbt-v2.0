from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import *
from .models import *

# Create your views here.

def index_view(request):
    notice = Notice.objects.all().order_by('-date')[:4]
    context = {
        'notice': notice
    }
    return render(request,'app_main/index.html', context)

def about_us_view(request):
    return render(request,'app_main/about_us.html')

def course_view(request):
    return render(request,'app_main/course.html')

def admission_view(request):
    context = {
        'admission': AdmissionModel.objects.first(),
    }
    return render(request,'app_main/admission.html', context)

def teachers_view(request):
    teachers_obj = Teacher.objects.all()
    context = {
        'teachers_obj': teachers_obj
    }
    return render(request,'app_main/teachers.html', context)

def notice_view(request):
    notice_obj = Notice.objects.all().order_by('-date')
    all_post = Paginator(notice_obj, 6)
    page = request.GET.get('page')
    notice_imagesObj = NoticeImages.objects.all().order_by('-id')
    try:
        notice = all_post.page(page)
    except PageNotAnInteger:
        notice = all_post.page(1)
    except:
        notice = all_post.page(all_post.num_pages)

    context = {
        'notice': notice,
        'notice_imagesObj':notice_imagesObj,
    }
    return render(request,'app_main/notice.html', context)

def contact_us_view(request):
    info = ContactInformationModel.objects.first()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contactus')


    context = {
        'form' : form,
        'info' : info,
    }
    return render(request,'app_main/contact_us.html', context)



def custom_page_not_found_view(request, exception=None):
    return render(request, "404.html", {})