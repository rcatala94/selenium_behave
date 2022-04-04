# Descripción #

# Instrucciones #

# Entorno

1. Instalar dependencias:  
- `python -m pip install -r .\requirements.txt`

# Cómo ejecutar

1. Features de Smart WiFi:

```
behave -D udid=1 .\features\melia_random_search.feature 
```

2. Features de Smart WiFi:

```
behave -D udid=1 .\features\melia_rooms.feature --no-capture
```

# Pruebas desarrolladas

- `melia_random_search -> Acceder a la web (www.melia.com) y se realiza una búsqueda destino con fecha y ocupación aleatoria, de momento solo puede ser random el mes en curso y el siguiente.`
- `melia_rooms.feature -> Se accede a la ficha del hotel "https://www.melia.com/es/hoteles/espana/madrid/melia-castilla/habitaciones.htm" y se muestra por pantalla el número total de habitaciones mostradas usando un único xpath`