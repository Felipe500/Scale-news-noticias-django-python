# Generated by Django 3.2.9 on 2021-11-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post_comentarios', '0002_alter_comentario_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'verbose_name_plural': 'Comentarios'},
        ),
        migrations.AlterField(
            model_name='comentario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
