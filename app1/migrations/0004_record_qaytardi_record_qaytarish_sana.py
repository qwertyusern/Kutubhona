# Generated by Django 4.0.3 on 2022-04-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_kitob_muallif_alter_record_kitob_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='qaytardi',
            field=models.CharField(blank=True, default='yoq', max_length=7),
        ),
        migrations.AddField(
            model_name='record',
            name='qaytarish_sana',
            field=models.DateField(blank=True, null=True),
        ),
    ]
