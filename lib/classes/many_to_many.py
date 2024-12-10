
class Article:
    all = []
    def __init__(self, author, magazine, title):

        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title   

    @title.setter
    def title(self, new_title):
        if hasattr(self, "title"):
            AttributeError("Title cannot be changed")
        else:
            if isinstance(new_title, str):
               if 5 <=  len(new_title ) <=50:
                self._title = new_title
               else:
                ValueError("Title must be between 5 and 50 characters")
            else:
                TypeError("Title must be a string")

    @property
    def author(self):
        return self._author 

    @author.setter
    def author(self, new_author):
        if isinstance (new_author, Author):
                self._author = new_author  
        else:
                TypeError("Author must be an instance of Author") 

    @property
    def magazine(self):
        return self._magazine  

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine  = new_magazine   
        else:
            TypeError("Magazine must be an instance of Magazine")           

    
class Author:
    def __init__(self, name):
        self.name = name

    @ property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if hasattr(self, "name"):
            AttributeError("Name cannot be changed")
        else:
            if isinstance(new_name, str):
                if len(new_name):
                    self._name = new_name
                else:
                    ValueError("Name must be longer than 0 characters")
            else:
                    TypeError("Name must be a string")


    def articles(self):
        return [article for article in Article.all if self == article.author]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topic_areas = list({magazine.category for magazine in self.magazines()})
        if topic_areas:
            return topic_areas
        else:
            return None

class Magazine:

    all = []
     

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)


    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16 :
                self._name = new_name  
            else:
                ValueError("Name must be between 2 and 16 characters")
        else:
            TypeError("Name must be a string")                 

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass