
import networkx as nx
import string
import re
import csv
import matplotlib.pyplot as plt
import PyPDF2 
from networkx.algorithms import community
from collections import Counter
#G is chapter graph having propositions,postulates,definations and common notions as vertices.G is a directed graph.
G=nx.DiGraph()
#G1 is the graph of the certain nodes(Nodes which form a tree leading to certain node)
G1=nx.DiGraph()
G2=nx.DiGraph()
#Following line is used to read book pdf as input
pdfFileObj = open('WebPage.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
#pages stores number of pages in the pdf
pages=pdfReader.numPages
# a contains the nodes of the final graph
a=[]
#b contains the edges of the final graph
b=[]
#d is used to store linear combination of a proposition
d=[]
c=[]
e=[]
# chapter function takes chapter number as input and prints the graph of that chapter. If you input 100 as chapter number it will print the graph of the whole book
#count is tha page at which the given chapter is starting
#pa is the page at which chapter ends
#text store all the text in the chapter
# else if statement checks pa variable whcich chapter is representing to choose the value of count and page to read and print the graph
#somo stores all the text which we have to make node in our graph 
# we have used to while loop to iterate from starting page numbe to ending page number for making graph
def chapter(pa):
    global count
    global pag
    text=""
    if pa==1:
        count=0
        pag=47
    elif pa==2:
        count=48
        pag=67
    elif pa==3:
        count=68
        pag=107
    elif pa==4:
        count=108
        pag=127
    elif pa==5:
        count=128
        pag=153
    elif pa==6:
        count=154
        pag=191
    elif pa==7:
        count=192
        pag=225
    elif pa==8:
        count=226
        pag=251
    elif pa==9:
        count=252
        pag=279
    elif pa==10:
        count=280
        pag=421
    elif pa==11:
        count=422
        pag=469
    elif pa==12:
        count=470
        pag=503
    elif pa==13:
        count=504
        pag=539
    elif pa==100 or pa==113:
        for i in range(1,14):
        	chapter(i)
    elif pa==101:
        chapter(1)
    elif pa==102:
        for i in range(1,3):
        	chapter(i)
    elif pa==103:
        for i in range(1,4):
        	chapter(i)
    elif pa==104:
        for i in range(1,5):
        	chapter(i)
    elif pa==105:
        for i in range(1,6):
        	chapter(i)
    elif pa==106:
        for i in range(1,7):
        	chapter(i)
    elif pa==107:
        for i in range(1,8):
        	chapter(i)
    elif pa==108:
        for i in range(1,9):
        	chapter(i)
    elif pa==109:
        for i in range(1,10):
        	chapter(i)
    elif pa==110:
        for i in range(1,11):
        	chapter(i)
    elif pa==111:
        for i in range(1,12):
        	chapter(i)
    elif pa==112:
        for i in range(1,13):
        	chapter(i)
    while count<=pag:
        pageObj = pdfReader.getPage(count)
        #text += pageObj.extractText().encode('ascii', 'ignore').decode().replace('\n','')
        text += pageObj.extractText().replace('\n','')
        #text=re.sub('^[\x00-\x7F]', '', text)
        count+=1
    somo=re.findall("(?:Proposition\d{1,3}|Corollary|Lemma|\[Prop\.\d{1,2}\.\d{1,3}corr.|\[Prop\.\d{1,2}\.\d{1,3}|\[Post\.\d|\[Def\.\d{1,2}\.\d{1,3}|\[C\.N\.\d)",text)
    i=0
    while i<len(somo):
        if "Proposition" in somo[i]:
            e=somo[i].replace('Proposition','')
            m=str(pa)+"."+e
            a.append(m)
        elif "Corollary" in somo[i]:
            temp=m
            m="corr"+m
            b.append((temp,m))
        elif "Lemma" in somo[i]:
            temp=m
            m="le"+m
            b.append((temp,m))
        elif "corr." in somo[i]:
            yy=somo[i].replace('corr.','')
            yy=yy.replace('[Prop.','')
            yy="corr"+yy
            b.append((yy,m))
        elif "[Prop." in somo[i]:
            t=somo[i].replace('[Prop.','')
            p=t.replace(']','')
            b.append((p,m))
        elif "[Post." in somo[i]:
            y=somo[i].replace('[Post.','p')
            x=y.replace(']','')
            b.append((x,m))
        elif "[Def." in somo[i]:
            y=somo[i].replace('[Def.','d')
            x=y.replace(']','')
            b.append((x,m))
        elif "[C.N." in somo[i]:
            y=somo[i].replace('[C.N.','c')
            x=y.replace(']','')
            b.append((x,m))
        i+=1
    G.add_nodes_from(a)
    G.add_edges_from(b)
    #k=list(set(a) - set(list(G.nodes)))
#num is taking input from user of the chapter number

num=input("Enter chapter number:")
chapter(int(num))
with open('test.csv', 'w+') as csvFile:
    writer=csv.writer(csvFile)
    row=['Source','Target']
    writer.writerow(row)
    for i in G.edges():
        writer.writerow(list(i))    
csvFile.close()
#next line is drawing graph with nodes being depicted as red
nx.draw(G,with_labels = True, node_color = 'r')
plt.show()
#in_degrees computes and stores number of incoming edge to each node
in_degrees=list(G.in_degree(list(G.nodes)))
#out_degrees computes and stores number of outgoing edge to each node
out_degrees=list(G.out_degree(list(G.nodes)))
with open('indegree.csv', 'w+') as csvFile:
    writer=csv.writer(csvFile)
    for i in in_degrees:
        writer.writerow(list(i))    
csvFile.close()
with open('outdegree.csv', 'w+') as csvFile:
    writer=csv.writer(csvFile)
    for i in out_degrees:
        writer.writerow(list(i))    
csvFile.close()
print("in degrees of all the nodes:",in_degrees)
print('--------------------------------------------------------------------')
print("out degrees of all the nodes:",out_degrees)
print('--------------------------------------------------------------------')
abc=[]
abc1=[]
for i in in_degrees:
    if i[1]==0:
        abc.append(i[0])
print("the nodes with in degree 0:",abc)
print("number of nodes with in degree 0:",len(abc))
print('--------------------------------------------------------------------')
for i in out_degrees:
    if i[1]==0:
        abc1.append(i[0])
print("the nodes with 0 out degree:",abc1)
print("number of nodes with 0 out degree :",len(abc1))
print('--------------------------------------------------------------------')
print("communities:")
#the folowing few lines compute the communities which exist in graph which we have printed
#the algorithm used here is girvan newman but we still don't know the threshold used to compute the communities
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)
coms=sorted(map(sorted, next_level_communities))
for i in coms:
    print(i)
print('--------------------------------------------------------------------')
#lin_eq computes the linear combination of a proposition
#linear combination means the how many basic postulates,definations and common notions are used to compute the path to nodes of the graph
def lin_eq(z):
    if G.in_degree(z)==0:
        d.append(z)
    else:
        for i in list(G.predecessors(z)):
            c.append((i,z))
            lin_eq(i)
#example for linear combination
num1=input("Enter the node:")
lin_eq(num1)
G1.add_edges_from(c)
nx.draw(G1,with_labels = True, node_color = 'r')
plt.show()
print("linear combinations for ",num1," is:",Counter(d))

pdfFileObj.close() 
