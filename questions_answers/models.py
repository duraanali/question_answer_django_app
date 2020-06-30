from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (1, "Unsolved"),
    (0, "Solved")
)


class Questions(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questionsByUser", null=True)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.title
    

class Answers(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="answersByQuestion", null=True)
    reply = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answersByUser", null=True)
    
    
    def __str__(self):
        return self.reply
    

class Person(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    bio = models.TextField(null=True)
    country = models.CharField(max_length=200, null=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
