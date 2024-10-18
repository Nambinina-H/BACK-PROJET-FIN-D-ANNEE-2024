# Generated by Django 4.2.16 on 2024-10-18 01:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_utilisateur', '0004_etudiant_niveau'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommandation', models.TextField()),
                ('date_recommendation', models.DateTimeField(default=django.utils.timezone.now)),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_utilisateur.enseignant')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_utilisateur.responsablepedagogique')),
            ],
        ),
    ]