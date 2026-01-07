
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes_offered', '0005_alter_classes_offered_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes_offered',
            name='participants',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), default=list, size=None),
        ),
    ]
