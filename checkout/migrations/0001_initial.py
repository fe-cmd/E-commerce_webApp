# Generated by Django 5.0.3 on 2024-11-19 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_name', models.CharField(help_text='Required', max_length=255, verbose_name='delivery_name')),
                ('delivery_price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'The price must be between 0 and 999.99.'}}, help_text='Maximum 999.99', max_digits=5, verbose_name='delivery price')),
                ('delivery_method', models.CharField(choices=[('IS', 'In Store'), ('HD', 'Home Delivery'), ('DD', 'Digital Delivery')], help_text='Required', max_length=255, verbose_name='delivery_method')),
                ('delivery_timeframe', models.CharField(help_text='Required', max_length=255, verbose_name='delivery timeframe')),
                ('delivery_window', models.CharField(help_text='Required', max_length=255, verbose_name='delivery window')),
                ('order', models.IntegerField(default=0, help_text='Required', verbose_name='list order')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Delivery Option',
                'verbose_name_plural': 'Delivery Options',
            },
        ),
        migrations.CreateModel(
            name='PaymentSelections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=255, verbose_name='name')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Payment Selection',
                'verbose_name_plural': 'Payment Selections',
            },
        ),
    ]
