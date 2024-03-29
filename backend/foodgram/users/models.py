from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class User(AbstractUser):
    email = models.EmailField('email', max_length=254, unique=True)
    first_name = models.CharField('first_name', max_length=150, blank=False)
    last_name = models.CharField('last_name', max_length=150, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']

    class Meta:
        ordering = ('-pk',)

    @property
    def is_admin(self):
        return self.is_staff or self.is_superuser


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        related_name='follower',
        on_delete=models.CASCADE,
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'author'],
                name='user_author_unique'
            )
        ]

    def __str__(self):
        return f'Пользователь {self.user} подписался на {self.author}'
