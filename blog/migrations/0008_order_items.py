# Generated by Django 5.0.3 on 2024-12-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='blog.cart'),
        ),
    ]
