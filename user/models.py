from django.db import models
from preference.models import Preference
from skill.models import SkillLevel
from learning_route.models import LearningRoute

# id: int
# name: string
# password: string
# email: string
# image: Image
# preference: Preference
# current_skills: SkillLevel[]
# target_skills: SkillLevel[]
# learning_routes: LearningRoute[]

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='user/images/', blank=True)
    preference = models.ForeignKey(Preference, on_delete=models.SET_NULL, blank=True, null=True)
    current_skills = models.ManyToManyField(SkillLevel, related_name='users_current', blank=True)
    target_skills = models.ManyToManyField(SkillLevel, related_name='users_target', blank=True)
    learning_routes = models.ManyToManyField(LearningRoute, related_name='users_route', blank=True)

    def __str__(self):
        return f'[{self.id}] {self.name}'
