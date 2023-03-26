# Generated by Django 2.2.24 on 2023-03-25 15:42

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20230324_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, verbose_name='ФИО владельца', db_index=True)),
                ('owners_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца', db_index=True)),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(
                    blank=True, max_length=20, null=True, region=None, verbose_name='Нормализованный номер владельца',
                    db_index=True)),
                ('flat', models.ManyToManyField(related_name='owner_by', to='property.Flat', verbose_name='В собственности')),
            ],
        ),
    ]
