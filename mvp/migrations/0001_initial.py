# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table('mvp_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('mvp', ['Student'])

        # Adding model 'Oracle'
        db.create_table('mvp_oracle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('mvp', ['Oracle'])

        # Adding model 'Group'
        db.create_table('mvp_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('oracle', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mvp.Oracle'], unique=True, null=True)),
        ))
        db.send_create_signal('mvp', ['Group'])

        # Adding M2M table for field tags on 'Group'
        db.create_table('mvp_group_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['mvp.group'], null=False)),
            ('tag', models.ForeignKey(orm['mvp.tag'], null=False))
        ))
        db.create_unique('mvp_group_tags', ['group_id', 'tag_id'])

        # Adding M2M table for field students on 'Group'
        db.create_table('mvp_group_students', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['mvp.group'], null=False)),
            ('student', models.ForeignKey(orm['mvp.student'], null=False))
        ))
        db.create_unique('mvp_group_students', ['group_id', 'student_id'])

        # Adding model 'Tag'
        db.create_table('mvp_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True, null=True)),
        ))
        db.send_create_signal('mvp', ['Tag'])

        # Adding model 'Wish'
        db.create_table('mvp_wish', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mvp.Student'], null=True)),
        ))
        db.send_create_signal('mvp', ['Wish'])

        # Adding M2M table for field tags on 'Wish'
        db.create_table('mvp_wish_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('wish', models.ForeignKey(orm['mvp.wish'], null=False)),
            ('tag', models.ForeignKey(orm['mvp.tag'], null=False))
        ))
        db.create_unique('mvp_wish_tags', ['wish_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table('mvp_student')

        # Deleting model 'Oracle'
        db.delete_table('mvp_oracle')

        # Deleting model 'Group'
        db.delete_table('mvp_group')

        # Removing M2M table for field tags on 'Group'
        db.delete_table('mvp_group_tags')

        # Removing M2M table for field students on 'Group'
        db.delete_table('mvp_group_students')

        # Deleting model 'Tag'
        db.delete_table('mvp_tag')

        # Deleting model 'Wish'
        db.delete_table('mvp_wish')

        # Removing M2M table for field tags on 'Wish'
        db.delete_table('mvp_wish_tags')


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
        'mvp.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oracle': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mvp.Oracle']", 'unique': 'True', 'null': 'True'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mvp.Student']", 'null': 'True', 'symmetrical': 'False'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mvp.Tag']", 'symmetrical': 'False'})
        },
        'mvp.oracle': {
            'Meta': {'object_name': 'Oracle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mvp.student': {
            'Meta': {'object_name': 'Student'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'mvp.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'mvp.wish': {
            'Meta': {'object_name': 'Wish'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mvp.Student']", 'null': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mvp.Tag']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['mvp']