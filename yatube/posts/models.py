from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField('название группы', max_length=200)
    slug = models.SlugField('уникальный адрес группы', unique=True)
    description = models.TextField('описание группы')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField('текст поста')
    pub_date = models.DateTimeField(
        'дата и время публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='автор',
    )
    group = models.ForeignKey(
        Group,
        related_name='posts',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='группа',
    )

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ('-pub_date',)

    def __str__(self) -> str:
        return self.text
