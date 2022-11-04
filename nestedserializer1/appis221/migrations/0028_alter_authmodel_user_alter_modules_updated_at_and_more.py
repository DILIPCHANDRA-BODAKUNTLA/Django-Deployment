# Generated by Django 4.1.1 on 2022-10-17 14:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appis221', '0027_alter_authmodel_user_alter_modules_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='modules',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 17, 20, 20, 32, 746937), null=True),
        ),
        migrations.AlterField(
            model_name='studentformodule',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 17, 20, 20, 32, 746937), null=True),
        ),
    ]