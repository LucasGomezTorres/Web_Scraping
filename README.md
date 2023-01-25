# Proyecto de Web Scraping

## Integrantes del proyecto 
- Lucas Gómez Torres
- Joan Amengual Mesquida

## Contexto del proyecto 

La ejecución del proyecto de Web Scraping se ha basado en la extracción de información de las películas clasificadas por categorías en la página: https://www.imdb.com/feature/genre/

## Requisitos previos

En la ejecución de proyecto se usa el navegador Firefox para realizar una interacción dinámica con el contenido de la página elegida. Por ese motivo, disponer de Firefox instalado es un requisito para poder llevar a cabo la ejecución del proyecto. 

## Ejecución del proyecto

Para llevar a cabo la ejecución del proyecto es necesario ejecutar el fichero principal llamado *main.py*. 

Comandos a ejecutar: 

- git clone https://github.com/LucasGomezTorres/Web_Scraping.git
- cd Web_Scraping
- python3 src/main.py

## Descripción de archivos que componen el repositorio

- genres_extraction: se lleva a cabo la extracción de los nombres de los géneros y sus respectivas URLs. 

- genre_movies: se realiza la extracción de las distintas características de las películas.

- get_images: se encarga de realizar toda la lógica necesaria para descargar los carteles de las películas.

- get_videos: se encarga de realizar toda la lógica necesaria para descargar los tráilers de las películas.

- login: archivo que realiza un login a través de un usuario y una contraseña y se devuelven dos sesiones, una mediante la librería requests y la otra mediante Selenium a través del navegador Firefox.

- login_docker: archivo que realiza un login a través de un usuario y una contraseña y se devuelven dos sesiones, una mediante la librería requests y la otra mediante Selenium a través del navegador Chrome; únicamente para su ejecución a través de contenedor Docker.

- review_movie: se realiza una valoración personal interactuando dinámicamente con el navegador una vez logeados dentro de la página web.

- main: fichero principal del proyecto, el cuál hay que ejecutar para llevar a cabo la extracción de los datos y su posterior creación del dataset en formato .CSV.

- main_docker: fichero principal del proyecto para su ejecución a través de contenedor Docker, el cuál hay que ejecutar para llevar a cabo la extracción de los datos y su posterior creación del dataset en formato .CSV.

## DOI de Zenodo del dataset generado

- DOI: 10.5281/zenodo.7311723
- URL: https://zenodo.org/record/7311723#.Y21G9C0w1gI

### Requisitos previos a la ejecución

Para llevar a cabo la ejecución del proyecto mediante el uso de contenedores de Docker es necesario tener instalado Docker en nuestra máquina. 

Artículos necesarios para su instalación:

- https://docs.docker.com/desktop/install/windows-install/
- https://docs.docker.com/desktop/install/mac-install/

## Ejecución del proyecto mediante Docker

Comandos a ejecutar: 

- git clone https://github.com/LucasGomezTorres/Web_Scraping.git
- cd Web_Scraping
- bash exe.sh

La primera fase de la ejecución consiste en la construcción de la imagen del proyecto, y todo seguido la siguiente fase consiste en el despliegue del contenedor partiendo de la imagen creada.

