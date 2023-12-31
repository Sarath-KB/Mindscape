# Generated by Django 4.2.1 on 2023-06-08 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0015_tbl_feedback'),
        ('Guest', '0004_tbl_newhospital'),
        ('User', '0006_delete_tbl_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_rescueinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_emergencyrequest')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_newhospital')),
                ('rescue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_rescueteam')),
            ],
        ),
    ]
