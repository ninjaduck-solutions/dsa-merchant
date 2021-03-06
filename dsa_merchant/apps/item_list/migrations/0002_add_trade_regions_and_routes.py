# Generated by Django 2.0.3 on 2018-03-11 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item_list', '0001_initial_create_rule_reference'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('shorthand', models.CharField(max_length=10, unique=True)),
                ('danger_level_spring', models.PositiveIntegerField(default=0, help_text='The danger level during spring.')),
                ('danger_level_summer', models.PositiveIntegerField(default=0, help_text='The danger level during summer.')),
                ('danger_level_autumn', models.PositiveIntegerField(default=0, help_text='The danger level during autumn.')),
                ('danger_level_winter', models.PositiveIntegerField(default=0, help_text='The danger level during winter.')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TradeRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sea_route', models.BooleanField(default=False)),
                ('point_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_routes_point_a', to='item_list.TradeRegion')),
                ('point_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_routes_point_b', to='item_list.TradeRegion')),
            ],
            options={
                'ordering': ('point_a', 'is_sea_route'),
            },
        ),
        migrations.AddField(
            model_name='traderegion',
            name='trade_routes',
            field=models.ManyToManyField(through='item_list.TradeRoute', to='item_list.TradeRegion'),
        ),
        migrations.AlterUniqueTogether(
            name='traderoute',
            unique_together={('point_a', 'point_b')},
        ),
    ]
