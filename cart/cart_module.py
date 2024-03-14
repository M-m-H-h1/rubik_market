from products.models import Products


CART_SESSION_ID = 'cart'

class Cart():

    def __init__(self,request):
        self.session = request.session

        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart



    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            product = Products.objects.get(id=int(item['id']))
            item['product'] = product
            item['total'] = int(item['quantity']) * int(item['price'])
            item['unique_id'] = self.unique_id_generator(product.id, item['color'], item['memory'])
            yield item


    def unique_id_generator(self, id, color, size):
        result = f'{id}-{color}-{size}'
        return result


    def add(self,product,color,quantity,memory):
        unique = self.unique_id_generator(product.id, color, memory)
        if product.discount_percent:
            if unique not in self.cart:
                self.cart[unique] = {'quantity': 0,'main_price':str(product.price), 'price': str(product.Price_after_discount), 'color': color, 'memory': memory,'id': str(product.id)}
        else:
            if unique not in self.cart:
                self.cart[unique] = {'quantity': 0,'main_price':str(product.price),'price': str(product.price), 'color': color, 'memory': memory,'id': str(product.id)}


        self.cart[unique]['quantity'] += int(quantity)
        self.save()

    def save(self):
        self.session.modified = True


    def delete(self, id):
        if id in self.cart:
            del self.cart[id]
            self.save()

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def final_price_total(self):
        cart = self.cart.values()
        total = sum(int(item['price']) * int(item['quantity']) for item in cart)
        return total

    def total_price(self):
        cart = self.cart.values()
        total = sum(int(item['main_price']) * int(item['quantity']) for item in cart)
        return total

    def total_discount(self):
        cart = self.cart.values()
        total_price = sum(int(item['main_price']) * int(item['quantity']) for item in cart)
        total_price_after_dis = sum(int(item['price']) * int(item['quantity']) if item['price'] is not None else int(
            item['main_price']) * int(item['quantity']) for item in cart)
        total = total_price - total_price_after_dis
        return total

    def remove_cart(self):
        del self.session[CART_SESSION_ID]

