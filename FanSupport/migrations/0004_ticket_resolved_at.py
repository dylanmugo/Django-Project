# Generated by Django 5.1.7 on 2025-03-30 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FanSupport', '0003_ticket_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='resolved_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
