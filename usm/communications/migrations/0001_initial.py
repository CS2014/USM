# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TextMessage'
        db.create_table(u'communications_textmessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('source_phone_number', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'communications', ['TextMessage'])

        # Adding model 'Email'
        db.create_table(u'communications_email', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('sending_address', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'communications', ['Email'])


    def backwards(self, orm):
        # Deleting model 'TextMessage'
        db.delete_table(u'communications_textmessage')

        # Deleting model 'Email'
        db.delete_table(u'communications_email')


    models = {
        u'communications.email': {
            'Meta': {'object_name': 'Email'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'sending_address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'communications.textmessage': {
            'Meta': {'object_name': 'TextMessage'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'source_phone_number': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['communications']