# IA_OpenSource2

-Autor: Gonzalo Solórzano Calvo

-Title: IA_OpenSource2

-Description: This is an individual project of the IA_Open_Source course of the ETSIINF computer science faculty.
This project consists of analyzing PDFs using the Grobid service.
The objectives are:
*Drawing a keyword cloud based on the words found in the abstract of the PDFs
*Create a visualization showing the number of figures per article
(How to achieve these objectives is documented in the document rationales.md located at IA_OpenSource2/IA_OpenSource2/rationales.md)

To manage the develoment enviroment od this python project, poetry has been the tool to use.
The goal is to dockerize the whole enviroment.

More detailed project specifications are documented in the IA_OpenSource2/IA_OpenSource2/README.md

docker network create <nombre_de_la_red>
docker run --name grobid --network <nombre_de_la_red> -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
docker run --rm -it --network="test" -v /home/kali/IA_OpenSource2/montaje:/Proy/Resources dockerfile

