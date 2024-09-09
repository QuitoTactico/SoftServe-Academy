from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from skill.models import SkillLevel
from learning_resource.models import LearningResource

# id: int
# index: int
# level: int
# LearningRoute: LearningRoute
# learning_resource: LearningResource
# completed: bool
# time_spent: int

class LearningRouteResource(models.Model):
    id = models.AutoField(primary_key=True)
    index = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    learning_resource = models.ForeignKey(LearningResource, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    time_spent = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.learning_resource.name + (' (Completed)' if self.completed else '')
    
    def set_completed(self):
        self.completed = True
        self.save()


# id: int
# skill_level: SkillLevel
# duration: int
# learning_route_resources: learningRouteResource[]
# actual_resource_index: int
# completed: bool
# time_spent: int

class LearningRoute(models.Model):
    id = models.AutoField(primary_key=True)
    skill_level = models.ForeignKey(SkillLevel, on_delete=models.CASCADE)
    duration = models.IntegerField(validators=[MinValueValidator(1)])
    learning_route_resources = models.ManyToManyField(LearningRouteResource, related_name='learning_routes', blank=True)
    actual_resource_index = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    time_spent = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return self.skill_level.skill.name + ' - ' + str(self.skill_level.level)