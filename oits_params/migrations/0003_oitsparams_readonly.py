# Generated by Django 3.1.2 on 2020-12-28 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oits_params', '0002_auto_20200414_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='oitsparams',
            name='readonly',
            field=models.BooleanField(default=False),
        ),
    ]
