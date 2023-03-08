# IA_OpenSource2

-Autor: Gonzalo Solórzano Calvo

-Title: IA_OpenSource2

-Description: This is an individual project of the IA_Open_Source course of the ETSIINF computer science faculty.
This project consists of analyzing PDFs using the Grobid service.
The objectives are:

*Drawing a keyword cloud based on the words found in the abstract of the PDFs

*Create a visualization showing the number of figures per article
(How to achieve these objectives is documented in the document rationales.md located at IA_OpenSource2/rationales.md)

To manage the develoment enviroment od this python project, poetry has been the tool to use.
The goal is to dockerize the whole enviroment.

# Follow the steps bellow to use this tool
It is assumed that you have docker and the grobid image installed on your computer.

lfoppiano/grobid:0.7.2 is the image to use.

PDFs to be reviewed must be written in English.

1: git clone this repository

2: create a docker network with the following command: docker network create <nombre_de_la_red>

3: Execute the grobid image with the following command: docker run --name grobid --network <nombre_de_la_red> -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2

4: Move to the next path: /.../IA_OpenSource2/montaje/Resources and copy the PDFs you want to be examined.

You can use the downloaded PDFs or use your own, but it is important to leave them in the location indicated: /.../IA_OpenSource2/montaje/Resources

Take results will be displayed at the /.../IA_OpenSource2/montaje/Resources/figures

5: Move to the next path: /.../IA_OpenSource2 and execute the following command: docker build -t dockerfile .

6: Execute the following command: docker run --rm -it --network="<nombre_de_la_red>" -v /.../IA_OpenSource2/montaje/Resources:/Proy/Resources dockerfile

7: Inside the container execute the following commands: 

poetry shell

poetry run python3 main.py

It takes around 1 min to process all the PDFs and the outputs are displayed at /.../IA_OpenSource2/montaje/Resources/figures

The links will be displayed on the terminal screen.

8: To execute the test: inside de container, move to the following path: /Proy/tests and execute the following command: poetry run python3 test.py



