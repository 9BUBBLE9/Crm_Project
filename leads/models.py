from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('interested', 'Успешно'),
        ('converted', 'Перезвон'),
        ('canceled', 'Не актуально'),
    ]

    lead_number = models.CharField(max_length=10, unique=True, blank=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    information = models.TextField(blank=True, null=True)
    assignee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='assigned_leads'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    in_queue = models.BooleanField(default=False, verbose_name="В очереди")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.lead_number:
            last_lead = Lead.objects.order_by('id').last()
            if last_lead and last_lead.lead_number.startswith("LD-"):
                try:
                    number = int(last_lead.lead_number.split('-')[1]) + 1
                except:
                    number = 1
            else:
                number = 1
            self.lead_number = f'LD-{number:04d}'
        super().save(*args, **kwargs)