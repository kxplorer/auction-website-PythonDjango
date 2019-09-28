# Generated by Django 2.2.5 on 2019-09-25 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('deadline_date', models.DateTimeField()),
                ('status', models.CharField(default='Active', max_length=500)),
            ],
        ),
    ]
