# Generated by Django 2.2.5 on 2019-10-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_auto_20191009_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_price', models.CharField(default=0.0, max_length=50)),
                ('hosted_by', models.CharField(default='', max_length=45)),
                ('bidder', models.CharField(default='', max_length=45)),
                ('bid_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='auction',
            name='new_price',
        ),
    ]
