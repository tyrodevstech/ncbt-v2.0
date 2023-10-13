from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=122, null=True)
    post = models.CharField(max_length=120, null=True)
    educational_qualification = models.CharField(max_length=255, null=True)
    teacher_picture = models.ImageField(upload_to= 'teacher_picture', null=True, blank=True)

    def __str__(self):
        return f'Name: {self.name}'

class Notice(models.Model):
    post_title = models.CharField(null = True, max_length= 150)
    post_content = models.TextField(null=True, max_length=500)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Post: {self.post_title}"


class Contact(models.Model):
    name = models.CharField(max_length=122, null=True)
    email = models.CharField(max_length=122, null=True)
    phone = models.CharField(max_length=12, null=True)
    address = models.CharField(max_length=12, null=True, blank=True)
    desc = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.email}'


class NoticeImages(models.Model):
    title = models.CharField(max_length=120, null=True,blank=True)
    notice_images = models.ImageField(upload_to= 'notice_images', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return f'#{self.id} {self.title}'
    class Meta:
        verbose_name = 'Image Notice'
        verbose_name_plural = 'Image Notice'