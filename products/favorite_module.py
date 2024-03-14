from products.models import Products
from django.core import serializers

class FavoriteProduct():


    def __init__(self, request):
        self.session = request.session

        fav = self.session.get('fav')
        if not fav:
            fav = self.session['fav'] = {}
        self.fav = fav

    def __iter__(self):
        fav = self.fav.copy()

        for item in fav.values():
            product = Products.objects.get(id=int(item['id']))
            item['product'] = product
            yield item


    def add(self, product):

        self.fav[product.id] = {'id': str(product.id)}
        self.save()

    def save(self):
        self.session.modified = True


    def delete(self, id):
        if id in self.fav:
            del self.fav[id]
            self.save()

    def remove_cart(self):
        del self.session['fav']

def __len__(self):
    return sum(item['quantity'] for item in self.cart.values())


