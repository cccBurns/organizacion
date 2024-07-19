import pandas as pd
from pathlib import Path
import re

# Definimos la ruta del archivo
file_path = Path('Spotify_Song_Attributes.csv')

# Leemos el archivo CSV con pandas
df = pd.read_csv(file_path)

# Convertimos todos los valores de la columna 'genre' a cadenas de texto, reemplazando NaN por 'Desconocido'
df['genre'] = df['genre'].fillna('Desconocido').astype(str)

# Obtener géneros únicos
generos = df['genre'].unique()

# Definir función para limpiar nombres de carpetas
def limpiar_nombre(nombre):
    return re.sub(r'[<>:"/\\|?*]', '', nombre)

# Para cada género, creamos un sub-dataframe y lo guardamos en la carpeta correspondiente
for genero in generos:
    genero_df = df[df['genre'] == genero]
    # Limpiar el nombre del género para usarlo como nombre de carpeta
    nombre_genero_limpio = limpiar_nombre(genero)
    # Creamos las carpetas si no existen
    dir_path = Path(f'generos/{nombre_genero_limpio}')
    dir_path.mkdir(parents=True, exist_ok=True)
    # Guardamos el sub-dataframe en la carpeta correspondiente
    genero_df.to_csv(dir_path / f'Spotify_Song_Attributes_{nombre_genero_limpio}.csv', index=False)

print("Proceso terminado")