# Generated by Django 2.2.2 on 2019-06-13 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('TT', 'Tutorial'), ('ST', 'Short Talk'), ('LT', 'Long Talk')], max_length=2)),
                ('abstract', models.TextField()),
                ('description', models.TextField()),
                ('pre_requesite', models.TextField()),
                ('about_author', models.TextField()),
                ('website', models.URLField()),
                ('accepted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
