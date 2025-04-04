from django.db import models

class ChatMessage(models.Model):
    session_key = models.CharField(max_length=255)
    is_user = models.BooleanField(default=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{'User' if self.is_user else 'GPT'}: {self.message[:50]}"