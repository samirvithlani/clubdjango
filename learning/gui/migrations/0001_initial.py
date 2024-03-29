# Generated by Django 4.0.4 on 2022-06-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('age', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('hobbies', models.CharField(choices=[('reading', 'Reading'), ('writing', 'Writing'), ('playing', 'Playing'), ('colleting', 'Collecting')], max_length=100)),
            ],
            options={
                'db_table': 'doctor1',
            },
        ),
    ]
