# Generated by Django 4.0.8 on 2022-12-20 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publicaciones', '0006_rename_fecha_comentario_fecha_agregado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='name',
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to=settings.AUTH_USER_MODEL),
        ),
    ]
