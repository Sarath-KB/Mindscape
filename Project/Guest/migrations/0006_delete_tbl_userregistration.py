# Generated by Django 4.2.1 on 2023-06-22 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_remove_lchat_from_lid_remove_lchat_from_user1_and_more'),
        ('Admin', '0016_delete_tbl_feedback'),
        ('Guest', '0005_tbl_unknownemergency'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_userregistration',
        ),
    ]