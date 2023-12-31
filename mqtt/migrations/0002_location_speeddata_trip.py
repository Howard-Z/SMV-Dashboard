# Generated by Django 3.2.13 on 2023-11-05 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank='', default='', max_length=128, null='')),
                ('active', models.BooleanField(default=False)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SpeedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.DecimalField(decimal_places=3, max_digits=6)),
                ('date', models.DateTimeField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mqtt.trip')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=11)),
                ('date', models.DateTimeField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mqtt.trip')),
            ],
        ),
    ]
