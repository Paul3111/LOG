# Generated by Django 3.2.6 on 2021-08-29 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_remove_entry_date_added2'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='topic_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='topic', to='learning_logs.topic'),
            preserve_default=False,
        ),
    ]
