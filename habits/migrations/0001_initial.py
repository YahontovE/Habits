# Generated by Django 4.2.6 on 2023-10-31 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200, verbose_name='Место выполениня')),
                ('time', models.TimeField(verbose_name='Время выполения')),
                ('action', models.CharField(max_length=200, verbose_name='активность в пирвычке')),
                ('is_pleasnt', models.BooleanField(default=False, verbose_name='признак приятной привычки')),
                ('period', models.IntegerField(default=1, verbose_name='колличество выполнений в неделю')),
                ('reward', models.CharField(max_length=150, verbose_name='награда за привычку')),
                ('duration', models.IntegerField(verbose_name='время выполнения в секундах')),
                ('is_public', models.BooleanField(verbose_name='признак публичности')),
                ('linked', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='связанная привычка')),
            ],
        ),
    ]
