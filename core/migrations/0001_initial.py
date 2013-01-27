# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'URL'
        db.create_table('core_url', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('indirizzo', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('percorso_su_disco', self.gf('django.db.models.fields.FilePathField')(path='/vagrant/projects/Qualita/media/uploaded/', max_length=100)),
        ))
        db.send_create_signal('core', ['URL'])

        # Adding model 'Interrogazione'
        db.create_table('core_interrogazione', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titolo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descrizione', self.gf('django.db.models.fields.TextField')(max_length=50)),
        ))
        db.send_create_signal('core', ['Interrogazione'])

        # Adding M2M table for field url on 'Interrogazione'
        db.create_table('core_interrogazione_url', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('interrogazione', models.ForeignKey(orm['core.interrogazione'], null=False)),
            ('url', models.ForeignKey(orm['core.url'], null=False))
        ))
        db.create_unique('core_interrogazione_url', ['interrogazione_id', 'url_id'])

        # Adding model 'Score'
        db.create_table('core_score', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rilevanza', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('fonte', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('leggibilita', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('stile', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('commento', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.URL'], null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('core', ['Score'])


    def backwards(self, orm):
        # Deleting model 'URL'
        db.delete_table('core_url')

        # Deleting model 'Interrogazione'
        db.delete_table('core_interrogazione')

        # Removing M2M table for field url on 'Interrogazione'
        db.delete_table('core_interrogazione_url')

        # Deleting model 'Score'
        db.delete_table('core_score')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.interrogazione': {
            'Meta': {'object_name': 'Interrogazione'},
            'descrizione': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.URL']", 'symmetrical': 'False'})
        },
        'core.score': {
            'Meta': {'object_name': 'Score'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'commento': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fonte': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leggibilita': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'rilevanza': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'stile': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'url': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.URL']", 'null': 'True', 'blank': 'True'})
        },
        'core.url': {
            'Meta': {'object_name': 'URL'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indirizzo': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'percorso_su_disco': ('django.db.models.fields.FilePathField', [], {'path': "'/vagrant/projects/Qualita/media/uploaded/'", 'max_length': '100'})
        }
    }

    complete_apps = ['core']