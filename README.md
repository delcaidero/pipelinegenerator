# Repositorio para el ejercicio de Nivel 3A

## Crear un paquete que permita:
--Generar pipelines para un dataset cualquiera
--Activar o desactivar el PCA
--CAMBIAR NÚMERO DE COMPONENTES DEL PCA
--Elegir variables numéricas y categoricas que queremos usar

## Debe tener:
### generador de pipelines
mipaquete.make_pipeline(use_pca=True, components=3, num_var=["age"], cat_var=["sex"])

### entrenador de pipelines
mipaquete.fit(pipeline, X, y)

### exporta paquete entrenador
mipaquete.export(pipeline, file)

### Tambien debe tener:
> test, docstring y un coverage superior al 80%
> crear el GitHubActions de este paquete