# Generated by Django 3.1.2 on 2021-01-02 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oits_params', '0003_oitsparams_readonly'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrajectoryResult',
            fields=[
                ('oits_params', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='oits_params.oitsparams')),
                ('values', models.TextField()),
                ('exception', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
