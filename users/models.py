from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

REGEX = '^[a-zA-Z0-9.+-]*$'


class BlogCustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email required")
        if not username:
            raise ValueError("username requried")

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class BlogCustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True, validators=[RegexValidator(
        regex=REGEX, message="username must contain alphabets and numbers only", code='invalid username')])
    email = models.EmailField(
        max_length=256, verbose_name="Email", unique=True)

    bio = models.TextField(verbose_name='bio', blank=True, null=True)
    # password not overridden

    display_picture = models.ImageField(
        upload_to='images/display_pictures', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = BlogCustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.username} ({self.email})"

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def updateEmail(self, newEmail):
        self.email = newEmail

    def updateBio(self, newBio):
        self.bio = newBio
