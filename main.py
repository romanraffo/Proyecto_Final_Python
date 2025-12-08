"""
Puntos elegidos a realizar:

1. Rentabilidad (ROI) por género o país.
○ ROI = revenue / budget
○ Analizar distribución y valores promedio por grupo.

2. Relación entre presupuesto y rating.
○ Correlaciones (Pearson, Spearman) y dispersogramas.

3. Evolución de la duración de películas en los últimos 50 años.
○ Promedio o mediana de runtime por década.

6. Distribución del rating por idioma o país de producción.
Cada análisis debe acompañarse con interpretación textual (no solo gráficos).

--------------------------------------------------------------------------------------------------------------------------------------------

                ¡¡¡IMPORTANTE!!!
👇 ACLARACIÓN DE LA ORGANIZACIÓN DEL PROYECTO👇

CARPETA "ENTRADAS" SON LOS LINKS DE LOS ARCHIVOS CSV DE KAGGLE.
CARPETA "SALIDAS" SON LAS VARIABLES TRANSFORMADAS A CSV.
CARPETA "VIDEO_PDF" AHÍ SE GUARDÓ EN UN ARCHIVO EN LINK AL VIDEO EXPLICATIVO Y EN OTRO ARCHIVO EL INFORME DEL PROYECTO EN PDF.
ARCHIVO "APP.PY" ES DONDE SE REALIZA EL TRABAJO CON LA API.
ARCHIVO "MAIN.PY" ES DONDE SE REALIZAN LAS OPERACIONES PRINCIPALES, TRABAJO DE PANDAS + GRÁFICOS.
ARCHIVO "README.MD" EXPLICACIÓN DEL PROYECTO EN ESTE FORMATO.
ARCHIVO "REQUERIMENTS.TXT" ESTÁN ANOTADOS AQUÍ LAS LIBRERÍAS UTILIZADAS PARA EL PROYECTO.
"""

#MAIN.PY ES DONDE SE REALIZAN LAS OPERACIONES PRINCIPALES

import pandas as pd
import ast
import seaborn as sns
import matplotlib.pyplot as plt

dataframe = pd.read_csv("C:\\Users\\Usuario\\Desktop\\proyectoLenguajes\\entradas\\tmdb_5000_movies.csv", index_col="id")

#Realizo la función "primer_genre" para que el género este solo, que esté en formato python(ya que esta en JSON) y así poder usarlo para sacar promedios, etc.
def primer_genre(x):
    try:
        lst = ast.literal_eval(x)      # <- ast.literal_eval convierte el string tipo "[{'id': 12, 'name':'Action'}, ...]" a una lista real de dicts
        return lst[0]["name"] if lst else None  # si la lista no está vacía, devuelvo el nombre del primer género
    except Exception:
        return None # Si ocurre cualquier error al parsear (p. ej. el string está vacío o malformado), devuelvo None

dataframe["tipo_genre"] = dataframe["genres"].apply(primer_genre)


# 1. Rentabilidad (ROI) por género o país.
#Agregado de ROI
dataframe_valido = dataframe[(dataframe["budget"] > 0) & (dataframe["revenue"] > 0)].copy() #Creo un nuevo dataframe donde los valores de budget y revenue sean mayor a 0, ya que para el roi cuenta como inválidos xq el 0 no se cuenta.
dataframe_valido["roi"] = dataframe_valido["revenue"] / dataframe_valido["budget"] #Creo una nueva columna con nombre "roi" donde cada fila tendra el calculo de su budget y revenue.

#Calculo por grupos, en este caso lo hice por género.
roi_por_genero = dataframe_valido.groupby("tipo_genre")["roi"].agg(["count", "mean", "median"]).reset_index() #el count se calcula en base al groupby, y lo demás en base al roi. .agg() es un método de pandas que sirve para aplicar varias funciones estadísticas a la vez sobre un grupo de datos. *count → cuántas películas hay en ese género. *mean → el ROI promedio del género. *median → la mediana del ROI.
print(roi_por_genero)

