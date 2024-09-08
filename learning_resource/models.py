from django.db import models
from django.core.validators import MinValueValidator
from skill.models import SkillLevel
#from user.models import User
from enums.enums import MEDIA_TYPE_CHOICES, CONTENT_TYPE_CHOICES, LANGUAGE_CHOICES

# id: int
# rate: int
# created_at: datetime
# comment: str
# user: User

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    rate = models.IntegerField(validators=[MinValueValidator(1), MinValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + ' - ' + str(self.rate) + ' - ' + self.created_at.strftime('%Y-%m-%d %H:%M:%S')

# id: int
# name: str
# media_type: str
# content_type: str
# link: str
# details: str
# duration: int
# language: str
# original_platform: str
# original_author: str
# content_manager: ContentManager
# general_level: int
# learning_skills: resourceLearningSkill[]
# required_skills: resourceRequiredSkill[]
# reviews: Review[]

class LearningResource(models.Model):
    id = models.AutoField(primary_key=True)
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
    reviews = models.ManyToManyField('Review', related_name='learning_resources_review', blank=True)

    def __str__(self):
        return f'{self.name} ({self.language} {self.media_type})'