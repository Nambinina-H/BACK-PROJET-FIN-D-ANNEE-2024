# Generated by Django 4.2.16 on 2024-10-12 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('pseudo', models.CharField(blank=True, max_length=255, null=True)),
                ('tel', models.CharField(blank=True, max_length=20, null=True)),
                ('matricule', models.CharField(max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('empreinte_digitale', models.BinaryField(blank=True, null=True)),
                ('type', models.CharField(choices=[('admin', 'Administrateur'), ('etudiant', 'Etudiant'), ('enseignant', 'Enseignant'), ('responsable', 'Responsable Pédagogique')], max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResponsablePedagogique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion_utilisateur.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carte_etudiant', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion_utilisateur.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=20)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion_utilisateur.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Administrateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion_utilisateur.utilisateur')),
            ],
        ),
    ]
