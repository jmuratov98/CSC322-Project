# Generated by Django 3.1.3 on 2020-11-29 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=15.0, max_digits=5),
        ),
    ]