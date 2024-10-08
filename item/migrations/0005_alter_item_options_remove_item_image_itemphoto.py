# Generated by Django 5.0.7 on 2024-07-27 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_alter_item_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',), 'verbose_name_plural': 'Items'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.CreateModel(
            name='ItemPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='item_images')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='item.item')),
            ],
        ),
    ]
