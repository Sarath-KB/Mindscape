# Generated by Django 4.2 on 2023-05-04 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_tbl_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='tbl_category',
        ),
        migrations.DeleteModel(
            name='tbl_subcategory',
        ),
    ]