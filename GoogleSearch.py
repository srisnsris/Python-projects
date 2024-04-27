from googlesearch import search

query = ("Srinivas Vuppala Linkedin")  #text srinivas

for i in search(query, start = 0, stop = 10 , pause = 2.0):  #sto top 15 none
    print(i)
    