# Generated by Django 3.0.7 on 2020-06-12 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('venture', models.CharField(max_length=100)),
                ('details', models.TextField(blank=True, null=True)),
                ('votes', models.SmallIntegerField(default=0)),
            ],
        ),
    ]