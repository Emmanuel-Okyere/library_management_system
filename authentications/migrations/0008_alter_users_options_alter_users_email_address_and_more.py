# Generated by Django 4.0.4 on 2022-06-02 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0007_remove_users_email_address_users_email_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ('email_address',)},
        ),
        migrations.AlterField(
            model_name='users',
            name='email_address',
            field=models.EmailField(blank=True, max_length=200, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]