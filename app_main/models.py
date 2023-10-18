from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


class Teacher(models.Model):
    name = models.CharField(max_length=122, null=True)
    post = models.CharField(max_length=120, null=True)
    educational_qualification = models.CharField(max_length=255, null=True)
    teacher_picture = models.ImageField(
        upload_to="teacher_picture", null=True, blank=True
    )

    def __str__(self):
        return f"Name: {self.name}"


class Notice(models.Model):
    title = models.CharField(null=True, max_length=150)
    content = RichTextUploadingField(null=True)
    thumbnail = models.ImageField(upload_to="notice-thumbnail-images", null=True, blank=True, help_text="image size: w-350px x h-400")

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notice: {self.title}"


class Contact(models.Model):
    name = models.CharField(max_length=122, null=True)
    email = models.CharField(max_length=122, null=True)
    phone = models.CharField(max_length=12, null=True)
    address = models.CharField(max_length=12, null=True, blank=True)
    desc = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.email}"



class ContactInformationModel(models.Model):
    details = models.TextField(
        null=True, blank=True, max_length=325, verbose_name="Short Summary"
    )
    phone = models.CharField(max_length=122, null=True)
    email = models.CharField(max_length=122, null=True)
    address = models.TextField(null=True, blank=True, max_length=325)
    work = models.CharField(
        null=True, blank=True, max_length=225, verbose_name="Working Date & Time"
    )

    def __str__(self):
        return f"{self.id} - Contact Info"

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Informations"
        ordering = ["-id"]


# Define Footer Information Model
class FooterInformationModel(models.Model):
    logo = models.ImageField(
        upload_to="footer_logo",
        null=True,
        verbose_name="Footer logo",
        help_text="image size: w-250px x h-120",
    )
    details = models.TextField(null=True, max_length=500, verbose_name="Short Summary")
    facebook_link = models.URLField(null=True, blank=True, verbose_name="Facebook Link")
    twitter_link = models.URLField(null=True, blank=True, verbose_name="Twitter Link")
    instagram_link = models.URLField(
        null=True, blank=True, verbose_name="Instagram Link"
    )
    youtube_link = models.URLField(null=True, blank=True, verbose_name="YouTube Link")

    def __str__(self):
        return f"{self.id} - Footer Info"

    class Meta:
        verbose_name = "Footer Information"
        verbose_name_plural = "Footer Informations"
        ordering = ["-id"]


# ----------- new addition 2.0 ----------

class HeaderSliderModel(models.Model):
    title = models.CharField(null=True, blank=True, max_length=125)
    sub_title = models.TextField(null=True, blank=True, max_length=225)
    btn_text = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="button text"
    )
    btn_link = models.URLField(null=True, blank=True, verbose_name="button link")
    bg_img = models.ImageField(
        upload_to="header-sliders-bg",
        null=True,
        verbose_name="slider image",
        help_text="image size: w-1920px x h-800",
    )
    active = models.BooleanField(default=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.created_at}"

    class Meta:
        verbose_name = "Header Slider"
        verbose_name_plural = "Header Sliders"



class AdmissionModel(models.Model):
    admission_banner = models.ImageField(upload_to="admission-banner", null=True)
    admission_details = RichTextUploadingField(null=True)

    def __str__(self):
        return f"{self.id} - Admission"

    class Meta:
        verbose_name = "Admission"
        verbose_name_plural = "Admissions"


class CounterModel(models.Model):
    total_student = models.CharField(max_length=255, null=True, verbose_name="total students")
    total_teacher = models.CharField(max_length=255, null=True, verbose_name="total teachers")
    total_book = models.CharField(max_length=255, null=True, verbose_name="total books")
    total_computer = models.CharField(max_length=255, null=True, verbose_name="total computers")

    def __str__(self):
        return f"Counter Data | Editable Object"


class FounderModel(models.Model):
    profile = models.ImageField(upload_to="founder-profile-image", null=True, verbose_name="profile image")
    founder_details = RichTextUploadingField(null=True)

    def __str__(self):
        return f"{self.id} - Founder | Editable Object"

    class Meta:
        verbose_name = "Founder"
        verbose_name_plural = "Founder Details"


class FacilityModel(models.Model):
    title = models.CharField(null=True, max_length=125)
    details = models.TextField(null=True, max_length=525, verbose_name="short details")
    is_important = models.BooleanField(default=False, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - Facility"

    class Meta:
        verbose_name = "Student Facility"
        verbose_name_plural = "Student Facilities"



class StudentActivitiesModel(models.Model):
    title = models.CharField(null=True, max_length=125, verbose_name="card title")
    details = RichTextUploadingField(null=True)
    btn_link = models.URLField(null=True, blank=True, verbose_name="button link")
    image = models.ImageField(upload_to="activities-images", null=True)

    is_active = models.BooleanField(default=True, null=True)
    status = models.CharField(null=True, max_length=125, default="Editable Data", editable=False)

    def __str__(self):
        return f"{self.id} - Activities"

    class Meta:
        verbose_name = "Student Activities"
        verbose_name_plural = "Student Activities"


class CourseModel(models.Model):
    course_name = models.CharField(null=True, max_length=125, verbose_name="course name")
    slug = models.SlugField(null=True, blank=True, editable=False)
    code_name = models.CharField(null=True, max_length=125, verbose_name="course code name")
    course_article = models.TextField(null=True, max_length=500, verbose_name="course article")
    cover_image = models.ImageField(upload_to="course-cover-images", null=True, verbose_name="course cover image", help_text="image size: w-800, h-500")
    course_glance = RichTextUploadingField(null=True)
    total_student_seat = models.CharField(null=True, max_length=125)
    total_student = models.CharField(null=True, max_length=125)
    total_graduated = models.CharField(null=True, max_length=125)
    total_credit = models.CharField(null=True, blank=True, max_length=125, help_text="it's mandatory for hon's courses")
    per_semester_fee = models.CharField(null=True, blank=True, max_length=125, help_text="it's mandatory for hon's courses")
    total_tuition_fee = models.CharField(null=True, blank=True, max_length=125, help_text="it's mandatory for hon's courses")


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.course_name)
        super(CourseModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.course_name}"

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
