# Generated by Django 2.2.3 on 2019-07-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(error_messages={'required': 'Role must be provided'}, max_length=12)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('chamber', models.CharField(blank=True, max_length=100, null=True)),
                ('speciality', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
