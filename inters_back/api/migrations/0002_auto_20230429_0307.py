# Generated by Django 3.2.18 on 2023-04-28 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='District',
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'District', 'verbose_name_plural': 'Districts'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='streets',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=1, max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=15, max_length=5.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]