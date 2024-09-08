from django.db import models
from django.core.validators import MinValueValidator
from enums.enums import MEDIA_TYPE_CHOICES, CONTENT_TYPE_CHOICES, LEARNING_TYPE_CHOICES

# id: int
# mediaType: enum = Text | Video | Audio
# contentType: enum =  Guides | Documentation | Introduction | Summary | Article | Quiz | Podcast
# timePerWeek: int
# timePerSession: int
# autodidactOrGuided: Bool

class Preference(models.Model):
    mediaType = models.CharField(max_length=100, choices=MEDIA_TYPE_CHOICES)
    contentType = models.CharField(max_length=100, choices=CONTENT_TYPE_CHOICES)
    learningType = models.CharField(max_length=100, choices=LEARNING_TYPE_CHOICES)
    timePerWeek = models.IntegerField(validators=[MinValueValidator(1)])
    timePerSession = models.IntegerField(validators=[MinValueValidator(1)])
