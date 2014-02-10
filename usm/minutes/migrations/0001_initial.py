# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Meeting'
        db.create_table(u'minutes_meeting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'minutes', ['Meeting'])

        # Adding model 'Agenda'
        db.create_table(u'minutes_agenda', (
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('meeting', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['minutes.Meeting'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'minutes', ['Agenda'])

        # Adding M2M table for field log on 'Agenda'
        m2m_table_name = db.shorten_name(u'minutes_agenda_log')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('agenda', models.ForeignKey(orm[u'minutes.agenda'], null=False)),
            ('log', models.ForeignKey(orm[u'accounting.log'], null=False))
        ))
        db.create_unique(m2m_table_name, ['agenda_id', 'log_id'])

        # Adding model 'Minutes'
        db.create_table(u'minutes_minutes', (
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('meeting', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['minutes.Meeting'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'minutes', ['Minutes'])

        # Adding M2M table for field log on 'Minutes'
        m2m_table_name = db.shorten_name(u'minutes_minutes_log')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('minutes', models.ForeignKey(orm[u'minutes.minutes'], null=False)),
            ('log', models.ForeignKey(orm[u'accounting.log'], null=False))
        ))
        db.create_unique(m2m_table_name, ['minutes_id', 'log_id'])


    def backwards(self, orm):
        # Deleting model 'Meeting'
        db.delete_table(u'minutes_meeting')

        # Deleting model 'Agenda'
        db.delete_table(u'minutes_agenda')

        # Removing M2M table for field log on 'Agenda'
        db.delete_table(db.shorten_name(u'minutes_agenda_log'))

        # Deleting model 'Minutes'
        db.delete_table(u'minutes_minutes')

        # Removing M2M table for field log on 'Minutes'
        db.delete_table(db.shorten_name(u'minutes_minutes_log'))


    models = {
        u'accounting.log': {
            'Meta': {'object_name': 'Log'},
            'ammount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'minutes.agenda': {
            'Meta': {'object_name': 'Agenda'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'log': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounting.Log']", 'symmetrical': 'False'}),
            'meeting': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['minutes.Meeting']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'minutes.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'minutes.minutes': {
            'Meta': {'object_name': 'Minutes'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'log': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounting.Log']", 'symmetrical': 'False'}),
            'meeting': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['minutes.Meeting']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '10000'})
        }
    }

    complete_apps = ['minutes']