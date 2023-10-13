from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Department(models.Model):
    department_name = models.CharField(max_length=120, null=True)
    hod = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.department_name


class Course(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True)
    course_name = models.CharField(max_length=120, null=True)
    course_code = models.CharField(max_length=120, null=True)
    course_credit = models.FloatField(null=True)

    def __str__(self):
        return f'{self.course_code} {self.course_name} - {self.department.department_name}'


#  student registration university table
class StudentRegistrationUni(models.Model):
    ACD_STATUS = (
        ('', 'Select Status'),
        ('running', 'Running '),
        ('inactive', 'Inactive'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    student_id = models.BigIntegerField(null=True, unique=True)
    name = models.CharField(max_length=120, null=True)
    email = models.CharField(max_length=120, null=True)
    phone = models.BigIntegerField(null=True, blank=True)
    fathername = models.CharField(max_length=120, blank=True, null=True)
    mothername = models.CharField(max_length=120, blank=True, null=True)
    dob = models.DateField(null=True)
    adminsion_year = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(max_length=120, null=True, blank=True)
    academic_status = models.CharField(
        max_length=120, null=True, choices=ACD_STATUS, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True)
    religion = models.CharField(max_length=120, null=True, blank=True)
    nationality = models.CharField(max_length=120, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_image', null=True, blank=True)
    cgpa = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.student_id}'

    class Meta:
        verbose_name = 'Registration (University)'
        verbose_name_plural = 'Registration (University)'

        ordering = ['-id']


#  student registration collage table
class StudentRegistrationCollage(models.Model):
    ACD_STATUS = (
        ('', 'Select Status'),
        ('running', 'Running '),
        ('inactive', 'Inactive'),
    )
    GROUPS = (
        ('', 'Select Group'),
        ('science', 'Science'),
        ('commerce', 'Business Studies / Commerce'),
        ('arts', 'Humanities / Arts'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    student_id = models.BigIntegerField(null=True, unique=True)
    name = models.CharField(max_length=120, null=True)
    email = models.CharField(max_length=120, null=True)
    phone = models.BigIntegerField(null=True)
    fathername = models.CharField(max_length=120, blank=True, null=True)
    mothername = models.CharField(max_length=120, blank=True, null=True)
    dob = models.DateField(null=True)
    adminsion_year = models.CharField(max_length=50, null=True)
    address = models.TextField(max_length=120, null=True)
    academic_status = models.CharField(
        max_length=120, null=True, choices=ACD_STATUS)
    group = models.CharField(max_length=120, null=True, choices=GROUPS)
    religion = models.CharField(max_length=120, null=True)
    nationality = models.CharField(max_length=120, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_image', null=True, blank=True)

    def __str__(self):
        return f'{self.student_id}'

    class Meta:
        verbose_name = 'Registration (HSC)'
        verbose_name_plural = 'Registration (HSC)'

        ordering = ['-id']


class Enroll(models.Model):
    student = models.ForeignKey(
        StudentRegistrationUni, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    enroll_year = models.IntegerField(blank=True, null=True)
    enroll_semester = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.student.student_id} - {self.course.course_code} ({self.enroll_year}year {self.enroll_semester}semester)'

    class Meta:
        ordering = ['-id']


class Result(models.Model):
    student = models.ForeignKey(
        StudentRegistrationUni, on_delete=models.CASCADE, null=True)
    enroll_course = models.ForeignKey(
        Enroll, on_delete=models.CASCADE, null=True)
    grade_point = models.FloatField(null=True)
    grade_letter = models.CharField(max_length=5, null=True)

    def __str__(self):
        return f'{self.student.student_id} - {self.grade_point} ({self.grade_letter})'

    class Meta:
        verbose_name = 'Result (University)'
        verbose_name_plural = 'Result (University)'

        ordering = ['-id']


class FinancialUni(models.Model):
    student = models.ForeignKey(
        StudentRegistrationUni, on_delete=models.CASCADE, null=True)
    year = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)
    payment_date = models.DateField(null=True, default=now)
    payment_amount = models.FloatField(null=True, default=0.0)
    money_receipt_no = models.CharField(max_length=120, null=True)

    def __str__(self):
        return f'Payment of #{self.student.student_id} - {self.year}year {self.semester}semester'

    class Meta:
        verbose_name = 'Financial (University)'
        verbose_name_plural = 'Financial (University)'

        ordering = ['-id']


class FinancialCollege(models.Model):
    student = models.ForeignKey(
        StudentRegistrationCollage, on_delete=models.CASCADE, null=True)
    payment_date = models.DateField(null=True, default=now)
    payment_amount = models.FloatField(null=True, default=0.0)
    money_receipt_no = models.CharField(max_length=120, null=True)
    comment = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return f'Payment of #{self.student.student_id} - ({self.student.group} Group)'

    class Meta:
        verbose_name = 'Financial (HSC)'
        verbose_name_plural = 'Financial (HSC)'

        ordering = ['-id']
