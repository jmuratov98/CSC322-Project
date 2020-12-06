# Generated by Django 3.1.4 on 2020-12-06 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_auto_20201205_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='reservationID',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.reservation'),
        ),
    ]
