class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self._author = author
        # self._title = None
        self.author = author 
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50:
            self._title = new_title
        else:
            print(f'Invalid title: {new_title}')
   
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):  
            self._author = new_author
        else:
            print(f'Invalid author: {new_author}. Must be an instance of Author.')

    # @property
    # def author(self):
    #     return self._author

    # @author.setter
    # def author(self, new_author):
    #     if isinstance(new_author, Author):
    #         self._author = new_author
    #     else:
    #         print(f'Invalid author: {new_author}. not in Author class.')
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            print(f'Invalid: {new_magazine}. not Magazine.')

    def __repr__(self):
        return f"<Article author={self.author.name}, magazine={self.magazine.name}, title={self.title}>"

class Author:
    all = []
    def __init__(self, name):
        # self._articles = []
        # self._name = None  
        self.name = name 
        # self.article = article
        Author.all.append(self)

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 1 and not hasattr(self, '_name'):
            self._name = new_name
        else:
            print(f'Invalid name: {new_name}')

    name = property(get_name, set_name)


    def articles(self):
        article_by = []
        for article_obj in Article.all:
            if article_obj.author is self:
                article_by.append(article_obj)
        return article_by

   ##NOT WORKING --- 
    def magazines(self):
        auth_mag_set = set()  # Use a set to store unique magazine objects
        for mag in Article.all:
            if mag.author is self:
                auth_mag_set.add(mag.magazine)
        return list(auth_mag_set)


    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        categories = set()
        for article in self.articles():
            categories.add(article.magazine.category)
        return list(categories) if categories else None

    def __repr__(self):
        return f"<Author name={self.name}>"

class Magazine:
    all = []
    def __init__(self, name, category):
        # self._name = None
        # self._category = None  # Initialize _category attribute
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            print(f'Invalid name: {new_name}')

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            print(f'Invalid category: {new_category}')

    def articles(self):
        mag_article_list = []
        for mag_article_obj in Article.all:
            if mag_article_obj.magazine is self:
                mag_article_list.append(mag_article_obj)
        return mag_article_list

    def contributors(self):
        contributors_set = set()
        for article in self.articles():
            contributors_set.add(article.author)
        return list(contributors_set)
    # Returns a unique list of authors who have written for this magazine
# Must be of type Author
        

    def articles(self):
        mag_article_list = []
        for mag_article_obj in Article.all:
            if mag_article_obj.magazine is self:
                mag_article_list.append(mag_article_obj)
        return mag_article_list

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1

        contributing_authors = []
        # new_count = []
        for new_count in author_counts:
            if author_counts[new_count] > 2:
                contributing_authors.append(new_count)

        if contributing_authors:
            return contributing_authors
        else:
            return None

    def __repr__(self):
        return f"<Magazine name={self.name}, category={self.category}>"



###----------------------
    
Author1 = Author('Mike')
print(Author1)
Author2 = Author('Ben')
print(Author2)

mag1 = Magazine("time", "News")
print(mag1)

art1 = Article(Author1, mag1, "Follow Me")
print(art1)

print(f"Magazines for {Author1.name}: {Author1.magazines()}")

print(Author1)


