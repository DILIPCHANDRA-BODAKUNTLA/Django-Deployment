# Generated by Django 4.1.1 on 2022-10-03 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appis221', '0009_modules_updated_at_alter_modules_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modules',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modules',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
