from django.db import models
from django.contrib.auth.models import User

# data base model for the rating of users


class Rating_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_choices = [
        (1, '😢'), (2, '😔'), (3, '😐'), (4, '😊'), (5, '😁'),
    ]
    mood_rating = models.IntegerField(
        choices=rating_choices, default=3)
    productivity_rating = models.IntegerField(
        choices=rating_choices, default=3)
    date = models.DateField(auto_now_add=True)

# data base model for the to dolist of users


class To_do_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    task_title = models.CharField(max_length=24)
    created = models.DateTimeField(auto_now_add=True)
