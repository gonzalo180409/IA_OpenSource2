This document explains how the script has been developed


The first thing to do is to send the PDFs to the Grobid service, this service returns an XML for each document sent, which is used to generate the word cloud, the display of the number of images, and the links.

To generate the word cloud, the abstract of the generated XML is taken and a stopwords filter is passed to keep the keywords, these words are stored in a dictionary to keep track of how many times each one appears, and the word cloud of the most repeated keywords in all the PDFs is generated

At the same time, the number of images in each PDF is counted, and then an image is displayed that clearly shows this information.

When the text has been cleaned, the links are searched for and chained in a list to be printed on the screen.

![WorkFLow](https://github.com/gonzalo180409/IA_OpenSource2/blob/main/WorkFlow%20IA.jpg)
