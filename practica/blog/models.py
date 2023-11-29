from django.db import models

class Cliente(models.Model):
    clienteid=models.CharField(primary_key=True,max_length=50,verbose_name='Rut Cliente')
    nombre=models.CharField(max_length=50, verbose_name="Nombre Cliente")
    apellido=models.CharField(max_length=50, verbose_name="Apellido Cliente")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    username = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    product = models.CharField(max_length=50, verbose_name="Nombre de producto")
    productoid=models.CharField(primary_key=True,max_length=50,verbose_name='ID Producto')
    text = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="projects", verbose_name="imagen")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.product}"


class Calificacion(models.Model):
    product= models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Nombre Producto')
    text = models.TextField(verbose_name="Reseña")
    calificacion_estrella = models.IntegerField(
        default=0,  
        verbose_name="Calificación Estrella",
        help_text="Ingrese la calificación estrella del producto (de 1 a 5)."
    )

    class Meta:
        verbose_name = "Calificacion"
        verbose_name_plural = "Calificacion"

    def __str__(self):
        return f"{self.producto}"



