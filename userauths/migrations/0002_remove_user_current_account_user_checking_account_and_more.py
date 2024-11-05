# Generated by Django 5.0.6 on 2024-10-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='current_account',
        ),
        migrations.AddField(
            model_name='user',
            name='checking_account',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='savings_account',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True),
        ),
    ]