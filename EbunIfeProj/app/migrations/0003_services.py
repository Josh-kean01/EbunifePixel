# Generated by Django 4.1 on 2024-03-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_gallery_alter_blogpost_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(help_text='What service do you provide? (Not more than 300 characters)', max_length=300)),
            ],
        ),
    ]