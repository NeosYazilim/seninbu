# Generated by Django 3.2 on 2021-12-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], default='Evet', max_length=10),
            preserve_default=False,
        ),
    ]