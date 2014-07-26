# Parser
from bs4 import BeautifulSoup
import urllib2

# Network and Visualizing
import networkx as nx
import matplotlib.pyplot as plt

# For polite bot
import time
import random

import datetime

url = "http://scholar.google.com"



class CitationGraph:

    def __init__(self, title=''):
        self.g = nx.Graph()

    def add_result(self, result):
        self.g.add_node(result.title)
        for paper in result.papers:
            self.g.add_node(paper.title, paper = paper)
            self.g.add_edge(result.title, paper.title)

    def draw(self, path):
        nx.draw(self.g)
        plt.savefig(path + ".png")


"""
    def extract(self, least_citations):

            if node['citations'] < least_citations:
                self.g.remove(node)
"""


"""
The information of papers gain from specific URL.
It also contains information about the context of the results. (ex. Cited or Related to the paper or a word search result)
"""
class Result:

    def __init__(self, query, title='', depth=1):
        self.title = title
        if 'cited' in query:
            context = 'cited'
        elif 'related' in query:
            context = 'related'
        else:
            context = 'search'
        self.query = query
        self.papers = []
        self.search(1)


    def search(self, depth=1):
        time.sleep(random.randint(10, 20))
        data = opener.open(url + self.query).read()
        soup = BeautifulSoup(data)

        for paper in soup.find_all('div', {'class' : 'gs_r'}):
            title = paper.find('div', {'class' : 'gs_ri'}).find('a').get_text()
            author = paper.find('div', {'class' : 'gs_a'}).get_text()
            abst =  paper.find('div', {'class' : 'gs_rs'}).get_text()
            for link in paper.find_all('a'):
                if 'Cited' in link.get_text():
                    cited_link = link.get('href')            
                    citations = int(link.get_text().strip('Cited by '))
            p = Paper(title, author, abst, cited_link, citations)    
            self.papers.append(p)


    def print_papers(self):
        for paper in self.papers:
            paper.print_data()
            
        

class Paper:
    def __init__(self, title, author, abst, cited_link, citations=0):
        self.title = title
        self.author = author
        self.abst = abst
        self.cited_link = cited_link
        self.citations = citations
        

    def print_data(self):
        print(self.title)
        print(self.author)
        print(self.abst)
        print(self.citations)
        print(self.cited_link)
        print('\n')

        


"""
Main Function 
"""

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
query = "/scholar?hl=en&q=computer&btnG=&as_sdt=1%2C5&as_sdtp="
r = Result(query, 'computer')
r.print_papers()
c = CitationGraph()
c.add_result(r)

for paper in r.papers:
    r2 = Result(paper.cited_link, paper.title)
    r2.print_papers()
    c.add_result(r2)

t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

c.draw('whole' + t)
plt.show()
