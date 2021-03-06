# Generated by Django 2.2.3 on 2019-07-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Speciality', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='bmdc_reg_no',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='degree_specification',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='user',
            name='title_or_designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='speciality',
            field=models.ManyToManyField(related_name='speciality', to='clientsite.Speciality'),
        ),
    ]
