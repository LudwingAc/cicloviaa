# Generated by Django 2.2.4 on 2019-08-28 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A3', '0003_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_de_corredor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
