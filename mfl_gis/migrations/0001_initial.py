# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
import common.models.base
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facilities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstituencyBoundary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(max_length=100)),
                ('area', models.IntegerField()),
                ('pop2005', models.IntegerField(verbose_name=b'Population 2005')),
                ('fips', models.CharField(max_length=2, verbose_name=b'FIPS Code')),
                ('iso2', models.CharField(max_length=2, verbose_name=b'2 Digit ISO')),
                ('iso3', models.CharField(max_length=3, verbose_name=b'3 Digit ISO')),
                ('un', models.IntegerField(verbose_name=b'United Nations Code')),
                ('region', models.IntegerField(verbose_name=b'Region Code')),
                ('subregion', models.IntegerField(verbose_name=b'Sub-Region Code')),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('constituency', models.OneToOneField(to='common.Constituency')),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
                'verbose_name_plural': 'constituency boundaries',
            },
        ),
        migrations.CreateModel(
            name='CountyBoundary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(max_length=100)),
                ('area', models.IntegerField()),
                ('pop2005', models.IntegerField(verbose_name=b'Population 2005')),
                ('fips', models.CharField(max_length=2, verbose_name=b'FIPS Code')),
                ('iso2', models.CharField(max_length=2, verbose_name=b'2 Digit ISO')),
                ('iso3', models.CharField(max_length=3, verbose_name=b'3 Digit ISO')),
                ('un', models.IntegerField(verbose_name=b'United Nations Code')),
                ('region', models.IntegerField(verbose_name=b'Region Code')),
                ('subregion', models.IntegerField(verbose_name=b'Sub-Region Code')),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('county', models.OneToOneField(to='common.County')),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
                'verbose_name_plural': 'county boundaries',
            },
        ),
        migrations.CreateModel(
            name='FacilityCoordinates',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('latitude', models.CharField(help_text=b'How far north or south a facility is from the equator', max_length=255)),
                ('longitude', models.CharField(help_text=b'How far east or west one a facility is from the Greenwich Meridian', max_length=255)),
                ('collection_date', models.DateTimeField()),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('facility', models.OneToOneField(to='facilities.Facility')),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
                'verbose_name': 'facility coordinates',
                'verbose_name_plural': 'facility coordinates',
            },
        ),
        migrations.CreateModel(
            name='GeoCodeMethod',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(help_text=b'The name of the method.', max_length=100)),
                ('description', models.TextField(help_text=b'A short description of the method', null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeoCodeSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(help_text=b'The name of the collecting organization', max_length=100)),
                ('description', models.TextField(help_text=b'A short summary of the collecting organization', null=True, blank=True)),
                ('abbreviation', models.CharField(help_text=b'An acronym of the collecting or e.g SAM', max_length=10)),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WardBoundary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(max_length=100)),
                ('area', models.IntegerField()),
                ('pop2005', models.IntegerField(verbose_name=b'Population 2005')),
                ('fips', models.CharField(max_length=2, verbose_name=b'FIPS Code')),
                ('iso2', models.CharField(max_length=2, verbose_name=b'2 Digit ISO')),
                ('iso3', models.CharField(max_length=3, verbose_name=b'3 Digit ISO')),
                ('un', models.IntegerField(verbose_name=b'United Nations Code')),
                ('region', models.IntegerField(verbose_name=b'Region Code')),
                ('subregion', models.IntegerField(verbose_name=b'Sub-Region Code')),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('ward', models.OneToOneField(to='common.Ward')),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
                'verbose_name_plural': 'ward boundaries',
            },
        ),
        migrations.CreateModel(
            name='WorldBorder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, help_text=b'Indicates whether the record has been retired?')),
                ('name', models.CharField(max_length=100)),
                ('area', models.IntegerField()),
                ('pop2005', models.IntegerField(verbose_name=b'Population 2005')),
                ('fips', models.CharField(max_length=2, verbose_name=b'FIPS Code')),
                ('iso2', models.CharField(max_length=2, verbose_name=b'2 Digit ISO')),
                ('iso3', models.CharField(max_length=3, verbose_name=b'3 Digit ISO')),
                ('un', models.IntegerField(verbose_name=b'United Nations Code')),
                ('region', models.IntegerField(verbose_name=b'Region Code')),
                ('subregion', models.IntegerField(verbose_name=b'Sub-Region Code')),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='facilitycoordinates',
            name='method',
            field=models.ForeignKey(help_text=b'Method used to obtain the geo codes. e.g taken with GPS device', to='mfl_gis.GeoCodeMethod'),
        ),
        migrations.AddField(
            model_name='facilitycoordinates',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mfl_gis.GeoCodeSource', help_text=b'where the geo code came from'),
        ),
        migrations.AddField(
            model_name='facilitycoordinates',
            name='updated_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.base.get_default_system_user_id, to=settings.AUTH_USER_MODEL),
        ),
    ]
