# Generated by Django 4.1.2 on 2022-10-18 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('apellido_parterno', models.TextField()),
                ('apellido_materno', models.TextField()),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
