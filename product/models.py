from django.db import models
from utils.images import resize_image
from utils.rands import new_slugfy
from utils.format_price import formatprice

class Product(models.Model):
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    name = models.CharField(verbose_name="nome", max_length=120, default="")
    short_description = models.TextField(verbose_name="Descrição Curta", max_length=255, default="")
    long_description = models.TextField(verbose_name="Descrição Longa", default="")
    image = models.ImageField(
        verbose_name="Imagem",
        upload_to="product_image/%Y/%m/", 
        blank=True, 
        default=""
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        default="",
        null=True)
    price_marketing = models.FloatField(verbose_name="Preço Marketing", default=0)
    promotion_price_marketing = models.FloatField(verbose_name="Preço Marketing Promocional", default=0)
    type = models.CharField(
        verbose_name="Tipo",
        default="V", 
        max_length=1, 
        choices=(
            ("V", "Variável"), 
            ("S", "Simples"),
        )
    )

    def formatted_price(self):
        return formatprice(self.price_marketing)
    
    formatted_price.short_description = "Preço"

    def formatted_promotion_price(self):
        return formatprice(self.promotion_price_marketing)
    
    formatted_promotion_price.short_description = "Preço Promo."

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugfy(self.name, 3)

        currente_image_name = str(self.image.name)
        super_save = super().save(*args, **kwargs)
        imagem_saved = False

        if self.image:
            imagem_saved = currente_image_name != self.image.name

        if imagem_saved:
            resize_image(self.image)

        return super_save

    def __str__(self) -> str:
        return self.name
    

class Variation(models.Model):
    class Meta:
        verbose_name = "Variação"
        verbose_name_plural = "Variações"

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(
        verbose_name="Nome",
        max_length=50,
        blank=True,
        null=True
    )
    price = models.FloatField(verbose_name="Preço")
    promotion_price = models.FloatField(verbose_name="Preço Promocional", default=0)
    stock = models.PositiveIntegerField(verbose_name="Estoque", default=0)

    def formatted_price(self):
        return formatprice(self.price)
    
    formatted_price.short_description = "Preço"

    def formatted_promotion_price(self):
        return formatprice(self.promotion_price)
    
    formatted_promotion_price.short_description = "Preço Promo."

    def __str__(self) -> str:
        return self.name