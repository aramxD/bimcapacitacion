# Generated by Django 4.0.1 on 2022-01-21 22:55

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/paginas', verbose_name='Imagen')),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('publicar', models.BooleanField(default=True)),
            ],
        ),
    ]
