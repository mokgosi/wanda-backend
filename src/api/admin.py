from django.contrib import admin
from .models import Testimonial, Wander, Page


# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('body', 'user', 'location', 'date_created', 'moderated')

class WanderAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url', 'date_created')

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_created')    

admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Wander, WanderAdmin)
admin.site.register(Page, PageAdmin)

