from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="Usuário"
    )
    total = models.FloatField()
    total_qty = models.PositiveIntegerField(verbose_name="Quantidade Total")
    status = models.CharField(
        max_length=1,
        default="C",
        choices=(
            ("A", "Aprovado"),
            ("C", "Criado"),
            ("R", "Reprovado"),
            ("P", "Pendente"),
            ("E", "Enviado"),
            ("F", "Finalizado"),
        )
    )

    def __str__(self) -> str:
        return f"Pedido N. {self.pk}"
    

class OrderItems(models.Model):
    class Meta:
        verbose_name = "Item do Pedido"
        verbose_name_plural = "Itens do Pedido"

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="Pedido"
    )
    product = models.CharField(max_length=120, verbose_name="Produto")
    product_id = models.PositiveIntegerField(verbose_name="Produto ID")
    variation = models.CharField(max_length=50, verbose_name="Variação")
    variation_id = models.PositiveIntegerField(verbose_name="Variacão ID")
    price = models.FloatField(verbose_name="Preço")
    promotional_price = models.FloatField(verbose_name="Preço Promocional")
    quantity = models.PositiveIntegerField(verbose_name="Quantidade")
    image = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return f"Item do {self.order}"