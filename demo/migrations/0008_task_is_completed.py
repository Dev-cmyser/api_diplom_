# Generated by Django 4.2.1 on 2023-06-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
