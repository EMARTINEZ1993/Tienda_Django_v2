# 🛒 Django TechStore v2

Una aplicación web de comercio electrónico desarrollada con Django que permite gestionar productos, categorías y un sistema de carrito de compras completo.

## 📋 Descripción

Django TechStore es una tienda en línea moderna que ofrece:
- Catálogo de productos organizados por categorías
- Sistema de carrito de compras
- Gestión de ofertas y promociones
- Búsqueda de productos
- Panel de administración personalizado con Jazzmin
- Interfaz responsive y amigable

## 🚀 Características Principales

### 🛍️ Funcionalidades de la Tienda
- **Catálogo de Productos**: Visualización de productos con imágenes, descripciones y precios
- **Categorías**: Organización de productos por categorías
- **Sistema de Ofertas**: Productos destacados en oferta
- **Búsqueda**: Búsqueda de productos por nombre
- **Carrito de Compras**: Agregar, eliminar y modificar cantidades
- **Proceso de Compra**: Sistema completo de checkout

### 🎨 Interfaz de Usuario
- Diseño responsive
- Navegación intuitiva
- Plantillas HTML organizadas
- Archivos estáticos (CSS/JS) estructurados

### 🔧 Panel de Administración
- Interface personalizada con **Jazzmin**
- Gestión de productos y categorías
- Administración de usuarios y órdenes
- Carga de imágenes para productos y categorías

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.2
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Frontend**: HTML, CSS, JavaScript
- **Servidor Web**: Gunicorn
- **Manejo de Imágenes**: Pillow
- **Admin Interface**: Django Jazzmin
- **Despliegue**: Heroku (configurado)

## 📦 Instalación y Configuración

### Prerrequisitos
- Python 3.8+
- pip
- Git

### 1. Clonar el Repositorio
```bash
git clone https://github.com/EMARTINEZ1993/Tienda_Django_v2.git
cd Tienda_Django_v2/django_techstore
```

### 2. Crear Entorno Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear Superusuario
```bash
python manage.py createsuperuser
```

### 6. Ejecutar el Servidor
```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

## 📁 Estructura del Proyecto

```
django_techstore/
├── django_techstore/          # Configuración principal
│   ├── settings.py           # Configuraciones del proyecto
│   ├── urls.py              # URLs principales
│   ├── wsgi.py              # Configuración WSGI
│   └── asgi.py              # Configuración ASGI
├── productos/                # App principal de productos
│   ├── models.py            # Modelos de datos
│   ├── views.py             # Vistas y lógica de negocio
│   ├── urls.py              # URLs de la app
│   ├── admin.py             # Configuración del admin
│   ├── context_processors.py # Procesadores de contexto
│   └── templates/           # Plantillas HTML
│       └── productos/
├── static/                   # Archivos estáticos
│   ├── css/                 # Hojas de estilo
│   └── js/                  # JavaScript
├── media/                    # Archivos multimedia
│   ├── productos/           # Imágenes de productos
│   └── categorias/          # Imágenes de categorías
├── requirements.txt          # Dependencias
├── Procfile                 # Configuración Heroku
└── manage.py                # Script de gestión Django
```

## 🗄️ Modelos de Datos

### Categoria
- `nombre`: Nombre de la categoría
- `imagen`: Imagen representativa

### Producto
- `nombre`: Nombre del producto
- `descripcion`: Descripción detallada
- `precio`: Precio del producto
- `categoria`: Relación con categoría
- `imagen`: Imagen del producto
- `en_oferta`: Indicador de oferta

### Carrito
- `producto`: Producto en el carrito
- `cantidad`: Cantidad del producto

### Orden
- `carrito`: Productos de la orden
- `fecha`: Fecha de creación
- `total`: Total de la orden

### Usuario
- `nombre`: Nombre del usuario
- `email`: Correo electrónico
- `fecha_registro`: Fecha de registro
- `contrasena`: Contraseña del usuario

## 🌐 URLs Principales

- `/` - Página principal
- `/productos/` - Lista de todos los productos
- `/categoria/<id>/` - Productos por categoría
- `/producto/<id>/` - Detalle del producto
- `/ofertas/` - Productos en oferta
- `/carrito/` - Ver carrito de compras
- `/buscar/` - Búsqueda de productos
- `/admin/` - Panel de administración

## 🎯 Funcionalidades del Carrito

- **Agregar productos**: Desde cualquier vista de producto
- **Modificar cantidades**: Aumentar/disminuir desde el carrito
- **Eliminar productos**: Remover productos individuales
- **Vaciar carrito**: Limpiar todo el carrito
- **Proceso de compra**: Finalizar compra y generar orden

## 🔧 Configuración de Producción

### Variables de Entorno Recomendadas
```bash
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com
DATABASE_URL=postgresql://...
```

### Despliegue en Heroku
El proyecto incluye configuración para Heroku:
- `Procfile` configurado
- `requirements.txt` actualizado
- Configuración de archivos estáticos

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Notas de Desarrollo

### Mejoras Sugeridas
- Implementar autenticación de usuarios
- Agregar sistema de pagos
- Implementar inventario de productos
- Agregar sistema de reseñas
- Mejorar la seguridad de contraseñas
- Implementar cache para mejor rendimiento

### Consideraciones de Seguridad
- Cambiar `SECRET_KEY` en producción
- Configurar `DEBUG = False` en producción
- Implementar HTTPS
- Validar y sanitizar inputs de usuario

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**EMARTINEZ1993**
- GitHub: [@EMARTINEZ1993](https://github.com/EMARTINEZ1993)
- Proyecto: [Tienda_Django_v2](https://github.com/EMARTINEZ1993/Tienda_Django_v2)

## 📞 Soporte

Si tienes alguna pregunta o problema, por favor:
1. Revisa la documentación
2. Busca en los issues existentes
3. Crea un nuevo issue si es necesario

---

⭐ **¡No olvides dar una estrella al proyecto si te ha sido útil!** ⭐