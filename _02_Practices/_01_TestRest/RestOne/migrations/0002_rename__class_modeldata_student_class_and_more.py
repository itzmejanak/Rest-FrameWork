# Generated by Django 5.0.6 on 2024-07-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestOne', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modeldata',
            old_name='_class',
            new_name='student_class',
        ),
        migrations.AlterField(
            model_name='modeldata',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modeldata',
            name='roll_no',
            field=models.IntegerField(),
        ),
    ]
