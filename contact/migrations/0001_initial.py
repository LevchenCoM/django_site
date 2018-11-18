# Generated by Django 2.1 on 2018-11-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('subject', models.CharField(max_length=128, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Contact message',
                'verbose_name_plural': 'Contact messages',
            },
        ),
    ]