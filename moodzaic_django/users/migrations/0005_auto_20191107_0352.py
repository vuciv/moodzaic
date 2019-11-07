# Generated by Django 2.2.6 on 2019-11-07 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191107_0256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mood',
            name='date',
        ),
        migrations.AddField(
            model_name='observation',
            name='mood1',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Mood'),
        ),
        migrations.AddField(
            model_name='observation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
        migrations.AlterField(
            model_name='mood',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='observation',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='date observed'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(default='', max_length=9),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]
