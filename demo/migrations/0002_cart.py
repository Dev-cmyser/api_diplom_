# Generated by Django 4.1.2 on 2022-10-10 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, max_length=254, verbose_name='Кол-во')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.product', verbose_name='Продукта')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователя')),
            ],
        ),
    ]
