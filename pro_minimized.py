import networkx as nx
import re
import matplotlib.pyplot as plt
import PyPDF2 
from networkx.algorithms import community
from collections import Counter

# Defining variables
G, G1, G2 = nx.DiGraph(), nx.DiGraph(), nx.DiGraph()
pdfFileObj = open('WebPage.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
pages=pdfReader.numPages
a,b,c,d,e = [],[],[],[],[]

chapter_pages = [0, 48, 68, 108, 128, 154, 192, 226, 252, 280, 422, 470, 504];

# Generating Nodes for the Graph takes parameter as chapter number

def generate_nodes(chapter_number):

    text = "" # Contains text of input chapter
    if (chapter_number == 100):
        for x in range(1, 14):
            generate_nodes(x);
    else:
        page_start = chapter_pages[chapter_number - 1] # starting page of the chapter
        page_end = chapter_pages[chapter_number] - 1 # ending page of the chapter

    # looping over all the pages
    while page_start<page_end:
        pageObj = pdfReader.getPage(page_start) # reading text from current page
        text += pageObj.extractText().replace('\n','') # append extracted text to variable text
        pattern=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}|\[Post\.\d|\[Def\.\d{1,2}\.\d{1,3}|\[C\.N\.\d)",text) # regex pattern to find in the book

        # looping through the pattern to distinguish among Proposition, Postulates, Definitions and Common Notions
        i=0 # loop counter

        while i<len(pattern):
            if "Proposition" in pattern[i]:
                e=pattern[i].replace('Proposition','')
                m=str(chapter_number)+"."+e
                a.append(m) # append Proposition to list a
            elif "[Prop." in pattern[i]:
                t=pattern[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m)) # append above used proposition in b
            elif "[Post." in pattern[i]:
                y=pattern[i].replace('[Post.','p')
                x=y.replace(']','')
                b.append((x,m)) # append above used postulates in b
            elif "[Def." in pattern[i]:
                y=pattern[i].replace('[Def.','d')
                x=y.replace(']','')
                b.append((x,m)) # append above used definitions in b
            elif "[C.N." in pattern[i]:
                y=pattern[i].replace('[C.N.','c')
                x=y.replace(']','')
                b.append((x,m)) # append above used common notions in b
            i+=1 # increment the loop counter
        page_start+=1 # go to next page
    G.add_nodes_from(a)  # append list a in Graph G
    G.add_edges_from(b)  # append list b in Graph G


num=input("Enter chapter number: (1-13) and 100 for complete book :- ")
generate_nodes(int(num))

nx.draw(G,with_labels = True, node_color = 'r')
plt.show()
in_degrees=list(G.in_degree(list(G.nodes)))
out_degrees=list(G.out_degree(list(G.nodes)))
print("in degrees of all the nodes:",in_degrees)
print('--------------------------------------------------------------------')
print("out degrees of all the nodes:",out_degrees)
print('--------------------------------------------------------------------')
print("communities:")

communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)
coms=sorted(map(sorted, next_level_communities))
for i in coms:
    print(i)
print('--------------------------------------------------------------------')

def lin_eq(z):
    if G.in_degree(z)==0:
        d.append(z)
    else:
        for i in list(G.predecessors(z)):
            c.append((i,z))
            lin_eq(i)

num1=input("Enter the node:")
lin_eq(num1)
G1.add_edges_from(c)
nx.draw(G1,with_labels = True, node_color = 'r')
plt.show()
print("linear combinations for 1.33 is:",Counter(d))
pdfFileObj.close() 
