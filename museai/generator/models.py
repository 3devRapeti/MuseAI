from django.db import models

class Lyrics(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"lyrics are create on {self.created_at}"

class Chords(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"chords are create on {self.created_at}"
