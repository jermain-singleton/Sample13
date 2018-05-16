# Generated by Django 2.0.2 on 2018-05-16 12:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(max_length=100)),
                ('postname', models.CharField(max_length=50)),
                ('post', models.TextField(default='Write a post', max_length=500)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
