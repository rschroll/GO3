# Generated by Django 3.0 on 2020-01-20 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0003_section_is_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
