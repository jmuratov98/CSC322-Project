# Generated by Django 3.1.2 on 2020-12-11 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='chef',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chef', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='restaurant.OrderDetails'),
        ),
        migrations.AddField(
            model_name='order',
            name='reservationID',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.reservation'),
        ),
    ]
