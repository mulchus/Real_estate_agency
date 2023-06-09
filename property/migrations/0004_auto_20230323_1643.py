# Generated by Django 2.2.24 on 2023-03-23 13:43

from django.db import migrations


def set_new_building_signs(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__lt=2015).update(new_building=False)
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20230323_1453'),
    ]

    operations = [
        migrations.RunPython(set_new_building_signs),
    ]
