# Generated by Django 3.1.5 on 2023-10-26 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20231025_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='iin',
            field=models.CharField(default='fa2b48', editable=False, max_length=220, unique=True),
        ),
    ]