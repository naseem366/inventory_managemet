# Generated by Django 3.1.5 on 2023-10-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20231025_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='iin',
            field=models.CharField(default='19d941', editable=False, max_length=220, unique=True),
        ),
    ]
