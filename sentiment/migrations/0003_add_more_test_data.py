from django.db import migrations

def add_more_sentiments(apps, schema_editor):
    SentimentAnalysis = apps.get_model('sentiment', 'SentimentAnalysis')
    SentimentAnalysis.objects.create(
        text="Je n'aime pas ce service.",
        sentiment="NEGATIVE",
        author="Bob"
    )
    SentimentAnalysis.objects.create(
        text="C'est correct, mais peut être amélioré.",
        sentiment="NEUTRAL",
        author="Charlie"
    )
    SentimentAnalysis.objects.create(
        text="Incroyable expérience, je recommande !",
        sentiment="POSITIVE",
        author="Diane"
    )

class Migration(migrations.Migration):
    dependencies = [
        ('sentiment', '0002_add_test_data'),
    ]
    operations = [
        migrations.RunPython(add_more_sentiments),
    ]
