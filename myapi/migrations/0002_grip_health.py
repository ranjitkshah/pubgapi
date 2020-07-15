# Generated by Django 3.0.8 on 2020-07-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='grip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('DRP', models.FloatField()),
                ('H_recoil', models.FloatField()),
                ('V_recoil', models.CharField(max_length=60)),
                ('sway', models.FloatField()),
                ('kick_animation', models.FloatField()),
                ('dec_adsSpeed', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='health',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('action_time', models.CharField(max_length=60)),
                ('health_gained', models.FloatField()),
                ('boost_bar', models.CharField(max_length=20)),
                ('duration', models.FloatField()),
            ],
        ),
    ]
