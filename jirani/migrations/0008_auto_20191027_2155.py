# Generated by Django 2.2.6 on 2019-10-27 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jirani', '0007_auto_20191027_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jirani.Neighbourhood'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jirani.Neighbourhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
