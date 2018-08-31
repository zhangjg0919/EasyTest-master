# Generated by Django 2.0.5 on 2018-08-31 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('case_id', models.AutoField(primary_key=True, serialize=False)),
                ('case_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('env_id', models.AutoField(primary_key=True, serialize=False)),
                ('env_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('private_key', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('if_id', models.AutoField(primary_key=True, serialize=False)),
                ('if_name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
                ('method', models.CharField(max_length=4)),
                ('data_type', models.CharField(max_length=4)),
                ('is_sign', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('request_header_param', models.TextField()),
                ('request_body_param', models.TextField()),
                ('response_header_param', models.TextField()),
                ('response_body_param', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('plan_id', models.AutoField(primary_key=True, serialize=False)),
                ('plan_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Environment')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('prj_id', models.AutoField(primary_key=True, serialize=False)),
                ('prj_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('report_name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('case_num', models.IntegerField(null=True)),
                ('pass_num', models.IntegerField(null=True)),
                ('fail_num', models.IntegerField(null=True)),
                ('error_num', models.IntegerField(null=True)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Plan')),
            ],
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('sign_id', models.AutoField(primary_key=True, serialize=False)),
                ('sign_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='sign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Sign'),
        ),
        migrations.AddField(
            model_name='plan',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Project'),
        ),
        migrations.AddField(
            model_name='interface',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Project'),
        ),
        migrations.AddField(
            model_name='environment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Project'),
        ),
        migrations.AddField(
            model_name='case',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Project'),
        ),
    ]
