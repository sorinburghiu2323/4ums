from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


# User Class
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Create and save a SuperUser with the given email and password.
    """

    email = models.EmailField(unique=True)
    password = models.CharField(blank=True, max_length=255)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    teacher_request = models.BooleanField(
        default=False
    )  # When the user applies for a teacher account.
    is_teacher = models.BooleanField(default=False)
    hide_leaderboard = models.BooleanField(default=False)

    # Permission fields
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return ("TEACHER REQUEST: " if self.teacher_request else "") + self.email

    def serialize_simple(self):
        return {
            "id": self.id,
            "username": self.username,
            "points": self.points,
            "is_teacher": self.is_teacher,
        }


# Community Class
class Community(models.Model):
    """
    Community model where the name is a unique modifier
    and has user as a foreign key
    """

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )  # Creator of the Community
    name = models.CharField(
        max_length=255, unique=True
    )  # Set the Name of the Community
    description = models.TextField(max_length=255)  # Community Description
    created_at = models.DateTimeField(
        default=timezone.now
    )  # Time of Community Being Created

    def __str__(self):
        return self.name

    def serialize_simple(self):
        return {"id": self.id, "name": self.name, "description": self.description}

    def serialize(self):
        return {
            "user": self.user,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
        }


class CommunityMember(models.Model):
    """
    Community-User relationship to keep track of the community members.
    """

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    community = models.ForeignKey(Community, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username + " in community: " + self.community.name


class Post(models.Model):
    """
    Post model where the title is a unique modifier
    and has user and community as foreign keys
    """

    class PostType(models.TextChoices):
        """
        Enum for Post type so that the posts will have two specific
        types, discussion and question posts.
        """

        DISCUSSION = "discussion"
        QUESTION = "question"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(default=0)
    post_type = models.CharField(
        max_length=20, choices=PostType.choices, default=PostType.DISCUSSION
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def serialize(self, request=None):
        return {
            "id": self.id,
            "user": self.user.serialize_simple(),
            "is_community_owner": Community.objects.filter(user=self.user).exists(),
            "community": self.community.serialize_simple(),
            "title": self.title,
            "description": self.description,
            "post_type": self.post_type,
            "created_at": self.created_at,
            "likes_num": PostLike.objects.filter(post=self).count(),
            "comments_num": PostComment.objects.filter(post=self).count(),
            "is_liked": PostLike.objects.filter(user=request.user, post=self).exists()
            if request
            else False,
        }


# PostLike Class
class PostLike(models.Model):
    """
    Post like model where the title is a unique modifier
    and has user and post as foreign keys
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post.title

    def serialize(self):
        return {
            "user": self.user,
            "post": self.post,
            "created_at": self.created_at,
        }


# PostComment Class
class PostComment(models.Model):
    """
    Post model where the title is a unique modifier
    and has user and post as foreign keys
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=255, unique=False)
    is_approved = models.BooleanField(default=0, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post.title

    def serialize(self):
        return {
            "user": self.user,
            "post": self.post,
            "comment": self.comment,
            "is_approved": self.is_approved,
            "created_at": self.created_at,
        }


# PostCommentLike Class
class PostCommentLike(models.Model):
    """
    Post Comment Like model where the user and post_comment make up
    the foreign keys and the unique attribute is the id.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_comment = models.ForeignKey(PostComment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_comment.__str__()

    def serialize(self):
        return {
            "user": self.user,
            "post_comment": self.post_comment,
            "created_at": self.created_at,
        }


class PointsGained(models.Model):
    """
    Record of points gained for the user consists of the community the post and the comment
    they have gained points in.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(
        Community, on_delete=models.SET_NULL, null=True, blank=True
    )
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.ForeignKey(
        PostComment, on_delete=models.SET_NULL, null=True, blank=True
    )
    points = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.email + " gained: " + str(self.points) + " points."
