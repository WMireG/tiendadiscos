# Generated by Django 5.0.6 on 2024-06-23 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]