# Generated by Django 3.1.5 on 2023-10-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20231025_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='iin',
            field=models.CharField(default='689874', editable=False, max_length=220, unique=True),
        ),
    ]