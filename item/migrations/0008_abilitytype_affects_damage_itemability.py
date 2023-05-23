# Generated by Django 4.2 on 2023-05-21 19:22

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_alter_item_bonus'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbilityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Affects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Damage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemAbility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300, null=True)),
                ('cooldown', models.CharField(max_length=100, null=True)),
                ('manacost', models.CharField(max_length=100, null=True)),
                ('details', jsonfield.fields.JSONField(blank=True, null=True)),
                ('ability_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.abilitytype')),
                ('affects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.affects')),
                ('damage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.damage')),
            ],
        ),
    ]
