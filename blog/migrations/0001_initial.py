# Generated by Django 3.2.7 on 2021-09-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=256)),
                ('blog_date', models.DateTimeField(auto_now_add=True)),
                ('blog_text', models.CharField(max_length=2048)),
                ('blog_image', models.ImageField(upload_to='blog_images/')),
            ],
        ),
    ]