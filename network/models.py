from django.db import models


class Contacts(models.Model):
    """Модель для хранения контактной информации."""
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Электронная почта'
    )
    country = models.CharField(
        max_length=100,
        verbose_name='Страна'
    )
    city = models.CharField(
        max_length=100,
        verbose_name='Город'
    )
    street = models.CharField(
        max_length=100,
        verbose_name='Улица'
    )
    house_number = models.CharField(
        max_length=10,
        verbose_name='Номер дома'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактные информации'


class Network(models.Model):
    """Модель для представления сети по продаже электроники."""
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]
    
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Электронная почта'
    )
    country = models.CharField(
        max_length=100,
        verbose_name='Страна'
    )
    city = models.CharField(
        max_length=100,
        verbose_name='Город'
    )
    street = models.CharField(
        max_length=100,
        verbose_name='Улица'
    )
    house_number = models.CharField(
        max_length=10,
        verbose_name='Номер дома'
    )
    supplier = models.ForeignKey(
        Contacts,
        on_delete=models.CASCADE,
        verbose_name='Поставщик'
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Задолженность'
    )
    level = models.IntegerField(
        choices=LEVEL_CHOICES,
        verbose_name='Уровень'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сеть'
        verbose_name_plural = 'Сети'


class Product(models.Model):
    """Модель для хранения информации о продуктах."""
    name = models.CharField(
        max_length=255,
        verbose_name='Название продукта'
    )
    model = models.CharField(
        max_length=255,
        verbose_name='Модель'
    )
    release_date = models.DateField(
        verbose_name='Дата выпуска'
    )
    network_node = models.ForeignKey(
        Network,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Сеть'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
