# Generated by Django 4.1.1 on 2022-10-03 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appis221', '0010_alter_modules_created_at_alter_modules_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modules',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 3, 11, 28, 23, 266624, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
