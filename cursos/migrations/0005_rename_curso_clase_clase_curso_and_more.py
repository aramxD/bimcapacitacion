# Generated by Django 4.0.1 on 2022-03-16 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_alter_clase_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clase',
            old_name='curso',
            new_name='clase_curso',
        ),
        migrations.RenameField(
            model_name='cursos',
            old_name='slug',
            new_name='curso_slug',
        ),
    ]
