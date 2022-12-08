from django.db import models

idea_choices = (
    ('pending', 'Waiting for review'),
    ('accepted', 'Accepted'),
    ('done', 'Done'),
    ('rejected', 'Rejected'),
)


# Create your models here.
class Ideas(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(choices=idea_choices, default='pending')


class Vote(models.Model):
    idea = models.ForeignKey(Ideas, on_delete=models.CASCADE())
    reason = models.TextField()
