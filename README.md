# Proyecto de Web Scraping

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

## Ejecución del proyecto mediante Docker

### Requisitos previos a la ejecución

Para llevar a cabo la ejecución del proyecto mediante el uso de contenedores de Docker es necesario tener instalado Docker en nuestra máquina. 

Artículos necesarios para su instalación:

- https://docs.docker.com/desktop/install/windows-install/
- https://docs.docker.com/desktop/install/mac-install/

## Ejecución del proyecto mediante Docker

- cd Web_Scraping
- bash exe.sh

La primera fase de la ejecución consiste en la construcción de la imagen del proyecto, y todo seguido la siguiente fase consiste en el despliegue del contenedor partiendo de la imagen creada.