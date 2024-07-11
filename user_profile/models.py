from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Usuário"
    )
    born = models.DateField(verbose_name="Data de Nascimento")
    cpf = models.CharField(verbose_name="CPF", max_length=11)
    address = models.CharField(verbose_name="Endereço", max_length=50)
    number = models.CharField(verbose_name="Numero", max_length=5)
    complement = models.CharField(verbose_name="Complemento", max_length=30)
    neighborhood = models.CharField(verbose_name="Bairro", max_length=30)
    zip_code = models.CharField(verbose_name="CEP", max_length=8)
    city = models.CharField(verbose_name="Cidade", max_length=30)
    state = models.CharField(
        verbose_name="Estado", 
        max_length=2,
        default="SP",
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
    
    def clean(self) -> None:
        # TODO: make the clean method
        ...