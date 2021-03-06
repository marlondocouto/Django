# Generated by Django 3.0.2 on 2020-02-03 23:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_title', models.CharField(max_length=255)),
                ('meeting_date', models.DateField()),
                ('meeting_time', models.TimeField()),
                ('meeting_location', models.CharField(max_length=255)),
                ('meeting_agenda', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'meetings',
                'db_table': 'meeting',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=255)),
                ('resource_type', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, null=True)),
                ('date_entered', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'resources',
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='MeetingMinutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes_text', models.TextField(verbose_name='Description')),
                ('attendance', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('meeting_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pythonclubapp.Meeting')),
            ],
            options={
                'verbose_name_plural': 'meeting minutes',
                'db_table': 'meeting minute',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=255)),
                ('event_location', models.CharField(max_length=255)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('event_description', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'events',
                'db_table': 'event',
            },
        ),
    ]
