# Generated by Django 3.0.8 on 2020-10-24 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fechaNacimiento', models.DateTimeField(verbose_name='Fecha de nacimiento')),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
