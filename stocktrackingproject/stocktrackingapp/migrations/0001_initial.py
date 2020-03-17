# Generated by Django 3.0.4 on 2020-03-17 16:18

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
            name='StockType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockname', models.CharField(max_length=255)),
                ('stockticker', models.CharField(max_length=50)),
                ('stockdescription', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'stocktypes',
                'db_table': 'stocktype',
            },
        ),
        migrations.CreateModel(
            name='StockPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockHighPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stockLowPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stockBuyPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stockBuyDate', models.DateField()),
                ('stockAdditionalInfo', models.TextField(blank=True, null=True)),
                ('stockticker', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stocktrackingapp.StockType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'stockperformances',
                'db_table': 'stockperformance',
            },
        ),
        migrations.CreateModel(
            name='FinanceResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourcename', models.CharField(max_length=255)),
                ('resourcetype', models.CharField(max_length=200)),
                ('resourcedescription', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'financeresources',
                'db_table': 'financeresource',
            },
        ),
    ]