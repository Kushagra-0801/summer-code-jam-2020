from django.db import models


class Topics(models.TextChoices):
    SCIENCE = "science"
    POLITICS = "politics"


class Languages(models.TextChoices):
    ENGLISH = "en"
    HINDI = "hi"


class Country(models.TextChoices):
    INDIA = "IN"
    UNITED_STATES_OF_AMERICA = "US"
    UNITED_KINGDOMS = "UK"


class Article(models.Model):
    """Article gotten from the News Catcher API"""

    _id = models.UUIDField(
        primary_key=True,
        help_text="Newscatcher API's unique identifier for each news article",
    )
    summary = models.TextField(help_text="Summary of the article")
    country = models.CharField(
        choices=Country.choices, help_text="Country of the publisher"
    )
    clean_url = models.URLField(help_text="URL of the article's source")
    author = models.TextField(help_text="Author of the article")
    rights = models.TextField("Copyright")
    link = models.URLField(help_text="Full URL of the article")
    rank = models.PositiveSmallIntegerField(help_text="Rank of the source website")
    topic = models.CharField(choices=Topics.choices, help_text="Topic of the article")
    language = models.CharField(
        choices=Languages.choices, help_text="Language of the article"
    )
    title = models.TextField(help_text="Title of the article")
    published_date = models.DateTimeField(help_text="Published date & time")
