# Generated by Django 3.2.9 on 2021-11-16 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post_noticias', '0003_alter_categoria_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postagem',
            options={'verbose_name_plural': 'Postagens'},
        ),
    ]