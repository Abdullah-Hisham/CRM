# Generated by Django 4.2.1 on 2023-08-14 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='nn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bb', models.IntegerField()),
                ('nn', models.CharField(max_length=50)),
            ],
        ),
    ]
