from django.db import migrations

def add_test_sentiment(apps, schema_editor):
    SentimentAnalysis = apps.get_model('sentiment', 'SentimentAnalysis')
    SentimentAnalysis.objects.create(
        text="Ce projet est génial !",
        sentiment="POSITIVE",
        author="Alice"
    )

class Migration(migrations.Migration):
    dependencies = [
        ('sentiment', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(add_test_sentiment),
    ]
