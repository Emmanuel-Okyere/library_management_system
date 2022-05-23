# Generated by Django 4.0.4 on 2022-05-21 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogue', '0005_alter_category_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.BooleanField(default=True)),
                ('approval', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_to_request', to='catalogue.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_book', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('approval',),
            },
        ),
    ]
