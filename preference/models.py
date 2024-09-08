from django.db import models
from django.core.validators import MinValueValidator
from enums.enums import MEDIA_TYPE_CHOICES, CONTENT_TYPE_CHOICES, LEARNING_TYPE_CHOICES

# id: int
# media_type: enum = Text | Video | Audio
# content_type: enum =  Guides | Documentation | Introduction | Summary | Article | Quiz | Podcast
# time_per_week: int
# time_per_session: int
# autodidact_or_guided: Bool

class Preference(models.Model):
    id = models.AutoField(primary_key=True)
    media_type = models.CharField(max_length=100, choices=MEDIA_TYPE_CHOICES)
    content_type = models.CharField(max_length=100, choices=CONTENT_TYPE_CHOICES)
    learning_type = models.CharField(max_length=100, choices=LEARNING_TYPE_CHOICES)
    time_per_week = models.IntegerField(validators=[MinValueValidator(1)])
    time_per_session = models.IntegerField(validators=[MinValueValidator(1)])
