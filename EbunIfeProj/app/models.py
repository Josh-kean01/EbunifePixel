from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Contact(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.TextField()


class Service(models.Model):
    service = models.CharField(max_length = 300, help_text='What service do you provide? (Not more than 300 characters)')

    def __str__(self):
        return self.service
    

class BlogPost(models.Model):
    title= models.CharField(max_length=200)
    slug = models.SlugField()
    cover = models.ImageField(upload_to='uploads/posts/')
    content = RichTextUploadingField()
    author = models.ForeignKey(get_user_model(), verbose_name=("posts"), default="AUTHOR", on_delete=models.SET_DEFAULT)
    date_posted = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        ordering= ('-date_posted',)

    
class Testimonial(models.Model):
    img = models.ImageField( upload_to='uploads/testimonials/', blank=True, null=True)
    author = models.CharField(max_length=100)
    testimony = models.TextField()


    def __str__(self):
        return str(self.author)


class Gallery(models.Model):

    image = models.ImageField(upload_to='uploads/gallery/')

    def __str__(self):
        return f"Image {str(self.id)}"

    class Meta:
        verbose_name_plural = 'Gallery'

