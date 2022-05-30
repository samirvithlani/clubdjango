# Generated by Django 4.0.4 on 2022-05-30 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_trp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('author_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='news.author')),
                ('bookName', models.CharField(max_length=200)),
                ('bookprice', models.FloatField()),
                ('publishDate', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'db_table': 'books',
            },
            bases=('news.author',),
        ),
    ]
