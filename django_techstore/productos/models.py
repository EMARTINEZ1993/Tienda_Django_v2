from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True)  # Permite valores nulos inicialmente

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')
    en_oferta = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
class Carrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

    @property
    def subtotal(self):
        return self.producto.precio * self.cantidad


class Orden(models.Model):
    carrito = models.ManyToManyField(Carrito)
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de creación de la orden
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total de la orden

    def __str__(self):
        return f"Orden #{self.id} - Total: {self.total}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Fecha de registro del usuario


    contrasena = models.CharField(max_length=100)  # Almacenar contraseñas de forma segura es importante

    def __str__(self):
        return self.nombre