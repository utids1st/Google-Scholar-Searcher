Google-Scholar-Searcher
=======================

Extract a citation graph of the paper from google scholar. 

- Overview

GUI <> Algorithm <> Drawing


- Service

Draw a graph of citations & relationships. The main target would be students, eager to study new areas.


- Using Sources

Python		  : language
Beautiful Soup	  : parsing html
Networkx  	  : constructing a graph
Matplotlib	  : plotting a graph
Google App Engine : server


- HTML Structure of Google Scholar Results

gs_r   		 : paper
 |-	gs_ri	 : title
 |-	gs_a	 : author
 |-	gs_rs	 : abstract
 |-	gs_fl	 : citations (fluent) 


- Class

Result		: Store information of papers from a single query. Papers are stored in form on Paper class.   
Paper		: Store information of a paper.


- Graph Modeling

Node		: Paper
Edge		: Relationship of the papers (ex. citation, related or keyword search).


- Graph Pruning Algorithm

So far only thinking on citation graph.

1. No strategy
   Just iterate over N times and show all papers.

2. Least Citations
   Show papers with more than a certain amount of citations.

3. Citations & Relationship
   The quality of nodes are defined by its number of citations and how related to the quering paper.


- Bot Detection

No need to be rude. 

1. Just wait for certain seconds (10 ~ 20) for each access (YES, you can avoid detection but being polite always pays)

2. Set user-agent to Mozilla Firefox/5.0, which is also used for Googlebots.






