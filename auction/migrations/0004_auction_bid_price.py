# Generated by Django 2.2.5 on 2019-10-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_auction_hosted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='bid_price',
            field=models.CharField(default=models.CharField(default=0.0, max_length=50), max_length=50),
        ),
    ]
