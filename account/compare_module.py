from products.models import Products
from django.core import serializers

class CompareProduct():


    def __init__(self, request):
        self.session = request.session

        compare = self.session.get('compare')
        if not compare:
            compare = self.session['compare'] = {}
        self.compare = compare

    def __iter__(self):
        fav = self.compare.copy()

        for item in fav.values():
            product = Products.objects.get(id=int(item['id']))
            item['product'] = product
            yield item


    def add(self, product):

        self.compare[product.id] = {'id': str(product.id)}
        self.save()

    def save(self):
        self.session.modified = True


    def delete(self, id):
        if id in self.compare:
            del self.compare[id]
            self.save()

    def remove_cart(self):
        del self.session['fav']




