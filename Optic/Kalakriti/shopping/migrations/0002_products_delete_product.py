# Generated by Django 4.2.7 on 2023-12-01 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(db_column='Product_id', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=60)),
                ('description', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('image', models.ImageField(upload_to='uploads/products/')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
