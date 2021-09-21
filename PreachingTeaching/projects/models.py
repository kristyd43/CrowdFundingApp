from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum

# Create your models here.


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges',
    )

class Project(models.Model):
    title = models.CharField(max_length=200)
    categories = models.JSONField(default=list)
    description = models.TextField()
    goal = models.IntegerField()
    # total_raised = Pledge.objects.aggregate(Sum('amount'))
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects',
    ) 

    @property
    def total_raised(self):
        return self.pledges.aggregate(sum_pledges = Sum("amount")).get("sum_pledges")


