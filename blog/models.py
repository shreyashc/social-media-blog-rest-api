from django.db import models
from users.models import BlogCustomUser


class BlogPost(models.Model):
    author = models.ForeignKey(BlogCustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    category = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=300)
    content = models.TextField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(
        upload_to='images/blog_thumbnails/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name="comment",
                             on_delete=models.CASCADE, blank=False, null=False)
    commented_by = models.ForeignKey(
        BlogCustomUser, on_delete=models.CASCADE, blank=False, null=False)
    text = models.CharField(max_length=200, blank=False, null=False)
    commented_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.commented_by}commented:{self.text} to {self.post}"


class Like(models.Model):
    post = models.ForeignKey(BlogPost, related_name="likes",
                             on_delete=models.CASCADE, blank=False, null=False)
    liked_by = models.ForeignKey(
        BlogCustomUser, on_delete=models.CASCADE, blank=False, null=False)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'liked_by',)
        ordering = ['-id']

    def __str__(self):
        return f"{self.liked_by} liked {self.post}"
