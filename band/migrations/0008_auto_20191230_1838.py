# Generated by Django 3.0 on 2019-12-30 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0007_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='band',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='band.Band'),
        ),
    ]