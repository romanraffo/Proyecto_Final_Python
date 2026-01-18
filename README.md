<h1 align="center">📊 Análisis de Datos + Mini API con Flask</h1>

<h2>📌 Descripción del Proyecto</h2>
<p>
Este proyecto combina un análisis exploratorio de datos (EDA) con la creación de una mini API local usando Flask.
El objetivo es analizar el dataset <strong>TMDB 5000 Movies</strong>, generar estadísticas, visualizaciones y exponer algunos
resultados procesados mediante endpoints en formato JSON.
</p>

<h2>📁 Estructura General</h2>

<h3>1️⃣ Notebook (.ipynb) – Análisis Exploratorio</h3>
<p>En el notebook se realiza:</p>
<ul>
  <li>Lectura y limpieza del dataset</li>
  <li>Transformación de columnas (fechas, géneros, etc.)</li>
  <li>Generación de estadísticas descriptivas</li>
  <li>Gráficos con <code>matplotlib</code> y <code>seaborn</code></li>
  <li>Desarrollo de conclusiones y ejes de análisis</li>
  <li>Exportación de resultados a archivos <code>.csv</code> para la API</li>
</ul>

<h3>2️⃣ Mini-API con Flask</h3>
<p>
La API carga los archivos CSV generados en el análisis y expone la información mediante endpoints simples.
Las respuestas se devuelven en formato JSON.
</p>

<h2>🛠️ Tecnologías Utilizadas</h2>
<ul>
  <li>Python</li>
  <li>Pandas</li>
  <li>Matplotlib</li>
  <li>Seaborn</li>
  <li>Flask</li>
</ul>

<h2>⚠️ Manejo de Errores</h2>
<p>La API incluye validación de parámetros y códigos de error como <code>400</code>, <code>404</code>, etc.</p>

<img src="errorApi.PNG" width="500" />

<h2>▶️ Ejecución</h2>
<ol>
  <li>Ejecutar el notebook para generar los CSV.</li>
  <li>Levantar la API con Flask.</li>
  <li>Acceder a los endpoints para ver los resultados.</li>
</ol>

<h2>📬 Autor</h2>
<p>Proyecto realizado por <strong>Román Raffo</strong> para la materia Lenguajes 2025 - UCALP.</p>

