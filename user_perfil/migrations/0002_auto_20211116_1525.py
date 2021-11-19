# Generated by Django 3.2.9 on 2021-11-16 15:25

import ckeditor.fields
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('user_perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(blank=True, max_length=40)),
                ('slug', models.SlugField(blank=True, max_length=400, null=True, unique=True)),
                ('biografia', ckeditor.fields.RichTextField(blank=True)),
                ('profile_pic', django_resized.forms.ResizedImageField(blank=True, crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=100, size=[50, 80], upload_to='authors')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='usuario',
        ),
    ]
