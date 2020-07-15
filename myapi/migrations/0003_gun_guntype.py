# Generated by Django 3.0.8 on 2020-07-12 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_grip_health'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guntype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='gun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('ammo', models.FloatField()),
                ('mag', models.FloatField()),
                ('ext_mag', models.FloatField()),
                ('fire_rate', models.FloatField()),
                ('damage', models.FloatField()),
                ('bullet_speed', models.FloatField()),
                ('rload', models.FloatField()),
                ('shot_range', models.FloatField()),
                ('scoped_spread', models.FloatField()),
                ('dps', models.FloatField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.Guntype')),
            ],
        ),
    ]
