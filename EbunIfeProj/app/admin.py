from django.contrib import admin
from django.contrib.auth.models import Group, User
from app.models import *
# Register your models here.

admin.site.site_header = "Photo Gallery Admin"
admin.site.unregister(Group)
admin.site.unregister(User)



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']   }
    list_display = ('title', 'author', 'date_posted')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'testimony')


admin.site.register(Contact)
admin.site.register(Gallery)
admin.site.register(Service)

