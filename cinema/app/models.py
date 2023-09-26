from django.db import models

class Continente(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Nacionalidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Pais(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.ForeignKey(Nacionalidade, on_delete=models.CASCADE)
    continente = models.ForeignKey(Continente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.nacionalidade.nome} - {self.continente.nome}'

class Episodio(models.Model):
    nome = models.CharField(max_length=50)
    duracao = models.TimeField()
    data_disponibilizacao = models.DateField()

    def __str__(self):
        return f'{self.nome} - {self.duracao} - {self.data_disponibilizacao}'

class Temporada(models.Model):
    nome = models.CharField(max_length=50)
    episodio = models.ForeignKey(Episodio, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.episodio.nome}'

class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Ator(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    nacionalidade = models.ForeignKey(Nacionalidade, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.site} - {self.instagram} - {self.facebook} - {self.twitter} - {self.nacionalidade.nome}'

class Diretor(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    nacionalidade = models.ForeignKey(Nacionalidade, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.site} - {self.instagram} - {self.facebook} - {self.twitter} - {self.nacionalidade.nome}'

class Serie(models.Model):
    nome = models.CharField(max_length=50)
    duracao = models.TimeField()
    sinopse = models.CharField(max_length=50)
    site_oficial = models.CharField(max_length=50)
    data_lancamento = models.DateField()
    nota_avaliacao = models.DecimalField(max_digits=8, decimal_places=2)
    genero = models.ManyToManyField(Genero)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.duracao} - {self.sinopse} - {self.site_oficial} - {self.data_lancamento} - {self.nota_avaliacao} - {self.pais.nome} - {self.diretor.nome}'

class SerieEpisodio(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.serie.nome} - {self.temporada.nome}'

class Filme(models.Model):
    nome = models.CharField(max_length=50)
    duracao = models.TimeField()
    sinopse = models.CharField(max_length=200)
    site_oficial = models.CharField(max_length=50)
    data_lancamento = models.DateField()
    nota_avaliacao = models.DecimalField(max_digits=8, decimal_places=2)
    genero = models.ManyToManyField(Genero)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.duracao} - {self.sinopse} - {self.site_oficial} - {self.data_lancamento} - {self.nota_avaliacao} - {self.pais.nome} - {self.diretor.nome}'

class FilmeAtor(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    ator = models.ForeignKey(Ator, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.filme.nome} - {self.ator.nome}'
