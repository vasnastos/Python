class book:
  def __init__(self,autt,autn,pr):
      self.author=autn
      self.title=autt
      self.price=pr
  def get_author(self): 
      return self.author
  def set_price(self,value):
      self.price=value 
  def get_title(self):
    return self.title
  def get_price(self):
    return self.price
  def to_str(self):
      return self.author+"-"+self.title+"-"+str(self.price)
  def is_Hardpad(self):
        if float(self.price)>60.0:
              return True
        else:
              return False

def show_books(data):
     for x in data:
         print(x.to_str())

def open_books(data):
      file=open("books.txt","r")
      for x in file:
            token=x.split(",")
            if len(token)!=3:
                  continue;
            newbook=book(token[0],token[1],token[2])
            data.append(newbook)

def expensive_book(data):
      max=data[0]
      for y in range(1,len(data)):
            if data[y].get_price()>max.get_price():
                  max=data[y]
      return max

def find_unique_authors(data):
      authors=[]
      found=False
      for x in data:
            for y in authors:
             if x.get_author()==y:
                   found=True
                   break
            if found==False:
                  authors.append(x.get_author())
      return authors

def insert_book(data):
      author=input("Give book's name:")
      title=input("Give title:")
      price=input("Give price of book:")
      newbook=book(title,author,price)
      for x in data:
            if str(x.get_title())==str(title):
                  print("Book already exists in list!!!")
                  return
      data.append(newbook)

def show_books_per_author(data):
      books=find_unique_authors(data)
      for y in books:
            for x in data:
                  if str(y)==str(x.get_author()):
                        print(x.to_str())

def save_to_file(data):
      filename=input("Give filename:")
      file=open(filename,"w")
      for x in data:
            if x.is_Hardpad():
              x.set_price(float(x.get_price())*1.20)
      for k in data:
            file.write(k.to_str())
      file.close()

def start():
      books=[]
      open_books(books)
      for x in range(0,5):
            insert_book(books)
      show_books(books)
      show_books_per_author(books)
      save_to_file(books)
      print("Most Expensive:"+expensive_book(books).to_str())

#Κύριο κομμάτι κώδικα!!!

start()
