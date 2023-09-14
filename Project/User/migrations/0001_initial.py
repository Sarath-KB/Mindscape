# Generated by Django 4.2 on 2023-05-09 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0004_tbl_newhospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_emergencyrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000)),
                ('major', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_userregistration')),
            ],
        ),
    ]