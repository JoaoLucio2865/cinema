# Generated by Django 4.2.5 on 2023-09-26 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Continente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('duracao', models.TimeField()),
                ('data_disponibilizacao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('duracao', models.TimeField()),
                ('sinopse', models.CharField(max_length=200)),
                ('site_oficial', models.CharField(max_length=50)),
                ('data_lancamento', models.DateField()),
                ('nota_avaliacao', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('site', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('facebook', models.CharField(max_length=50)),
                ('twitter', models.CharField(max_length=50)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('continente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.continente')),
                ('nacionalidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nacionalidade')),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('duracao', models.TimeField()),
                ('sinopse', models.CharField(max_length=50)),
                ('site_oficial', models.CharField(max_length=50)),
                ('data_lancamento', models.DateField()),
                ('nota_avaliacao', models.DecimalField(decimal_places=2, max_digits=8)),
                ('diretor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario')),
                ('genero', models.ManyToManyField(to='app.genero')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('episodio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.episodio')),
            ],
        ),
        migrations.CreateModel(
            name='SerieEpisodio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.serie')),
                ('temporada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.temporada')),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='nacionalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nacionalidade'),
        ),
        migrations.CreateModel(
            name='FilmeAtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario')),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.filme')),
            ],
        ),
        migrations.AddField(
            model_name='filme',
            name='diretor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario'),
        ),
        migrations.AddField(
            model_name='filme',
            name='genero',
            field=models.ManyToManyField(to='app.genero'),
        ),
        migrations.AddField(
            model_name='filme',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais'),
        ),
    ]
