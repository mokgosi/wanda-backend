from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


# Create your models here.
class Testimonial(models.Model):

    RATING_CHOICES = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    # name = models.CharField(max_length=100,)
    location = models.CharField(max_length=100,null=True)
    body = RichTextUploadingField(max_length=300) 
    moderated = models.BooleanField(default=False,)
    # TODO  soft deleted testimonials
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
    date_created = models.DateTimeField(auto_now_add=True,)
    date_updated = models.DateTimeField(auto_now=True,)   
    
    class Meta:
        ordering = ["-moderated", "rating", "-date_created"]
    

    def __str__(self) -> str:
        return f"{self.body[0:50]}"


class Wander(models.Model):

    title = models.CharField(max_length=255)
    caption = RichTextUploadingField(max_length=255)
    video_url = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("wonder-detail", kwargs={"pk": self.pk})


class Page(models.Model):

    title = models.CharField(max_length=255, null=False, blank=False)
    body  =  RichTextUploadingField()
    slug  = models.SlugField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("title",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Page, self).save(*args, **kwargs)