# Generated by Django 3.0.7 on 2020-06-12 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getSeededTeam', '0002_candidate_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
