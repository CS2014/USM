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
            ('society', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Society'])),
            ('recipients', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['societymembers.SocietyMember'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('source_phone_number', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'communications', ['TextMessage'])

        # Adding model 'Email'
        db.create_table(u'communications_email', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('society', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Society'])),
            ('recipients', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['societymembers.SocietyMember'])),
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
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'communications.email': {
            'Meta': {'object_name': 'Email'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'recipients': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['societymembers.SocietyMember']"}),
            'sending_address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'society': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Society']"}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'communications.textmessage': {
            'Meta': {'object_name': 'TextMessage'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'recipients': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['societymembers.SocietyMember']"}),
            'society': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Society']"}),
            'source_phone_number': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.society': {
            'Meta': {'object_name': 'Society'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'societymembers.societymember': {
            'Meta': {'object_name': 'SocietyMember'},
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'society': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Society']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['societymembers.Tag']", 'symmetrical': 'False'})
        },
        u'societymembers.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'society': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Society']"})
        }
    }

    complete_apps = ['communications']