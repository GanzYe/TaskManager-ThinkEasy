# Generated by Django 4.0.4 on 2022-05-18 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_alter_tasks_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('unCOM', 'Uncompleted'), ('COM', 'Completed')], default='unCOM', max_length=255),
        ),
    ]
