from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from enums.enums import SKILL_TYPE_CHOICES

# id: int
# skill: Skill
# level: int


class SkillLevel(models.Model):
    id = models.AutoField(primary_key=True)
    skill = models.ForeignKey("Skill", on_delete=models.CASCADE)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.skill.name + " - " + str(self.level)


# id: int
# name: str
# skill_type: enum = Programming Language | Library | Database | Deployment | Cloud | Framework | Information Systems | Low-Code | No-Code | Office Software
# image: Image


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=100, choices=SKILL_TYPE_CHOICES)
    image = models.ImageField(upload_to="skill/images/", null=True, blank=True)

    def __str__(self):
        return self.name

    # Save the skill and create the 5 skill levels for it
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for level in range(1, 6):
            SkillLevel.objects.get_or_create(skill=self, level=level)
