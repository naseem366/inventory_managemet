# Generated by Django 3.1.5 on 2023-10-27 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20231026_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='iin',
            field=models.CharField(editable=False, max_length=220, unique=True),
        ),
    ]
