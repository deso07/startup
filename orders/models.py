from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    telegram_username = models.CharField(max_length=100, blank=True)
    
    # Add related_name to avoid clash with auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'В обработке'),
        ('in_progress', 'В работе'),
        ('completed', 'Выполнен'),
        ('cancelled', 'Отменён')
    )
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    name        = models.CharField('Имя', max_length=100)
    telegram    = models.CharField('Telegram', max_length=64)
    deadline    = models.DateField('Дедлайн')
    description = models.TextField('Описание')
    media       = models.FileField('Файл', upload_to='orders_media/', blank=True, null=True)
    status      = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Статус'
    )
    created_at  = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        return f"#{self.id} {self.name}"

    class Meta:
        ordering = ['-created_at']
