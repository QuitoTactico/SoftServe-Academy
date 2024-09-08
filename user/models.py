from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from preference.models import Preference
from skill.models import SkillLevel
from learning_route.models import LearningRoute

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The user must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# id: int
# name: string
# password: string
# email: string
# image: Image
# preference: Preference
# current_skills: SkillLevel[]
# target_skills: SkillLevel[]
# learning_routes: LearningRoute[]

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='user/images/', blank=True)
    preference = models.ForeignKey(Preference, on_delete=models.SET_NULL, blank=True, null=True)
    current_skills = models.ManyToManyField(SkillLevel, related_name='users_current', blank=True)
    target_skills = models.ManyToManyField(SkillLevel, related_name='users_target', blank=True)
    learning_routes = models.ManyToManyField(LearningRoute, related_name='users_route', blank=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'[{self.id}] {self.name}'
