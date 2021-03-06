# Generated by Django 3.2.5 on 2021-08-18 20:18

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Imagine')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='MultiFile',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MultiImage',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Numele şi prenumele')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Funcţia persoanei')),
                ('img', models.ImageField(upload_to='person/', verbose_name='Imagine')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Numărul de telefon')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(editable=False, max_length=250, unique=True)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('multifile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='website.multifile')),
                ('multiimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.multiimage')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Text')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('cover_photo', models.ImageField(upload_to='blog_images/', verbose_name='Imagine')),
                ('slug', models.SlugField(editable=False, max_length=250, unique=True)),
            ],
            options={
                'ordering': ('-date_created',),
            },
            bases=('website.multiimage', 'website.multifile'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='imageid', to='website.multiimage')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Material aditional')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='fileid', to='website.multifile')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPost',
            fields=[
                ('multifile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='website.multifile')),
                ('multiimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.multiimage')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Text')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('cover_photo', models.ImageField(upload_to='project_images/')),
                ('slug', models.SlugField(editable=False, max_length=250, unique=True)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.tag')),
            ],
            options={
                'ordering': ('-date_created',),
            },
            bases=('website.multiimage', 'website.multifile'),
        ),
    ]
