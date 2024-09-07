from django.db import models
from enums.enums import SKILL_TYPE_CHOICES

# id: int
# name: str
# skillType: enum = Programming Language | Library | Database | Deployment | Cloud | Framework | Information Systems | Low-Code | No-Code | Office Software

class Skill(models.Model):
    name = models.CharField(max_length=100)
    skillType = models.CharField(max_length=100, choices=SKILL_TYPE_CHOICES)

    def __str__(self):
        return self.name