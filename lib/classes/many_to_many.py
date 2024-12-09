
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
        self._title = new_title
        if hasattr(self, "title"):
            AttributeError("Tittle cannot be changed")
        else:
            if isinstance (new_title, str):
                if 5 <= len(new_title) <= 50:
                  self._title = new_title    
                else:
                    ValueError("Title must be between 5 and 50 characters")
            else:
                TypeError("Title must be a string")

    @property
    def author(self)  :
        return self._author         
            
        
class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass