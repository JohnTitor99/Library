# Generated by Django 4.0.4 on 2022-11-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_finished_name_alter_library_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finished',
            name='name',
            field=models.CharField(blank=True, max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='wish',
            name='name',
            field=models.CharField(blank=True, max_length=56, null=True),
        ),
    ]
