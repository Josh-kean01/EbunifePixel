from django.shortcuts import render, redirect

from .models import BlogPost, Gallery, Testimonial, Contact, Service
from django.contrib import messages

# Create your views here.

def index(request):

    two_posts = BlogPost.objects.all()[:2]
    gallery = Gallery.objects.all()[:9]
    testimonies = Testimonial.objects.all()[:6]

    services = Service.objects.all()
    services_partA = services[ : (len(services) + 1 ) //2]
    services_partB = services[ (len(services) + 1) //2 : ]


    if request.method == 'POST' and 'contact_form' in request.POST:
        
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        new_contact = Contact( firstname= firstname,  lastname= lastname, email= email,  subject= subject,   message= message )

        new_contact.save()
        messages.success(request, "I've received your message. I'll get back to you shortly!!", extra_tags="success")
        return redirect('index')

    context = {
        'posts' : two_posts,
        'pictures_gallery': gallery,
        'testimonies': testimonies,
        'servicesA': services_partA,
        'servicesB': services_partB
    }

    return render(request, 'index.html', context)

def services(request):
    return render(request, 'services.html')

def about(request):
    testimonies = Testimonial.objects.all()[:6]

    return render(request, 'about.html', {'testimonies': testimonies})

def blog(request):
    return render(request, 'blog.html')

def gallery(request):
    return render(request, 'gallery.html')

def blog_detail(request, pk):
    return render(request, 'blog-single.html')
