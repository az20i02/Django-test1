# Generated by Django 5.0.7 on 2024-07-22 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_item_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
    ]
