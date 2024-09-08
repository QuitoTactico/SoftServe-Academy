from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from enums.enums import SKILL_TYPE_CHOICES

# id: int
# name: str
# skill_type: enum = Programming Language | Library | Database | Deployment | Cloud | Framework | Information Systems | Low-Code | No-Code | Office Software
# image: Image

class Skill(models.Model):
    name = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=100, choices=SKILL_TYPE_CHOICES)
    image = models.ImageField(upload_to='skill/images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
# id: int
# skill: Skill
# level: int

class SkillLevel(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.skill.name + ' - ' + str(self.level)