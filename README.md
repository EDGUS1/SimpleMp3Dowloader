# Descargar música de Youtube 

## Crear entorno virtual Windows

```sh
python -m venv <nombre>
```

## Ingresar al entorno virtual Windows

```sh
.\<nombre>\Scripts\activate
```

## Instalar dependencias

```sh
pip install -r requirements.txt
```

## Salir del entorno virtual

```sh
deactivate
```

## Ejecución

```sh
python src/main.py
```


## Funcionamiento

- Agregar los links de youtube al archivo links.txt
- Los archivos se alamacenaran en la carpeta src/out