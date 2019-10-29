# Generated by Django 2.2.6 on 2019-10-29 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jirani', '0011_auto_20191029_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jirani.Neighbourhood'),
        ),
        migrations.AlterField(
            model_name='updates',
            name='estate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jirani.Neighbourhood'),
        ),
    ]