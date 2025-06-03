from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_number', models.CharField(max_length=10, null=True, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('new', 'Новый'), ('interested', 'Клиент заинтересован в услуге'), ('converted', 'Перевоз'), ('canceled', 'Отказ')], default='new', max_length=20)),
                ('information', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_leads', to='auth.user')),
            ],
        ),
    ]