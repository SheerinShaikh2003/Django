# Generated by Django 4.2.5 on 2023-10-18 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_item_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('prod_ref', models.IntegerField(default=100)),
                ('item_name', models.CharField(max_length=200)),
                ('op_type', models.CharField(max_length=100)),
            ],
        ),
    ]
