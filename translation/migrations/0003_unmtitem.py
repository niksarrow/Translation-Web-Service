# Generated by Django 3.0.7 on 2020-06-12 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0002_todoitem_gen'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnmtItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('gen', models.TextField()),
            ],
        ),
    ]