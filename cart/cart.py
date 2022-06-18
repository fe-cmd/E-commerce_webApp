from store.models import Product
from decimal import Decimal
from checkout.models import DeliveryOptions
from django.conf import settings

class Cart():
    """
    A base Cart class , providing some default behaviours that
    can be inherited or overrided, as neccessary.
    """
    def __init__(self, request):
        
       self.session = request.session
       cart = self.session.get(settings.CART_SESSION_ID)
       if settings.CART_SESSION_ID not in request.session:
           cart = self.session[settings.CART_SESSION_ID] = {}
       self.cart = cart
       
    def add(self, product, qty):
        """
        Adding and updating the users cart session data
        """
        product_id = str(product.id)
        
        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        else:
            self.cart[product_id] = {'price': str(product.regular_price), 'qty':qty}
        
        self.save()
        
    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product'] = product
            
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item
            
    def __len__(self):
        """
        Get the cart data and count the qty of items
        """
        return sum(item['qty'] for item in self.cart.values())
    
    def get_subtotal_price(self):
        return sum(Decimal(item["price"]) * item["qty"] for item in self.cart.values())

    def get_delivery_price(self):
        newprice = 0.00

        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price

        return newprice
    
    def get_total_price(self):
        newprice = 0.00
        subtotal = sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
        
        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price
            
        total = subtotal + Decimal(newprice)
        return total
    
    
    def cart_update_delivery(self, deliveryprice=0):
        subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.cart.values())
        total = subtotal + Decimal(deliveryprice)
        return total
    
    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)
        
        if product_id in self.cart:
            del self.cart[product_id]
            print(product_id)
            self.save()
            
    def update(self, product, qty):
        """
        Update values session data
        """
        product_id = str(product)
        
        if product_id in self.cart:
            self.cart[product_id]['qty'] =  qty
            
        self.save()
        
        
    def clear(self):
        #Remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()
            
    def save(self):
        self.session.modified = True
        
        
        
        
       