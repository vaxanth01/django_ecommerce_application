# Generated by Django 5.0.2 on 2024-04-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_userprofile_billing_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address_line',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='alter_number',
            field=models.IntegerField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.IntegerField(default=0, max_length=15),
        ),
    ]
