# Generated by Django 2.0.1 on 2018-02-09 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
        ('residue', '0001_initial'),
        ('signprot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignprotInteractions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaction_type', models.CharField(max_length=200)),
                ('gpcr_residue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpcr_residue', to='residue.Residue')),
                ('signprot_residue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signprot_residue', to='residue.Residue')),
                ('structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.Structure')),
            ],
        ),
    ]