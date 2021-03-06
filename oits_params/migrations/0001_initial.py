# Generated by Django 3.0.5 on 2020-04-11 22:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OitsParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('N', 'New'), ('P', 'Processing'), ('C', 'Complete')], default='N', max_length=1)),
                ('parameters', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='oitsparams',
            index=models.Index(fields=['created_at'], name='oits_params_created_706c87_idx'),
        ),
    ]
