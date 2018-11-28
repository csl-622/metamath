import networkx as nx
import string
import re
import csv
import matplotlib.pyplot as plt
import PyPDF2 
from operator import itemgetter
from networkx.algorithms import community
from collections import Counter
import firebase_admin
from firebase_admin import credentials,firestore
cred = credentials.Certificate('./metamath_database.json')
default_app=firebase_admin.initialize_app(cred)
db =firestore.client()
collection_ref=db.collection(u'nodes')
pdfFileObj = open('WebPage.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
pages=pdfReader.numPages
G=nx.DiGraph()
a=[]
b=[]
d=[]
c=[]
e=[]

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
for i in a:
	ined=[]
	outed=[]
	for j in list(G.in_edges(i)):
		ined.append(j[0])
	for k in list(G.out_edges(i)):
		outed.append(k[1])
	lenin=len(ined)
	lenout=len(outed)
	collection_ref.document(i).set({'in_edges':ined, 'out_edges':outed, 'in_degree':lenin, 'out_degree':lenout})
			
pdfFileObj.close() 














