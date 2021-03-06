# Generated by Django 4.0.5 on 2022-07-05 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rh', '0008_remove_funcionario_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='sexo',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rh.departamento'),
        ),
    ]
