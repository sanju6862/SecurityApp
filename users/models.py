from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    USER_TYPES = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('security', 'Security Personnel'),
    )
    USER_TYPES1 = (
    ('student', 'Student'),
    ('faculty', 'Faculty'),
    ('security', 'Security Personnel'),
)
    DEPARTMENTS = (
    ('architecture', 'Architecture, Planning and Design'),
    ('ceramic', 'Ceramic Engineering'),
    ('chemical', 'Chemical Engineering'),
    ('civil', 'Civil Engineering'),
    ('computer', 'Computer Engineering'),
    ('electrical', 'Electrical Engineering'),
    ('electronics', 'Electronics Engineering'),
    ('mechanical', 'Mechanical Engineering'),
    ('metallurgical', 'Metallurgical Engineering'),
    ('mining', 'Mining Engineering'),
    ('pharmaceutical', 'Pharmaceutical Engineering & Technology'),
    ('biochemical', 'Biochemical Engineering'),
    ('biomedical', 'Biomedical Engineering'),
    ('materials', 'Materials Science and Technology'),
    ('chemistry', 'Chemistry'),
    ('physics', 'Physics'),
    ('math', 'Mathematical Sciences'),
    ('humanistic', 'Department of Humanistic Studies'),
)
    current_year = timezone.now().year
    address_city = models.CharField(max_length=100,null=True)
    address_state = models.CharField(max_length=50,null=True)
    address_pin = models.CharField(max_length=10,null=True)
    address_locality = models.CharField(max_length=100, blank=True)
    registration_year = models.PositiveIntegerField(
    validators=[
        MinValueValidator(1900),
        MaxValueValidator(current_year),
    ],null=True
)
    passing_out_year = models.PositiveIntegerField(blank=True, null=True,validators=[
        MinValueValidator(current_year),
        MaxValueValidator(2035),
    ])
    department = models.CharField(max_length = 50, choices=DEPARTMENTS,null=True)
    contact_self = models.CharField(max_length=20,null=True)
    contact_parents = models.CharField(max_length=20, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES,null=True)

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
    # @receiver(post_save, sender=User)
    # def create_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_profile(sender, instance, **kwargs):
    #     instance.profile.save()
        


