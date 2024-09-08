from django.db import models
from django.core.validators import MinValueValidator
from skill.models import SkillLevel
from enums.enums import MEDIA_TYPE_CHOICES, CONTENT_TYPE_CHOICES, LANGUAGE_CHOICES

# id: int
# name: string
# mediaType: enum
# contentType: enum
# link: string
# details: string
# duration: int
# language: enum
# originalPlatform: string
# originalAuthor: string
# contentManager: ContentManager
# generalLevel: int
# learningSkills: resourceLearningSkill[]
# requiredSkills: resourceRequiredSkill[] 
# reviews: Review[]

class LearningResource(models.Model):
    name = models.CharField(max_length=100)
    media_type = models.CharField(max_length=100, choices=MEDIA_TYPE_CHOICES)
    content_type = models.CharField(max_length=100, choices=CONTENT_TYPE_CHOICES)
    link = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    duration = models.IntegerField(validators=[MinValueValidator(1)])
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    original_platform = models.CharField(max_length=100, blank=True)
    original_author = models.CharField(max_length=100, blank=True)
    # content_manager = models.ForeignKey(ContentManager, on_delete=models.CASCADE)
    general_level = models.IntegerField(validators=[MinValueValidator(1)])
    learning_skills = models.ManyToManyField(SkillLevel, related_name='learning_resources_learning')
    required_skills = models.ManyToManyField(SkillLevel, related_name='learning_resources_required', blank=True)
    # reviews = models.ManyToManyField(Review, related_name='learning_resources')

    def __str__(self):
        return self.name