import networkx as nx
import re
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
    elif pa==100:
        chapter(1)
        chapter(2)
        chapter(3)
        chapter(4)
        chapter(5)
        chapter(6)
        chapter(7)
        chapter(8)
        chapter(9)
        chapter(10)
        chapter(11)
        chapter(12)
        chapter(13)
    while count<pag:
        pageObj = pdfReader.getPage(count)
        text += pageObj.extractText().replace('\n','')
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}|\[Post\.\d|\[Def\.\d{1,2}\.\d{1,3}|\[C\.N\.\d)",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m=str(pa)+"."+e
                a.append(m)
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
        count+=1
    G.add_nodes_from(a)
    G.add_edges_from(b)
    #k=list(set(a) - set(list(G.nodes)))
#num is taking input from user of the chapter number
num=input("Enter chapter number:")
chapter(int(num))
#next line is drawing graph with nodes being depicted as red
nx.draw(G,with_labels = True, node_color = 'r')
plt.show()
#in_degrees computes and stores number of incoming edge to each node
in_degrees=list(G.in_degree(list(G.nodes)))
#out_degrees computes and stores number of outgoing edge to each node
out_degrees=list(G.out_degree(list(G.nodes)))
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
#def ispresent(z,z1):
#    if G.in_degree(z)==0:
#        e.append(z)
#    elif z==z1:
#        return 0
#    else:
#        for i in list(G.predecessors(z)):
#            c.append((i,z))
#            ispresent(i)
#    print("not present")
#ispresent(1.33,1.1)
#G1.add_edges_from(e)
#nx.draw(G2,with_labels = True, node_color = 'r')
#plt.show()
print("linear combinations for 1.33 is:",Counter(d))
pdfFileObj.close() 
