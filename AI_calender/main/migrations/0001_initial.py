# Generated by Django 4.1.1 on 2022-09-21 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individual_data',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('description', models.CharField(blank=True, max_length=100)),
                ('end_date', models.DateTimeField()),
                ('schedule_class', models.CharField(max_length=1)),
                ('user_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.individual_data')),
            ],
        ),
    ]
