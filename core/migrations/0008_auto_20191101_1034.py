# Generated by Django 2.2.6 on 2019-11-01 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_student_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subject_test',
            field=models.CharField(max_length=20),
        ),
    ]
