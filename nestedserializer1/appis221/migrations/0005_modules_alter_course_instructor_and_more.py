# Generated by Django 4.1.1 on 2022-09-28 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appis221', '0004_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=100)),
                ('module_duration', models.IntegerField()),
                ('class_room', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appis221.instructor'),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('title', 'instructor')},
        ),
        migrations.CreateModel(
            name='StudentforModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('modules', models.ManyToManyField(to='appis221.modules')),
            ],
        ),
    ]
