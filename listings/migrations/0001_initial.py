# Generated by Django 4.1 on 2022-08-19 12:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('genere', models.CharField(choices=[('HH', 'Hiphop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock')], max_length=5)),
                ('bio', models.CharField(max_length=10)),
                ('year_formed', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)])),
                ('active', models.BooleanField(default=True)),
                ('ofecial_page', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('matr', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('sold', models.BooleanField(default=False)),
                ('year', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1990), django.core.validators.MaxValueValidator(2022)])),
                ('type', models.CharField(choices=[('R', 'Records'), ('C', 'Clothing'), ('P', 'Posters'), ('M', 'Miscellaneous')], max_length=10)),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band')),
            ],
        ),
    ]