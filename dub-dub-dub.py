from google import search

query = "geeksteev"

for i in search(query=query,tld='co.in',lang='en',num=10,stop=1,pause=2):
    print(i +'\n')


# # Performing google search using Python code
# class Gsearch_python:
#    def __init__(self,name_search):
#       self.name = name_search
#    def Gsearch(self):
#       count = 0
#       try :
#          from google import search
#       except ImportError:
#          print("No Module named 'google' Found")
#       for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=1,pause=2):
#          count += 1
#          print (count)
#          print(i + '\n')
# if __name__=='__main__':
#    gs = Gsearch_python("Tutorialspoint Python")
#    gs.Gsearch()