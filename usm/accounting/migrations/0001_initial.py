# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Log'
        db.create_table('accounting_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('ammount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal('accounting', ['Log'])

        # Adding model 'TransactionCategory'
        db.create_table('accounting_transactioncategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('accounting', ['TransactionCategory'])

        # Adding model 'TransactionMethod'
        db.create_table('accounting_transactionmethod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('accounting', ['TransactionMethod'])

        # Adding model 'Transaction'
        db.create_table('accounting_transaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transaction_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.TransactionCategory'])),
            ('transaction_method', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.TransactionMethod'])),
            ('ammount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('submit_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('bank_reconlliation_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('accounting', ['Transaction'])

        # Adding M2M table for field logs on 'Transaction'
        m2m_table_name = db.shorten_name('accounting_transaction_logs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('transaction', models.ForeignKey(orm['accounting.transaction'], null=False)),
            ('log', models.ForeignKey(orm['accounting.log'], null=False))
        ))
        db.create_unique(m2m_table_name, ['transaction_id', 'log_id'])

        # Adding model 'Bill'
        db.create_table('accounting_bill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ammount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('biller', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('accounting', ['Bill'])

        # Adding M2M table for field logs on 'Bill'
        m2m_table_name = db.shorten_name('accounting_bill_logs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bill', models.ForeignKey(orm['accounting.bill'], null=False)),
            ('log', models.ForeignKey(orm['accounting.log'], null=False))
        ))
        db.create_unique(m2m_table_name, ['bill_id', 'log_id'])

        # Adding model 'Invoice'
        db.create_table('accounting_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ammount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('invoicee', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('accounting', ['Invoice'])

        # Adding M2M table for field logs on 'Invoice'
        m2m_table_name = db.shorten_name('accounting_invoice_logs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('invoice', models.ForeignKey(orm['accounting.invoice'], null=False)),
            ('log', models.ForeignKey(orm['accounting.log'], null=False))
        ))
        db.create_unique(m2m_table_name, ['invoice_id', 'log_id'])

        # Adding model 'Grant'
        db.create_table('accounting_grant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ammount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal('accounting', ['Grant'])


    def backwards(self, orm):
        # Deleting model 'Log'
        db.delete_table('accounting_log')

        # Deleting model 'TransactionCategory'
        db.delete_table('accounting_transactioncategory')

        # Deleting model 'TransactionMethod'
        db.delete_table('accounting_transactionmethod')

        # Deleting model 'Transaction'
        db.delete_table('accounting_transaction')

        # Removing M2M table for field logs on 'Transaction'
        db.delete_table(db.shorten_name('accounting_transaction_logs'))

        # Deleting model 'Bill'
        db.delete_table('accounting_bill')

        # Removing M2M table for field logs on 'Bill'
        db.delete_table(db.shorten_name('accounting_bill_logs'))

        # Deleting model 'Invoice'
        db.delete_table('accounting_invoice')

        # Removing M2M table for field logs on 'Invoice'
        db.delete_table(db.shorten_name('accounting_invoice_logs'))

        # Deleting model 'Grant'
        db.delete_table('accounting_grant')


    models = {
        'accounting.bill': {
            'Meta': {'object_name': 'Bill'},
            'ammount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'biller': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['accounting.Log']", 'symmetrical': 'False'})
        },
        'accounting.grant': {
            'Meta': {'object_name': 'Grant'},
            'ammount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'accounting.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'ammount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoicee': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'logs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['accounting.Log']", 'symmetrical': 'False'})
        },
        'accounting.log': {
            'Meta': {'object_name': 'Log'},
            'ammount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'accounting.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'ammount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'bank_reconlliation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['accounting.Log']", 'symmetrical': 'False'}),
            'submit_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'transaction_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounting.TransactionCategory']"}),
            'transaction_method': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounting.TransactionMethod']"})
        },
        'accounting.transactioncategory': {
            'Meta': {'object_name': 'TransactionCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'accounting.transactionmethod': {
            'Meta': {'object_name': 'TransactionMethod'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['accounting']