from django.db import models
from utils.images import resize_image
from utils.rands import new_slugfy

class Product(models.Model):
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    nome = models.CharField(max_length=120)
    descricao_curta = models.TextField(max_length=120)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to="product_image/%Y/%m/", 
        blank=True, 
        default=""
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        default="",
        null=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(
        default="V", 
        max_length=1, 
        choices=(
            ("V", "Variação"), 
            ("S", "Simples"),
        )
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugfy(self.nome, 3)

        currente_image_name = str(self.imagem.name)
        super_save = super().save(*args, **kwargs)
        imagem_saved = False

        if self.imagem:
            imagem_saved = currente_image_name != self.imagem.name

        if imagem_saved:
            resize_image(self.imagem)

        return super_save

    def __str__(self) -> str:
        return self.nome
    

class Variation(models.Model):
    class Meta:
        verbose_name = "Variação"
        verbose_name_plural = "Variações"

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    nome = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.nome