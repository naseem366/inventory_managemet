# Generated by Django 3.1.5 on 2023-10-23 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0004_auto_20231020_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.IntegerField(default=0)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('selling_price', models.IntegerField(default=0)),
                ('transactiondttm', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(default=0)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('orderdttm', models.DateTimeField(auto_now_add=True)),
                ('is_received', models.BooleanField(default=False)),
                ('is_cancel', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
            ],
        ),
    ]
