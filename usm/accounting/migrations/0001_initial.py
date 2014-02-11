# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'accounting_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('society', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Society'], unique=True)),
        ))
        db.send_create_signal(u'accounting', ['Account'])

        # Adding model 'Log'
        db.create_table(u'accounting_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('ammount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'accounting', ['Log'])

        # Adding model 'TransactionCategory'
        db.create_table(u'accounting_transactioncategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'accounting', ['TransactionCategory'])

        # Adding model 'TransactionMethod'
        db.create_table(u'accounting_transactionmethod', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'accounting', ['TransactionMethod'])

        # Adding model 'Transaction'
        db.create_table(u'accounting_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.Account'])),
            ('transaction_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.TransactionCategory'])),
            ('transaction_method', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.TransactionMethod'])),
            ('ammount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('submit_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('bank_reconlliation_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'accounting', ['Transaction'])

        # Adding M2M table for field logs on 'Transaction'
        m2m_table_name = db.shorten_name(u'accounting_transaction_logs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('transaction', models.ForeignKey(orm[u'accounting.transaction'], null=False)),
            ('log', models.ForeignKey(orm[u'accounting.log'], null=False))
        ))
        db.create_unique(m2m_table_name, ['transaction_id', 'log_id'])

        # Adding model 'Bill'
        db.create_table(u'accounting_bill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.Account'])),
            ('ammount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('biller', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'accounting', ['Bill'])

        # Adding M2M table for field logs on 'Bill'
        m2m_table_name = db.shorten_name(u'accounting_bill_logs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bill', models.ForeignKey(orm[u'accounting.bill'], null=False)),
            ('log', models.ForeignKey(orm[u'accounting.log'], null=False))
        ))
        db.create_unique(m2m_table_name, ['bill_id', 'log_id'])

        # Adding model 'Invoice'
        db.create_table(u'accounting_invoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.Account'])),
            ('ammount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('invoicee', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'accounting', ['Invoice'])

        # Adding M2M table for field logs on 'Invoice'
        m2m_table_name = db.shorten_name(u'accounting_invoice_logs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('invoice', models.ForeignKey(orm[u'accounting.invoice'], null=False)),
            ('log', models.ForeignKey(orm[u'accounting.log'], null=False))
        ))
        db.create_unique(m2m_table_name, ['invoice_id', 'log_id'])

        # Adding model 'Grant'
        db.create_table(u'accounting_grant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.Account'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ammount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'accounting', ['Grant'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table(u'accounting_account')

        # Deleting model 'Log'
        db.delete_table(u'accounting_log')

        # Deleting model 'TransactionCategory'
        db.delete_table(u'accounting_transactioncategory')

        # Deleting model 'TransactionMethod'
        db.delete_table(u'accounting_transactionmethod')

        # Deleting model 'Transaction'
        db.delete_table(u'accounting_transaction')

        # Removing M2M table for field logs on 'Transaction'
        db.delete_table(db.shorten_name(u'accounting_transaction_logs'))

        # Deleting model 'Bill'
        db.delete_table(u'accounting_bill')

        # Removing M2M table for field logs on 'Bill'
        db.delete_table(db.shorten_name(u'accounting_bill_logs'))

        # Deleting model 'Invoice'
        db.delete_table(u'accounting_invoice')

        # Removing M2M table for field logs on 'Invoice'
        db.delete_table(db.shorten_name(u'accounting_invoice_logs'))

        # Deleting model 'Grant'
        db.delete_table(u'accounting_grant')


    models = {
        u'accounting.account': {
            'Meta': {'object_name': 'Account'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'society': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Society']", 'unique': 'True'})
        },
        u'accounting.bill': {
            'Meta': {'object_name': 'Bill'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.Account']"}),
            'ammount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'biller': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounting.Log']", 'symmetrical': 'False'})
        },
        u'accounting.grant': {
            'Meta': {'object_name': 'Grant'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.Account']"}),
            'ammount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'accounting.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.Account']"}),
            'ammount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoicee': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'logs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounting.Log']", 'symmetrical': 'False'})
        },
        u'accounting.log': {
            'Meta': {'object_name': 'Log'},
            'ammount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'accounting.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.Account']"}),
            'ammount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'bank_reconlliation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounting.Log']", 'symmetrical': 'False'}),
            'submit_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'transaction_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.TransactionCategory']"}),
            'transaction_method': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.TransactionMethod']"})
        },
        u'accounting.transactioncategory': {
            'Meta': {'object_name': 'TransactionCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'accounting.transactionmethod': {
            'Meta': {'object_name': 'TransactionMethod'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
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
        }
    }

    complete_apps = ['accounting']