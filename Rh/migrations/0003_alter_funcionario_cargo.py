# Generated by Django 4.0.5 on 2022-06-30 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rh', '0002_alter_funcionario_cargo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.CharField(choices=[('ES', 'Estagiário'), ('AS', 'Assistente'), ('JR', 'Junior'), ('PL', 'Pleno'), ('SR', 'Sênior'), ('GR', 'Gerente'), ('CEO', 'Presidente')], max_length=3),
        ),
    ]
