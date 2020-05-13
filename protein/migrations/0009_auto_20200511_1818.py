# Generated by Django 3.0.4 on 2020-05-11 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protein', '0008_auto_20200422_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proteingproteinpair',
            name='log_ec50_dnorm',
        ),
        migrations.RemoveField(
            model_name='proteingproteinpair',
            name='log_ec50_mean',
        ),
        migrations.RemoveField(
            model_name='proteingproteinpair',
            name='log_ec50_sem',
        ),
        migrations.AddField(
            model_name='proteingproteinpair',
            name='pec50_dnorm',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proteingproteinpair',
            name='pec50_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proteingproteinpair',
            name='pec50_sem',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proteingproteinpair',
            name='emax_dnorm',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proteingproteinpair',
            name='emax_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proteingproteinpair',
            name='emax_sem',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proteingproteinpair',
            name='log_rai_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proteingproteinpair',
            name='log_rai_sem',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
