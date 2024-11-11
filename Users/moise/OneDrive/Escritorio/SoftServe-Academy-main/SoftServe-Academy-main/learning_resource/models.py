from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from skill.models import SkillLevel

# from user.models import User
from enums.enums import MEDIA_TYPE_CHOICES, CONTENT_TYPE_CHOICES, LANGUAGE_CHOICES

# id: int
# rate: int
# created_at: datetime
# comment: str
# user: User


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)

    def __str__(self):
        return (
            self.user.name
            + " - "
            + str(self.rate)
            + " - "
            + self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        )

    def rate_range(self):
        return range(self.rate)


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
# (UNUSED) content_manager: ContentManager
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
    learning_skills = models.ManyToManyField(
        SkillLevel, related_name="learning_resources_learning"
    )
    required_skills = models.ManyToManyField(
        SkillLevel, related_name="learning_resources_required", blank=True
    )
    reviews = models.ManyToManyField(
        "Review", related_name="learning_resources_review", blank=True
    )

    def __str__(self):
        return f"{self.name} ({self.language.upper()}) ({self.media_type})"

    def save(self, *args, **kwargs):
        # Filter learning_skills and required_skills to keep only the highest level of each skill
        if self.pk:  # Ensure this is not a new instance
            self.learning_skills.set(
                self._get_highest_levels(self.learning_skills.all())
            )
            self.required_skills.set(
                self._get_highest_levels(self.required_skills.all())
            )
        super().save(*args, **kwargs)

    def _get_highest_levels(self, skills):
        highest_levels = {}
        for skill in skills:
            if (
                skill.skill not in highest_levels
                or skill.level > highest_levels[skill.skill].level
            ):
                highest_levels[skill.skill] = skill
        return highest_levels.values()
