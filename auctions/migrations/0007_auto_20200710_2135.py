# Generated by Django 3.0.3 on 2020-07-10 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20200710_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='listingState',
            new_name='active',
        ),
    ]