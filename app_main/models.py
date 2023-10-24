from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.utils import timezone

# ----------- new addition 2.0 ----------

class AdministrationModel(models.Model):
    CATEGORY = (
        ("", "Select Administration Type"),
        ("Authorities", "Authorities"),
        ("Teachers", "Teachers"),
        ("Staffs", "Staffs"),
    )
    type = models.CharField(choices=CATEGORY, max_length=50, null=True)
    name = models.CharField(max_length=122, null=True)
    designation = models.CharField(max_length=120, null=True)
    education = models.CharField(max_length=255, null=True, verbose_name="last educational qualification")
    image = models.ImageField(
        upload_to="administration-profile-images", null=True, blank=True, verbose_name="profile picture"
    )

    active = models.BooleanField(default=True, null=True)
    show_on_home = models.BooleanField(default=False, null=True,verbose_name='Show on Homepage')
    joining_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Name: {self.name}"

    class Meta:
        verbose_name = "Administration"
        verbose_name_plural = "Administrations"

        ordering = [
            "joining_date",
            "id"
        ]


class Notice(models.Model):
    title = models.CharField(null=True, max_length=150)
    content = RichTextUploadingField(null=True)
    thumbnail = models.ImageField(
        upload_to="notice-thumbnail-images",
        null=True,
        blank=True,
        help_text="image size: w-350px x h-400",
    )

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

    class Meta:
        verbose_name = "Query Contact"
        verbose_name_plural = "Query Contacts"


class ContactInformationModel(models.Model):
    TYPE = (
        ("", "Select Type"),
        ("Main Campus", "Main Campus"),
        ("Dhaka Office", "Dhaka Office"),
    )
    contact_info_type = models.CharField(max_length=125, null=True, choices=TYPE)
    details = models.TextField(
        null=True,
        max_length=325,
        blank=True,
        verbose_name="contact short summary",
        help_text="Please provide information regarding the primary objective at the main campus.",
    )
    phone = models.CharField(max_length=125, null=True)
    email = models.CharField(max_length=125, null=True)
    address = models.TextField(null=True, max_length=525)
    work = models.CharField(
        null=True, max_length=225, verbose_name="working date & time"
    )

    def __str__(self):
        return f"{self.id} - {self.contact_info_type}"

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Informations"


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
    total_student = models.CharField(
        max_length=255, null=True, verbose_name="total students"
    )
    total_teacher = models.CharField(
        max_length=255, null=True, verbose_name="total teachers"
    )
    total_book = models.CharField(max_length=255, null=True, verbose_name="total books")
    total_computer = models.CharField(
        max_length=255, null=True, verbose_name="total computers"
    )

    def __str__(self):
        return f"Counter Data | Editable Object"


class FounderModel(models.Model):
    name = models.CharField(null=True, max_length=125, verbose_name="founder name")
    profile = models.ImageField(
        upload_to="founder-profile-image", null=True, verbose_name="profile image"
    )
    founder_details = RichTextUploadingField(null=True)

    def __str__(self):
        return f"{self.id} - {self.name} Founder | Editable Object"

    class Meta:
        verbose_name = "Founder"
        verbose_name_plural = "Founder Info"


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
    status = models.CharField(
        null=True, max_length=125, default="Editable Data", editable=False
    )

    def __str__(self):
        return f"{self.id} - Activities"

    class Meta:
        verbose_name = "Student Activities"
        verbose_name_plural = "Student Activities"


class CourseModel(models.Model):
    course_name = models.CharField(
        null=True, max_length=125, verbose_name="course name"
    )
    slug = models.SlugField(null=True, blank=True, editable=False)
    code_name = models.CharField(
        null=True, max_length=125, verbose_name="course code name"
    )
    course_article = models.TextField(
        null=True, max_length=500, verbose_name="course article"
    )
    home_cover_image = models.ImageField(
        upload_to="course-home-cover-images",
        null=True,
        blank=True,
        verbose_name="course home cover image",
        help_text="image size: w-370, h-230",
    )
    cover_image = models.ImageField(
        upload_to="course-cover-images",
        null=True,
        verbose_name="course cover image",
        help_text="image size: w-800, h-500",
    )
    course_glance = RichTextUploadingField(null=True)
    total_student_seat = models.CharField(null=True, max_length=125)
    total_student = models.CharField(null=True, max_length=125)
    total_graduated = models.CharField(null=True, max_length=125)
    total_credit = models.CharField(
        null=True,
        blank=True,
        max_length=125,
        help_text="it's mandatory for hon's courses",
    )
    per_semester_fee = models.CharField(
        null=True,
        blank=True,
        max_length=125,
        help_text="it's mandatory for hon's courses",
    )
    total_tuition_fee = models.CharField(
        null=True,
        blank=True,
        max_length=125,
        help_text="it's mandatory for hon's courses",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.course_name)
        super(CourseModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.course_name}"

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


def routine_upload_path(instance, filename):
    return f"courses/{instance.course.slug}/{filename}"


class RoutineModel(models.Model):
    course = models.ForeignKey(
        CourseModel, on_delete=models.CASCADE, null=True, related_name="routines"
    )
    title = models.CharField(max_length=255, null=True)
    routine = models.FileField(upload_to=routine_upload_path, null=True)
    semester = models.CharField(max_length=15, null=True, blank=True)
    year = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        verbose_name = "Course Routine"
        verbose_name_plural = "Course Routines"


class HistoryModel(models.Model):
    content = RichTextUploadingField(null=True, max_length=9999)
    history_cover_img = models.ImageField(
        upload_to="history-cover-image",
        null=True,
        verbose_name="history cover image",
        help_text="image size: w-800, h-500",
    )

    def __str__(self):
        return f"{self.id} - history | Editable object"

    class Meta:
        verbose_name = "History"
        verbose_name_plural = "History"


class AboutInformationModel(models.Model):
    sub_title = models.CharField(
        null=True, max_length=100, verbose_name="sub title"
    )
    title = models.CharField(null=True, max_length=150)
    content = RichTextUploadingField(null=True, max_length=999)
    cover_img = models.ImageField(
        upload_to="about-section-images",
        null=True,
        verbose_name="about section image",
        help_text="image size: w-800, h-500",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        verbose_name = "About Information"
        verbose_name_plural = "About Informations"


class CodeOfConduct(models.Model):
    text = models.TextField(null=True, max_length=999)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.text}"

    class Meta:
        verbose_name = "Code Of Conduct"
        verbose_name_plural = "Code Of Conduct"