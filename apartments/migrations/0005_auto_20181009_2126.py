# Generated by Django 2.1 on 2018-10-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0004_auto_20181009_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentdates',
            name='status',
            field=models.CharField(choices=[('0', 'Disable'), ('1', 'Booked')], default='0', max_length=1),
        ),
    ]
