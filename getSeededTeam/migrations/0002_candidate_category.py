# Generated by Django 3.0.7 on 2020-06-12 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getSeededTeam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='category',
            field=models.CharField(choices=[('N', 'None'), ('T', 'Technology'), ('G', 'General'), ('S', 'Society')], default='N', max_length=1),
        ),
    ]
