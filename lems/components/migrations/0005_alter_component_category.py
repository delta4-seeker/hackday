# Generated by Django 4.0.6 on 2022-07-16 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0004_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='components.category'),
        ),
    ]