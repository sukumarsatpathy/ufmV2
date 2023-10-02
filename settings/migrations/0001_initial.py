# Generated by Django 4.2.5 on 2023-10-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Brand Name')),
                ('slogan', models.CharField(max_length=255, null=True, verbose_name='Slogan')),
                ('logo_dark', models.ImageField(upload_to='settings/logo/%Y/%m/%d/', verbose_name='Logo Dark')),
                ('logo_light', models.ImageField(upload_to='settings/logo/%Y/%m/%d/', verbose_name='Logo Light')),
                ('favicon', models.FileField(upload_to='settings/favicon/%Y/%m/%d/', verbose_name='Favicon')),
                ('default_user', models.ImageField(blank=True, null=True, upload_to='settings/user/%Y/%m/%d/', verbose_name='Default User Image')),
                ('public_key', models.CharField(blank=True, max_length=255, null=True, verbose_name='Google reCaptcha Public Key')),
                ('private_key', models.CharField(blank=True, max_length=255, null=True, verbose_name='Google reCaptcha Private Key')),
                ('meta_title', models.CharField(max_length=60, null=True, verbose_name='Meta Title')),
                ('meta_description', models.CharField(max_length=158, null=True, verbose_name='Meta Description')),
                ('meta_keywords', models.CharField(max_length=255, null=True, verbose_name='Meta Keywords')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
            ],
            options={
                'verbose_name': 'Web Setting',
                'verbose_name_plural': 'Web Settings',
                'db_table': 'settings-website',
            },
        ),
    ]
