# Generated manually to add body_html field to Message model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threaded_messages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='body_html',
            field=models.TextField(blank=True, null=True, verbose_name='body HTML'),
        ),
    ]