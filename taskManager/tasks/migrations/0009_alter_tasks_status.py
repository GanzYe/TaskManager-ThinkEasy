# Generated by Django 4.0.4 on 2022-05-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_alter_tasks_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[{'Fulfilled', 'unFUL'}, {'FUL', 'Unfulfilled'}], default='FUL', max_length=255),
        ),
    ]
