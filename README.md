# Web-Scraping

To understand python basics I have developed a basic example for extracting the data from webpage and storing it into .csv file. As, that is the most used format for analysis. 

List of United States cities by population: This project focuses on using 'BeautifulSoup' library in Python to scrap data from wikipedia.
The general idea behind web scraping is to retrieve data that exists on a wikipedia and convert it into a format that is usable for analysis.
We begin by reading the source code for a given wiki page and creating a BeautifulSoup (soup)object with the BeautifulSoup function. Beautiful Soup is a Python package for parsing HTML and XML documents. 
It creates a parse tree for parsed pages that can be used to extract data from HTML. After carefully inspecting the HTML script all the table contents i.e. list of the countries which we intend to extract is under class "Wikitable Sortable". Hence,creating a list of Countries so that we can extract the name of countries from the link and append it to the list countries and convert the list into dataframe and written that dataframe to .csv file.
