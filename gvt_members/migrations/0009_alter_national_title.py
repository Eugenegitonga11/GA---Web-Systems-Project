# Generated by Django 4.1.3 on 2022-11-23 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvt_members', '0008_womenrepresentatives'),
    ]

    operations = [
        migrations.AlterField(
            model_name='national',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]