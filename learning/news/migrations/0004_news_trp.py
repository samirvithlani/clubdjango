# Generated by Django 4.0.4 on 2022-05-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_reportername'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='trp',
            field=models.IntegerField(null=True),
        ),
    ]
