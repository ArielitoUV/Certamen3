from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Comment(models.Model):
    username = models.CharField(max_length=50, verbose_name="Nombre de usuario")
    text = models.TextField(verbose_name="Comentario sobre el servicio o producto")
    rating = models.PositiveIntegerField(
        verbose_name="Calificación",
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de ingreso del comentario")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización de los comentarios")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return self.username

