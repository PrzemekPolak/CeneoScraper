class Product:
    def __init__(self, product_id, name, opinions=[] ):
        self.product_id = product_id
        self.name = name
        self.opinions = opinions
    
    def __str__(self):
        return (f'Product_id: {self.product_id}\nName: {self.name}\nOpinions:\n'.join(str(opinion) for opinion in self.opinions)
        #return (f'Product_id: {self.product_id}\nName: {self.name}\nOpinions:\n{[str(opinion) for opinion in self.opinions]}'



class Opinion:
    #słownik z składowymi opinii
    tags = {
    "author": ["div",  "reviewer-name-line"],
    "recommendation": ["div", "product-review-summary", 'em'],
    "stars": ['span', 'review-score-count'],
    "purchased": ['div','product-review-pz', 'em'],
    "useful": ['button', 'vote-yes', 'span'],
    "useless": ['button', 'vote-no', 'span'],
    "content": ['p', 'product-review-body'],
    "pros": ['div', 'pros-cell', 'ul'],
    "cons": ['div', 'cons-cell', 'ul']
    }

    #definicja konstruktora klasy
    def __init__(self, opinion_id=None, author=None, recommendation=None, stars=None, content=None, pros=None, cons=None,
                useful=None, useless=None, purchased=None, purchased_date=None, review_date=None):
        self.opinion_id = opinion_id
        self.author = author
        self.recommendation = recommendation
        self.stars = stars
        self.content = content
        self.pros = pros
        self.cons = cons
        self.useful = useful
        self.useless = useless
        self.purchased = purchased
        self.purchased_date = purchased_date
        self.review_date = review_date

    def __str__(self):
        return f'Opinion_id: {self.opinion_id}\nAuthor: {self.author}\n'

    def extract_opinion():
        pass


opinion = Opinion()
print(opinion)
product = Product(None, None, opinions=[opinion])
print(product)