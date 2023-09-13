# Generated by Django 4.2.5 on 2023-09-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='for_user',
            field=models.CharField(default='xyz', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='prod_code',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_desc',
            field=models.CharField(default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque, reiciendis saepe accusantium fugiat illo reprehenderit quidoloribus molestiae recusandae? Recusandae ducimus accusamus et. Soluta asperiores rerum laboriosam ratione, rem sed.', max_length=500),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://cdn-icons-png.flaticon.com/512/1377/1377194.png', max_length=500),
        ),
    ]
