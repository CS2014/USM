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
            ('society', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Society'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'minutes', ['Meeting'])

        # Adding M2M table for field society_members on 'Meeting'
        m2m_table_name = db.shorten_name(u'minutes_meeting_society_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('meeting', models.ForeignKey(orm[u'minutes.meeting'], null=False)),
            ('societymember', models.ForeignKey(orm[u'societymembers.societymember'], null=False))
        ))
        db.create_unique(m2m_table_name, ['meeting_id', 'societymember_id'])

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
            ('society', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Society'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('meeting', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['minutes.Meeting'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'minutes', ['Minutes'])

        # Adding M2M table for field attendence on 'Minutes'
        m2m_table_name = db.shorten_name(u'minutes_minutes_attendence')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('minutes', models.ForeignKey(orm[u'minutes.minutes'], null=False)),
            ('societymember', models.ForeignKey(orm[u'societymembers.societymember'], null=False))
        ))
        db.create_unique(m2m_table_name, ['minutes_id', 'societymember_id'])

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

        # Removing M2M table for field society_members on 'Meeting'
        db.delete_table(db.shorten_name(u'minutes_meeting_society_members'))

        # Deleting model 'Agenda'
        db.delete_table(u'minutes_agenda')

        # Removing M2M table for field log on 'Agenda'
        db.delete_table(db.shorten_name(u'minutes_agenda_log'))

        # Deleting model 'Minutes'
        db.delete_table(u'minutes_minutes')

        # Removing M2M table for field attendence on 'Minutes'
        db.delete_table(db.shorten_name(u'minutes_minutes_attendence'))

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
            'society': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Society']"}),
            'society_members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['societymembers.SocietyMember']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'minutes.minutes': {
            'Meta': {'object_name': 'Minutes'},
            'attendence': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['societymembers.SocietyMember']", 'symmetrical': 'False'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'log': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounting.Log']", 'symmetrical': 'False'}),
            'meeting': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['minutes.Meeting']", 'unique': 'True', 'primary_key': 'True'}),
            'society': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Society']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '10000'})
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

    complete_apps = ['minutes']