# Ordenar los géneros por ROI promedio antes de graficar
roi_ordenado = roi_por_genero.sort_values("mean", ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(data=roi_ordenado, x="tipo_genre", y="mean")

plt.title("ROI promedio por género")
plt.xlabel("Género")
plt.ylabel("ROI promedio")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# 2.Relación entre presupuesto y rating.
# Correlaciones (Pearson, Spearman) y dispersogramas.

# Datos filtrados
sub = dataframe[["budget", "vote_average"]].dropna() # dropna() elimina filas con valores vacíos
sub = sub[sub["budget"] > 0]

# Correlaciones
pearson = sub["budget"].corr(sub["vote_average"], method="pearson")
spearman = sub["budget"].corr(sub["vote_average"], method="spearman")

print("Correlación Pearson:", pearson)
print("Correlación Spearman:", spearman)

# Crear diccionario con las correlaciones
correlaciones_dict = {
    "tipo": ["pearson", "spearman"],
    "valor": [pearson, spearman]
}

# Convertir a DataFrame
correlaciones_df = pd.DataFrame(correlaciones_dict)

# Dispersograma
sns.scatterplot(data=sub, x="budget", y="vote_average")
plt.title("Presupuesto vs Rating")
plt.xlabel("Presupuesto (budget)")
plt.ylabel("Rating (vote_average)")
plt.show()


#3. Evolución de la duración de películas en los últimos 50 años.
#○ Promedio o mediana de runtime por década.

dataframe["release_date"] = pd.to_datetime(dataframe["release_date"], errors="coerce") #Reescribo el release_date asi se tranforma la fecha en tipo dato.
dataframe["anio"] = dataframe["release_date"].dt.year #Traigo la columna de la fecha, y a las filas de esa le saco el año. creando la columna año ademas. 
dataframe["ultimos50anios"] =  (dataframe["anio"] >= 1975) #Teniendo en cuenta que el año actual es 2025. 

dataframe_ultimos_50 = dataframe[dataframe["ultimos50anios"] == True]
promedio_runtime_50anios = dataframe_ultimos_50["runtime"].agg(["mean"])
print(f"Promedio de duracion de tiempo de la películas en los ultimos 50 años: -->  {promedio_runtime_50anios}  <--")


#6. Distribución del rating por idioma o país de producción.
#Cada análisis debe acompañarse con interpretación textual (no solo gráficos).

# Filtrar ratings válidos
df_rating = dataframe[(dataframe["vote_average"] > 0)].copy()

# Agrupación estadística (promedio, mediana, conteo)
rating_por_idioma = df_rating.groupby("original_language")["vote_average"].agg(["count", "mean", "median"]).reset_index()
print(rating_por_idioma.sort_values("mean", ascending=False))

plt.figure(figsize=(12,6))
sns.boxplot(data=df_rating, x="original_language", y="vote_average")
plt.title("Distribución del rating por idioma de producción")
plt.xlabel("Idioma")
plt.ylabel("Rating (vote_average)")
plt.show()

"""
Análisis de punto 6: 
Interpretación del análisis de rating por idioma.
Cuando comparé los ratings según el idioma original de cada película, se ven diferencias bastante marcadas entre unos y otros.
Por ejemplo, los idiomas japonés (ja), francés (fr) y coreano (ko) terminan teniendo, en promedio, mejores puntajes. Además, en estos idiomas la distribución es más pareja: casi no aparecen ratings muy bajos, lo que muestra que suelen mantener una calidad más constante.
En cambio, en el caso del inglés ("en"), que es el idioma que más películas tiene en el dataset, la dispersión es mucho más grande. Hay de todo: películas con ratings muy buenos y otras bastante malas. Esto tiene sentido porque se producen muchísimas películas en inglés y hay más variedad.
En los idiomas menos comunes (como “hi”, “ru”, etc.), se ven distribuciones más “inestables”, principalmente porque hay muy pocas películas y cualquier valor extremo influye más.
En general, mirando todo el conjunto, se nota que los idiomas asiáticos (como japonés y coreano) tienden a tener mejores promedios de rating dentro del dataset que analicé.
"""


#ESTAS 4 VARIABLES TRANSFORMADAS A CSV, SE GUARDAN EN LA CARPETA "SALIDAS" AL PASARSE A CSV.
roi_por_genero.to_csv("salidas/roi_por_genero.csv", index=False)
correlaciones_df.to_csv("salidas/correlacion_budget_rating.csv", index=False)
promedio_runtime_50anios.to_csv("salidas/promedio_runtime_50anios.csv", index=False)
rating_por_idioma.to_csv("salidas/rating_por_idioma.csv", index=False)