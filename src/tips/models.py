from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import DateTimeField
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField()
    image = models.ImageField(default='category-default.jpg', upload_to='articles')
    approved = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name',) 
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)    

    def get_absolute_url(self):
        return reverse("tips:categories", kwargs={"slug": self.slug})


class Article(models.Model):

    DRAFTED = 'DRAFTED'
    PUBLISHED = 'PUBLISHED'
    DELETED = 'Deleted'

    STATUS_CHOICES = (
        (DRAFTED, 'Draft'),
        (PUBLISHED, 'Publish'),
        (DELETED, 'Deleted'),
    )
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField()
    body = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    image = models.ImageField(default='article-default.jpg', upload_to='articles')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
    date_published = models.DateTimeField(null=True, blank=True, default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("title",)
        ordering = ("-date_published",)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("tips:articles", 
            kwargs={'username': self.author.username.lower(), 'slug': self.slug})
    

class Comment(models.Model):
    
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField()
    comment = RichTextUploadingField(null=False, blank=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    approved = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created',]

    def __str__(self):
        return f"Comment by {self.name} on {self.article}"


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile-default.jpg', upload_to='user_profiles')
    job_titile = models.CharField(max_length=100)
    bio = models.CharField(max_length=200, help_text='Short Bio (eg. I love cats and games)')
    twitter = models.CharField(max_length=150, null=True, blank=True, default='#')
    linkdin = models.CharField(max_length=150, null=True, blank=True, default='#')
    instagram = models.CharField(max_length=150, null=True, blank=True, default='#')
    github = models.CharField(max_length=150, null=True,blank=True, default='#')
    facebook = models.CharField(max_length=150, null=True, blank=True, default='#')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    




