# Generated by Django 3.1.3 on 2020-12-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20201211_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_profile_friends_+', to='User.Profile', verbose_name='Amigos'),
        ),
    ]