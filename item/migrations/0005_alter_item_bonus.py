# Generated by Django 4.2 on 2023-05-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_typespecific_alter_item_bonus_alter_item_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='bonus',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
