# Generated by Django 4.1 on 2022-11-09 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvt_members', '0004_national_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='national',
            name='category',
            field=models.CharField(choices=[('Presidential', 'Presidential'), ('Cabinet', 'Cabinet')], max_length=200, null=True),
        ),
    ]
