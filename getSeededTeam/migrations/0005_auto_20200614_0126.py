# Generated by Django 3.0.7 on 2020-06-14 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getSeededTeam', '0004_auto_20200612_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='category',
            field=models.CharField(choices=[('Technology', 'Technology'), ('General', 'General'), ('Society', 'Society')], max_length=10),
        ),
    ]