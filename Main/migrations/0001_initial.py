# Generated by Django 3.1 on 2020-09-08 10:37

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_devops', models.CharField(max_length=60, verbose_name='Fullname')),
                ('key_words', models.CharField(max_length=500, verbose_name='Key words')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('faq_icon', models.ImageField(upload_to='images', verbose_name='Faq icon')),
                ('logo', models.ImageField(upload_to='images', verbose_name='Logo')),
                ('description', models.TextField(verbose_name='Description')),
                ('project_developing_start_time', models.DateField()),
                ('project_developing_finish_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('image', models.ImageField(upload_to='images', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('email', models.EmailField(max_length=40, verbose_name='Email')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=60, verbose_name='Fullname')),
                ('email', models.CharField(max_length=40, verbose_name='Email')),
                ('phone_number', models.PositiveIntegerField(verbose_name='Phone Number')),
                ('location', models.CharField(max_length=100, verbose_name='Our location')),
            ],
            options={
                'verbose_name': 'Our Contact',
                'verbose_name_plural': 'Our Contacts',
            },
        ),
        migrations.CreateModel(
            name='Helps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popular_questions', models.TextField(verbose_name='Popular questions')),
                ('answers', models.TextField(verbose_name='Answers')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
            ],
            options={
                'verbose_name': 'Helps',
                'verbose_name_plural': 'Helps',
            },
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_of_service', ckeditor.fields.RichTextField(verbose_name='Terms of Service')),
                ('privacy_policy', ckeditor.fields.RichTextField(verbose_name='Privacy Policy')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
            },
        ),
        migrations.CreateModel(
            name='WebsiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(choices=[('az', 'Azerbaijan'), ('eng', 'English'), ('rus', 'Russian')], max_length=5, verbose_name='Type')),
                ('cover_image', models.ImageField(upload_to='image', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Name')),
                ('location', models.CharField(max_length=40, verbose_name='Name')),
                ('image', models.ImageField(upload_to='images', verbose_name='Image')),
                ('description', models.TextField(verbose_name='Description')),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price')),
                ('longtitude', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='Main.city', verbose_name='City')),
            ],
            options={
                'verbose_name': 'Places',
                'verbose_name_plural': 'Places',
            },
        ),
    ]
