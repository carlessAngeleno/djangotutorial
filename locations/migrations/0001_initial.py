# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vehicle'
        db.create_table(u'locations_vehicle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seconds_since_report', self.gf('django.db.models.fields.IntegerField')()),
            ('run_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6)),
            ('heading', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=1)),
            ('route_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('predictable', self.gf('django.db.models.fields.BooleanField')()),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6)),
            ('vehicle_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'locations', ['Vehicle'])


    def backwards(self, orm):
        # Deleting model 'Vehicle'
        db.delete_table(u'locations_vehicle')


    models = {
        u'locations.vehicle': {
            'Meta': {'object_name': 'Vehicle'},
            'heading': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'predictable': ('django.db.models.fields.BooleanField', [], {}),
            'route_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'run_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'seconds_since_report': ('django.db.models.fields.IntegerField', [], {}),
            'vehicle_id': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['locations']