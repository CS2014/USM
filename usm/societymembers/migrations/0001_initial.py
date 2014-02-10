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
        ))
        db.send_create_signal(u'societymembers', ['Tag'])

        # Adding model 'SocietyMember'
        db.create_table(u'societymembers_societymember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
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
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['societymembers.Tag']", 'symmetrical': 'False'})
        },
        u'societymembers.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['societymembers']