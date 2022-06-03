# Generated by Django 4.0.4 on 2022-06-02 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0005_alter_salon_image'),
        ('service', '0005_service_price_alter_service_duration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='salon',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='salons.salon', verbose_name='Салон'),
            preserve_default=False,
        ),
    ]