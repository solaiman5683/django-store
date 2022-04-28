# Generated by Django 4.0.4 on 2022-04-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_address_address_address_address_line_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='fist_name',
            new_name='first_name',
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='store_custo_last_na_e6a359_idx'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store_customers',
        ),
    ]