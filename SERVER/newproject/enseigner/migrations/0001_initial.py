# Generated by Django 4.2.16 on 2024-10-18 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_utilisateur', '0004_etudiant_niveau'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enseigner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_utilisateur.enseignant')),
                ('etudiants', models.ManyToManyField(to='gestion_utilisateur.etudiant')),
            ],
        ),
    ]
