# Generated by Django 4.2.3 on 2023-07-10 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0010_tbl_psychologistappointment_and_more'),
        ('Psychiatrist', '0006_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_prescription',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_psychiatristappointment'),
        ),
    ]
