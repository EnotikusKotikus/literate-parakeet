from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import string
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from transliterate import translit


# Create your models here.



class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=250, unique=True, editable=False)
    
    class Meta:
        ordering=('-name',)
        verbose_name_plural = 'Categorii'
    
    def __str__(self):
	    return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            name = translit(self.name, 'ru', reversed=True)
            self.slug = slugify(name)
        super(Tag, self).save(*args, **kwargs)


class MultiImage(models.Model):
    image_id = models.AutoField(primary_key=True)

class MultiFile(models.Model):
    file_id = models.AutoField(primary_key=True)


class Image(models.Model):
    post = models.ForeignKey(MultiImage, default=None, on_delete=models.CASCADE,  related_name='imageid')
    image = models.FileField()
    
    def __str__(self):
        return str(self.image)

class File(models.Model):
    post = models.ForeignKey(MultiFile, default=None, on_delete=models.CASCADE,  related_name='fileid')
    file = models.FileField(null=True, blank=True, max_length=255, verbose_name='Material aditional')
    
    def __str__(self):
        return str(self.file)
    



class ProjectPost(MultiImage, MultiFile):
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)

    
    title = models.CharField(max_length=255)
    content = RichTextUploadingField(blank=True, null=True, verbose_name='Text')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    cover_photo = models.ImageField(upload_to = 'project_images/')
    
    slug = models.SlugField(max_length=250, unique=True, editable=False)
    
    class Meta:
        ordering = ('-date_created', )
        verbose_name_plural = 'Postări cu Proiecte'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            temp_title = translit(self.title, 'ru', reversed=True)
            self.slug = slugify(temp_title)

        super(ProjectPost, self).save(*args, **kwargs)



class NewsPost(MultiImage, MultiFile):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField(blank=True, null=True, verbose_name='Text')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    cover_photo = models.ImageField(upload_to='news_images/',verbose_name='Imagine')
    
    slug = models.SlugField(max_length=250, unique=True, editable=False)
   

    class Meta:
        ordering = ('-date_created', )
        verbose_name_plural = 'Postări cu Noutăţi'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            temp_title = translit(self.title, 'ru', reversed=True)
            self.slug = slugify(temp_title)
        super(NewsPost, self).save(*args, **kwargs)


class Person(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Numele şi prenumele')
    position = models.CharField(max_length=255, blank=True, null=True, verbose_name='Funcţia persoanei')
    img = models.ImageField(upload_to='person/',verbose_name='Imagine')
    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name='Email')
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name='Numărul de telefon')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-name', )
        verbose_name_plural = 'Persoane'


class GalleryItem(models.Model):
    img = models.ImageField(verbose_name='Imagine')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.img)


    class Meta:
        ordering = ('-date_created', )
        verbose_name_plural = 'Imagini Galerie'

class AboutCompanyText(models.Model):
    content = RichTextUploadingField(blank=False, null=False, verbose_name='Text')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.date_created)

    class Meta:
        ordering = ('-date_created', )
        verbose_name_plural = 'Despre Noi Pagina'
