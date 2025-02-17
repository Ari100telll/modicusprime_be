# Generated by Django 5.1.6 on 2025-02-17 10:25

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('users', '0002_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInstancePermission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_transition_allowed', models.BooleanField(default=False)),
                ('is_edit_allowed', models.BooleanField(default=False)),
                ('object_id', models.UUIDField(blank=True, db_index=True, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_instance_permissions', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_instance_permissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Permission',
                'verbose_name_plural': 'User Permissions',
                'db_table': 'user_permission',
            },
        ),
    ]
