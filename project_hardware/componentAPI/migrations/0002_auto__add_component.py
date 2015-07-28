# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Component'
        db.create_table(u'componentAPI_component', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compId', self.gf('django.db.models.fields.IntegerField')()),
            ('compName', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'componentAPI', ['Component'])


    def backwards(self, orm):
        # Deleting model 'Component'
        db.delete_table(u'componentAPI_component')


    models = {
        u'componentAPI.component': {
            'Meta': {'object_name': 'Component'},
            'compId': ('django.db.models.fields.IntegerField', [], {}),
            'compName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['componentAPI']