# -*- coding:utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0034_auto_20220401_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatedcertificate',
            name='document_number',
            field=models.CharField(blank=True, default=b'', max_length=30),
        ),
    ]