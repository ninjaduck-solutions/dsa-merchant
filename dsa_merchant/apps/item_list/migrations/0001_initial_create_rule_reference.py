# Generated by Django 2.0.3 on 2018-03-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RuleReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The references full title.', max_length=200)),
                ('shorthand', models.CharField(help_text='The references common shorthand.', max_length=10)),
                ('edition', models.PositiveIntegerField(help_text='Number of the referenced edition')),
                ('year_published', models.PositiveIntegerField(help_text='Year in which this reference has been published.')),
            ],
            options={
                'ordering': ('title', 'year_published'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='rulereference',
            unique_together={('title', 'edition', 'year_published')},
        ),
    ]