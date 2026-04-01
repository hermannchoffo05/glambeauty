from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.FloatField()
    image = models.ImageField(upload_to='produits/', blank=True)

    def __str__(self):
        return self.nom

class Service(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    icone = models.CharField(
        max_length=100,
        help_text="Classe Font Awesome ex: fa-spa, fa-star, fa-heart"
    )

    def __str__(self):
        return self.titre