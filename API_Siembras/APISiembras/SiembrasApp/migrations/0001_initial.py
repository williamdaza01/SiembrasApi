# Generated by Django 4.1.1 on 2022-09-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arboles',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'arboles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contratistas',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'contratistas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
            ],
            options={
                'db_table': 'municipios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Siembras',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.TextField()),
                ('total_arboles', models.IntegerField(blank=True, null=True)),
                ('total_hectareas', models.FloatField()),
            ],
            options={
                'db_table': 'siembras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Veredas',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
            ],
            options={
                'db_table': 'veredas',
                'managed': False,
            },
        ),
    ]