from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Legislation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Ensure this line exists

    def __str__(self):
        return self.title

class VotingSession(models.Model):
    legislation = models.OneToOneField(Legislation, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()
    votes = models.ManyToManyField(User, through='Vote', related_name='votes')

    def save(self, *args, **kwargs):
        if not self.end_time:
            self.end_time = self.start_time + timedelta(days=7)  # or whatever duration you prefer
        super().save(*args, **kwargs)

    @property
    def is_active(self):
        return timezone.now() < self.end_time
    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(VotingSession, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        logger.debug(f'Creating Vote: User {self.user.id}, Session {self.session.id}, Rating {self.rating}')
        super().save(*args, **kwargs)