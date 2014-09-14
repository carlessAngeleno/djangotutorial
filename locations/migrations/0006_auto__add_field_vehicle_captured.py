# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Vehicle.captured'
        db.add_column(u'locations_vehicle', 'captured',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 9, 13, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Vehicle.captured'
        db.delete_column(u'locations_vehicle', 'captured')


    models = {
        u'locations.route': {
            'Meta': {'object_name': 'Route'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route_id': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'locations.stop': {
            'Meta': {'object_name': 'Stop'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'routes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['locations.Route']", 'symmetrical': 'False'}),
            'stop_id': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'locations.vehicle': {
            'Meta': {'object_name': 'Vehicle'},
            'captured': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'heading': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'predictable': ('django.db.models.fields.BooleanField', [], {}),
            'route_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'run_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'seconds_since_report': ('django.db.models.fields.IntegerField', [], {}),
            'vehicle_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['locations']