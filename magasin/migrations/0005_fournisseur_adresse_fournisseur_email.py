# Generated by Django 4.1.7 on 2023-03-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0004_fournisseur_produit_fournisseur'),
    ]

    operations = [
        migrations.AddField(
            model_name='fournisseur',
            name='adresse',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]