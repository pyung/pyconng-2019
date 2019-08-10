# Generated by Django 2.2.2 on 2019-06-15 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0003_proposal_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='audience',
            field=models.CharField(choices=[('TT', 'Tutorial'), ('ST', 'Short Talk'), ('LT', 'Long Talk')], default='A', help_text='Who are your target audience?', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proposal',
            name='about_author',
            field=models.TextField(help_text='Let us know a little more about you'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='abstract',
            field=models.TextField(help_text='a summary on why this talk is neccessary'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='category',
            field=models.CharField(choices=[('TT', 'Tutorial'), ('ST', 'Short Talk'), ('LT', 'Long Talk')], help_text='Where does your talk fit in?', max_length=2),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='description',
            field=models.TextField(help_text='content of your talk as to be shown to the public'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='pre_requesite',
            field=models.TextField(help_text='what are the pre-requisites for this talk?'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='title',
            field=models.CharField(help_text='a short title of your talk', max_length=250),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='website',
            field=models.URLField(help_text='have a link to your personal website/blog?'),
        ),
    ]