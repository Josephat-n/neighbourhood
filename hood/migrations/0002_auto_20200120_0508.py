# Generated by Django 2.1 on 2020-01-20 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hood',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.Hood'),
        ),
    ]