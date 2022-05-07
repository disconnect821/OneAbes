# Generated by Django 4.0.4 on 2022-05-07 07:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0002_alter_task_task_from_alter_task_task_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_to',
        ),
        migrations.AddField(
            model_name='task',
            name='task_to',
            field=models.ManyToManyField(related_name='tasks_given', to=settings.AUTH_USER_MODEL),
        ),
    ]
