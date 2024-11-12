from django.db import models
from django.db.models import Subquery, OuterRef
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
    level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=1
    )
    learning_resource = models.ForeignKey(LearningResource, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    time_spent = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return (
            "["
            + str(self.id)
            + "] "
            + self.learning_resource.name
            + (" (Completed)" if self.completed else "")
        )

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
    learning_route_resources = models.ManyToManyField(
        LearningRouteResource, related_name="learning_routes", blank=True
    )
    actual_resource_index = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    time_spent = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return self.skill_level.skill.name + " - " + str(self.skill_level.level)

    def set_completed(self):
        self.completed = True
        self.save()

    # This method alone is basically the core of all the project.
    # Used on learning_routes/views.py generate()
    @classmethod
    def generate(cls, user, user_target_skill: SkillLevel):
        # We delete every other learning route with the same skill as target
        user.learning_routes.filter(skill_level__skill=user_target_skill.skill).delete()

        learning_route = cls(skill_level=user_target_skill, duration=0)
        learning_route.save()

        # If you wanna use other order or filter:
        # Comment from "FROM HERE", to "TO HERE", and use the order you want
        learning_resources = (
            LearningResource.objects.filter(
                learning_skills__skill=user_target_skill.skill,
                general_level__lte=user_target_skill.level,
                # These ones are about the user preferences
                media_type=user.preference.media_type,
                # content_type=user.preference.content_type,
                duration__lte=user.preference.time_per_session,
                # Maybe adding another attribute like user.preference.is_strict to filter less would be nice
                # FROM HERE <---
            )
            .annotate(
                # Does two consults (skillLevel filtering) to save them it in the instace search
                # We need the target skillLevel of the resource (required and learning), to get their level
                # Then, we can use that in the final order_by
                required_skill_level=Subquery(
                    SkillLevel.objects.filter(
                        learning_resources_required__id=OuterRef(
                            "pk"
                        ),  # SkillLevel required Reverse FK == Resource
                        skill=user_target_skill.skill,  # SkillLevel skill == User Target Skill
                    ).values("level")[
                        :1
                    ]  # Get the level and saves it on required_skill_level
                ),
                learning_skill_level=Subquery(
                    SkillLevel.objects.filter(
                        learning_resources_learning__id=OuterRef(
                            "pk"
                        ),  # SkillLevel learning Reverse FK == Resource
                        skill=user_target_skill.skill,  # SkillLevel skill == User Target Skill
                    ).values("level")[
                        :1
                    ]  # Get the level and saves it on learning_skill_level
                ),
            )
            .order_by("general_level", "required_skill_level", "learning_skill_level")
        )
        # TO HERE <---
        # ).order_by('general_level')
        # ).order_by('general_level', 'required_skills__level', 'learning_skills__level')  # DON'T USE THIS
        # ).order_by('level', 'required_skills', 'learning_skills')  # DON'T USE THIS

        # Create LearningRouteResource instances and add them to the learning route
        for index, resource in enumerate(learning_resources):
            route_resource = LearningRouteResource.objects.create(
                index=index, level=resource.general_level, learning_resource=resource
            )
            learning_route.learning_route_resources.add(route_resource)

        # Update the duration of the learning route
        learning_route.duration = sum(
            resource.duration for resource in learning_resources
        )
        learning_route.save()

        # Returns it to be added on the user's learning routes
        return learning_route
