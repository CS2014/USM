# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'societymembers_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('society', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Society'])),
        ))
        db.send_create_signal(u'societymembers', ['Tag'])

        # Adding model 'SocietyMember'
        db.create_table(u'societymembers_societymember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('society', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Society'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('email_address', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('join_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'societymembers', ['SocietyMember'])

        # Adding M2M table for field tags on 'SocietyMember'
        m2m_table_name = db.shorten_name(u'societymembers_societymember_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('societymember', models.ForeignKey(orm[u'societymembers.societymember'], null=False)),
            ('tag', models.ForeignKey(orm[u'societymembers.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['societymember_id', 'tag_id'])

        # Adding model 'MembershipFee'
        db.create_table(u'societymembers_membershipfee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('society_member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['societymembers.SocietyMember'])),
            ('date_paid', self.gf('django.db.models.fields.DateTimeField')()),
            ('expiration_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('ammount', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal(u'societymembers', ['MembershipFee'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'societymembers_tag')

        # Deleting model 'SocietyMember'
        db.delete_table(u'societymembers_societymember')

        # Removing M2M table for field tags on 'SocietyMember'
        db.delete_table(db.shorten_name(u'societymembers_societymember_tags'))

        # Deleting model 'MembershipFee'
        db.delete_table(u'societymembers_membershipfee')


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
        u'societymembers.membershipfee': {
            'Meta': {'object_name': 'MembershipFee'},
            'ammount': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'date_paid': ('django.db.models.fields.DateTimeField', [], {}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'society_member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['societymembers.SocietyMember']"})
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

    complete_apps = ['societymembers']