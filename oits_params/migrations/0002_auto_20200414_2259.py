# Generated by Django 3.0.5 on 2020-04-14 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oits_params', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oitsparams',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddIndex(
            model_name='oitsparams',
            index=models.Index(fields=['status'], name='oits_params_status_2c55df_idx'),
        ),
    ]
