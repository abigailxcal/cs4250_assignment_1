#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/
#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
#AS numpy OR pandas. You have to work here only with standard arrays
#Importing some Python libraries

import csv
import math
documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: # skipping the header
            documents.append(row[0])
#print(documents)

# for each document, turn it's string into a list and put into a container of all documents 

docs =[]
for line in documents:
    docs.append(line.split())
#print(docs)



def print_docs(D):
    for index,D in enumerate(D):
        print(f'\tDocument {index+1}: {D}')

print('Original Document Contents:')
print_docs(docs)
#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define
#your stopwords.
#--> add your Python code here
stopWords = {"nor","yet","and", "but", "or", "because'", "although", "since", "if", "when","she","her", "he", "they" ,"their", "we", "i", "you", "it", "who"}
for i in range(len(docs)):
    mylist = []
    #print(document_words[i])
    for j in range(len(docs[i])):
        if docs[i][j].lower() not in stopWords:
            #print(f'{doc1[i][j]} not removed')
            mylist.append(docs[i][j])
    docs[i]=mylist
print('Document contents after stopword removal: ')
print_docs(docs)


#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {'lov': ['loved','loves', 'lover', 'loving','love'],
            'cat': ['cats'],
            'dog': ['dogs','doggie','doggy','doggies']
            }

for i in range(len(docs)):
    mylist = []
    for j in range(len(docs[i])):
        for k,v in stemming.items():
            if k in docs[i][j].lower() and docs[i][j].lower() in v: 
                docs[i][j]=k
print(f'Document contents after stemming: ')
print_docs(docs)




#Identifying the index terms.
#--> add your Python code here
terms = []
for doc in docs:
    for word in doc:
        if word not in terms:
            terms.append(word)
print(f'Terms: {terms}')

# tf(t,d) is the relative frequency of term t within document d
def tf(term,d):
    total_terms = len(d)
    freq_count = 0
    for word in d:
        if word == term:
            freq_count+=1
    #print(f'Total terms within doc: {total_terms}\n"{term}" count: {freq_count}')
    #print(f'tf: {freq_count/total_terms} for {term} in {d}')
    return freq_count/total_terms


#df(t, D), is the number of documents in the document set D in which the term t appears
def df(term,D):
    total_doc_count = len(D)
    term_count = 0
    for doc in D:
        if term in doc:
            #print(f'Term: {term} found in {doc}')
            term_count +=1 
    #print("df: ",term_count, "for term ",term) 
    return term_count

#idf(t, D), is the logarithmically (base 10) scaled inverse fraction of the documents D that contain the term t
def idf(term,D):
    a = math.log10( (len(D))/df(term,D) )
    #print("idf: ",a, "for term ",term)
    return round(a,2)
#print(idf('cat',docs))

def tf_idf(term,d,D):
    #print("tf-idf: ",tf(term,d)*idf(term,D), " for term ",term, " and doc ",d)
    return tf(term,d)*idf(term,D)


#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []

for doc in docs:
    term_count = []
    for term in terms:
        term_count.append(tf_idf(term,doc,docs))
    docTermMatrix.append(term_count)



#Printing the document-term matrix.
#--> add your Python code here
num = 1
column_width = 10
print(f"{'Doc-Term Matrix':<{column_width}} | {'Term 1':<{column_width}} | {'Term 2':<{column_width}} | {'Term 3':<{column_width}} |")
print("-" * (column_width * 5 + 16))
for r in range(len(docTermMatrix)):
    print(f"{'     Document ' + str(num):<{column_width}} | ", end="")
    for c in range(len(docTermMatrix[r])):
        print(f"{docTermMatrix[r][c]:<{column_width}} | ", end="")
    print("")
    num+=1

tf_matrix = []
for d in docs:
    myList = []
    for t in terms:
        #myList.append(tf(t,d))
        #myList.append(df(t,docs))
        myList.append(idf(t,docs))
    #print(myList)
