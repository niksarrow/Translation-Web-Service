# Generated by Django 3.0.7 on 2020-12-26 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0003_unmtitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='DCItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('gen', models.TextField()),
            ],
        ),
    ]