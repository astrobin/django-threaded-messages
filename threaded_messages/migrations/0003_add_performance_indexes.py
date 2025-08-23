# Generated manually for performance optimization
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threaded_messages', '0002_add_body_html'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='participant',
            index=models.Index(fields=['user', 'deleted_at'], name='participant_user_deleted'),
        ),
        migrations.AddIndex(
            model_name='participant',
            index=models.Index(fields=['user', 'read_at'], name='participant_user_read'),
        ),
        migrations.AddIndex(
            model_name='participant',
            index=models.Index(fields=['user', 'replied_at'], name='participant_user_replied'),
        ),
        migrations.AddIndex(
            model_name='participant',
            index=models.Index(fields=['thread', 'user'], name='participant_thread_user'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['sent_at'], name='message_sent_at'),
        ),
        migrations.AddIndex(
            model_name='thread',
            index=models.Index(fields=['latest_msg'], name='thread_latest_msg'),
        ),
    ]