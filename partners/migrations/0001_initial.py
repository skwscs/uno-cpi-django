# Generated by Django 2.1.1 on 2019-03-22 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_blogindexpage_blogpage_datadefinition_datadefinitiongroup_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampusPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('weitz_cec_part', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=False, max_length=6)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CampusPartnerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.CampusPartner')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('website_url', models.URLField(blank=True, max_length=300)),
                ('k12_level', models.CharField(blank=True, max_length=20)),
                ('address_line1', models.CharField(blank=True, max_length=1024)),
                ('address_line2', models.CharField(blank=True, max_length=1024)),
                ('county', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=25)),
                ('state', models.CharField(blank=True, max_length=15)),
                ('zip', models.CharField(blank=True, max_length=10)),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)),
                ('active', models.BooleanField(default=False)),
                ('weitz_cec_part', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=6)),
                ('legislative_district', models.IntegerField(blank=True, null=True)),
                ('median_household_income', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPartnerMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_type', models.CharField(choices=[('Primary', 'Primary'), ('Other', 'Other')], default=False, max_length=20)),
                ('community_partner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communitypartnermission', to='partners.CommunityPartner')),
                ('mission_area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mission_area', to='home.MissionArea')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPartnerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_partner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communitypartner', to='partners.CommunityPartner')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_type', models.CharField(max_length=50, verbose_name='Community Type')),
            ],
        ),
        migrations.AddField(
            model_name='communitypartner',
            name='community_type',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='partners.CommunityType', verbose_name='Community Type'),
        ),
    ]