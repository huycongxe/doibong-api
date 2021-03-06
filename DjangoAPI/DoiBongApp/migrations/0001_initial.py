# Generated by Django 3.2.5 on 2021-08-01 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doibong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('short_name', models.CharField(max_length=200, null=True)),
                ('area', models.CharField(choices=[('Asia', 'Asia'), ('Africa', 'Africa'), ('Europe', 'Europe'), ('North America', 'North America'), ('South America', 'South America'), ('Australia', 'Australia')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cauthu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField(null=True)),
                ('number', models.IntegerField(null=True)),
                ('height', models.IntegerField(null=True)),
                ('weight', models.IntegerField(null=True)),
                ('avatar', models.CharField(max_length=500)),
                ('doibong', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DoiBongApp.doibong')),
            ],
        ),
    ]
