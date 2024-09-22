import csv
import math

documents = []
#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: # skipping the header
            documents.append(row[0])


def print_docs(D):
    for index,D in enumerate(D):
        print(f'\tDocument {index+1}: {D}')

# for each document, turn it's string into a list and put into a container of all documents 
docs = [line.split() for line in documents]

print('Original Document Contents:')
print_docs(docs)

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define
#your stopwords.
#--> add your Python code here
stopWords = {"nor","yet","and", "but", "or", "because'", "although", "since", "if", "when","she","her", "he", "they" ,"their", "we", "i", "you", "it", "who"}
for i in range(len(docs)):
    mylist = []
    for j in range(len(docs[i])):
        if docs[i][j].lower() not in stopWords:
            mylist.append(docs[i][j])
    docs[i]=mylist

print('Document contents after stopword removal: ')
print_docs(docs)


#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
stemming = {'love': ['loved','loves', 'lover', 'loving','love'],
            'cat': ['cats'],
            'dog': ['dogs','doggie','doggy','doggies']
}

for i in range(len(docs)):
    mylist = []
    for j in range(len(docs[i])):
        for stem, variations in stemming.items():
            if docs[i][j].lower() in variations:
                docs[i][j] = stem
print(f'Document contents after stemming: ')
print_docs(docs)


#Identifying the index terms.
terms = []
for doc in docs:
    for word in doc:
        if word not in terms:
            terms.append(word)
print(f'Terms: {terms}')

# tf(t,d) is the relative frequency of term t within document d
def tf(term,d):
    return d.count(term)/len(d)


#df(t, D), is the number of documents in the document set D in which the term t appears
def df(term,D):
    term_count = 0
    for doc in D:
        if term in doc:
            term_count +=1 
    return term_count

#idf(t, D), is the logarithmically (base 10) scaled inverse fraction of the documents D that contain the term t
def idf(term,D):
    return round(math.log10( (len(D))/df(term,D) ),2)

def tf_idf(term,d,D):
    return tf(term,d)*idf(term,D)


#Building the document-term matrix by using the tf-idf weights.
docTermMatrix = []
for doc in docs:
    term_count = []
    for term in terms:
        term_count.append(tf_idf(term,doc,docs))
    docTermMatrix.append(term_count)


#Printing the document-term matrix.
num = 1
column_width = 10
print(f"{'Doc-Term Matrix':<{column_width}} | " + " | ".join(f"{term:<{column_width}}" for term in terms) + " |")
print("-" * (column_width * 5 + 16))
for r in range(len(docTermMatrix)):
    print(f"{'     Document ' + str(num):<{column_width}} | ", end="")
    for c in range(len(docTermMatrix[r])):
        print(f"{docTermMatrix[r][c]:<{column_width}} | ", end="")
    print("")
    num+=1


