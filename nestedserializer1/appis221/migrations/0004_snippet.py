# Generated by Django 4.1.1 on 2022-09-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appis221', '0003_article_article_alter_article_headline_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
    ]
