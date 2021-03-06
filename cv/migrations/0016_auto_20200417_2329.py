# Generated by Django 2.1.4 on 2020-04-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0015_auto_20200417_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='permanent_address',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AddField(
            model_name='resume',
            name='present_end',
            field=models.CharField(default='Present', max_length=20),
        ),
        migrations.AddField(
            model_name='resume',
            name='present_start',
            field=models.CharField(default='Jan, 2020', max_length=20),
        ),
        migrations.AddField(
            model_name='resume',
            name='previous_end',
            field=models.CharField(default='Feb, 2020', max_length=20),
        ),
        migrations.AddField(
            model_name='resume',
            name='previous_start',
            field=models.CharField(default='Jan, 2020', max_length=20),
        ),
    ]
