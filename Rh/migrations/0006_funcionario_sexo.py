# Generated by Django 4.0.5 on 2022-07-04 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rh', '0005_alter_funcionario_departamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='sexo',
            field=models.CharField(choices=[('Fem', 'Feminino'), ('Mas', 'Masculino')], max_length=3, null=True),
        ),
    ]
