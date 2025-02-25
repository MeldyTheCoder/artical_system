# Generated by Django 5.0.3 on 2024-12-18 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_order_items_order_rims_order_spares'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='rims',
        ),
        migrations.RemoveField(
            model_name='order',
            name='spares',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('rims', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.rims')),
                ('spares', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.spares')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='blog.orderitem'),
        ),
    ]
