# Generated by Django 5.2.1 on 2025-06-03 08:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_leads', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='information',
            field=models.TextField(blank=True, null=True, verbose_name='Информация о клиенте'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='lead_number',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='Номер лида'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('new', 'Новый'), ('interested', 'Успешно'), ('converted', 'Перезвон'), ('canceled', 'Не актуально')], default='new', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
