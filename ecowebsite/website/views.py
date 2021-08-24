from django.shortcuts import render, get_object_or_404
from .models import Image,NewsPost, ProjectPost, Tag,Person, GalleryItem, File, AboutCompanyText
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def home(request):
    project_posts = ProjectPost.objects.all().order_by('-date_created')[:3]
    news_posts = NewsPost.objects.all().order_by('-date_created')[:3]
    
    #posts = list(project_posts) + list(news_posts)
    posts = {'projects':list(project_posts),  'news':list(news_posts)}


    context = {
        'posts':posts,
        
    }

    return render(request, 'website/home.html', context)

def projects(request, tag=None):
    
    curent_tag = 'Toate' # Default tag to show

    if tag is not None:
        object_list = ProjectPost.objects.filter(tag__slug=tag) 
        curent_tag = Tag.objects.filter(slug=tag)[0] # Get name of current tag
    else:
        object_list = ProjectPost.objects.all()

    tags = Tag.objects.all()

    paginator = Paginator(object_list, 9)
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
        print('Page is an integer')
        print(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
        
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    
    context = {
        'posts':posts, 
        'tags':tags,
        'curent_tag':curent_tag,
        }
    return render(request, 'website/projects.html', context)




def about_company(request):
    text = AboutCompanyText.objects.all().first()
    context = {
        'text':text
    }
    print(text)
    return render(request, 'website/about_company.html', context)



def people(request):
    people = Person.objects.all()

    context = {
        'people':people
    }
    return render(request, 'website/people.html', context)


def news(request):
   

    object_list = NewsPost.objects.all()




    paginator = Paginator(object_list, 9)
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)



    context = {
        'posts':posts, 
        }
    return render(request, 'website/news.html', context)



def contact_us(request):
    mapbox_access_token = settings.MAPTOKEN
    context = {
        'was_sent':False,
        'mapbox_access_token':mapbox_access_token
    }
    if request.method == 'POST':

        user_name = request.POST.get('user_name')  
        user_email = request.POST.get('user_email')
        user_phone = request.POST.get('user_phone')
        user_message = request.POST.get('user_message')
        sender = settings.EMAIL_HOST_USER
        message = f'Numele: {user_name}\nEmail: {user_email}\nTelefonul: {user_phone}\nMesajul: {user_message}'
        send_mail(user_name, message, sender, ['auritarius@gmail.com'])
        
        context['was_sent'] = True

        return render(request, 'website/contact-us.html', context)

    return render(request, 'website/contact-us.html', context)


def news_single(request, post):

    post = get_object_or_404(NewsPost, slug=post)
    photos = Image.objects.filter(post=post)
    files = File.objects.filter(post=post)
    
    number_photos = list(range(0,len(photos)))
    print(number_photos)
    context = {
        'post':post,
        'photos':photos,
        'files':files,
        'number_photos':number_photos
        }
    return render(request, 'website/news_single.html', context)



def project_single(request, tag, post):

    post = get_object_or_404(ProjectPost, slug=post)
    photos = Image.objects.filter(post=post)
    files =  File.objects.filter(post=post)
    number_photos = list(range(0,len(photos)))
    print(number_photos)

    context = {
        'post':post,
        'photos':photos,
        'files':files,
        'number_photos':number_photos
        }
    return render(request, 'website/project_single.html', context)


def gallery(request):
    object_list = GalleryItem.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    
    try:
        images = paginator.get_page(page)
        print('Page is an integer')
        print(object_list)
        
    except PageNotAnInteger:
        images = paginator.page(1)
        print(f' Not an Integer')
        print(object_list)
        
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
        print(object_list)
        

    context = {
        'images':images
    }
    return render(request, 'website/gallery.html', context)