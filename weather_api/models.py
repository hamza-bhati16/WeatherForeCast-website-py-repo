from django.db import models

# Create your models here.

# class Social(models.Model):
#     website_url = models.CharField(max_length=255, null=True, blank=True)
#     facebook_url = models.CharField(max_length=255, null=True, blank=True)
#     instagram_url = models.CharField(max_length=255, null=True, blank=True)
#     twitter_url = models.CharField(max_length=255, null=True, blank=True)
#     github_url = models.CharField(max_length=255, null=True, blank=True)
#     linkedin_url = models.CharField(max_length=255, null=True, blank=True)
#
#     def __str__(self):
#         return self.website_url

class LegalTopic(models.Model):
    TOPIC_CHOICES = [
        ('family', 'Family Law'),
        ('education', 'Education Law'),
        ('tax', 'Tax Law'),
    ]
    name = models.CharField(max_length=50, choices=TOPIC_CHOICES, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.get_name_display()

class LegalSolution(models.Model):
    topic = models.ForeignKey(LegalTopic, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return f"Solution for {self.topic}: {self.question[:30]}..."
