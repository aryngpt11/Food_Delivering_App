from django.shortcuts import render
from django.views import View  #class based views
from customer.models import *
#allows you to define views with greater flexibility and reusability compared to function-based views. Using class-based views can help organize your code better, particularly for complex views that require a lot of functionality. Here's an overview of the benefits and uses of defining a class-based view like
# Create your views here.

#This refers to the instance of the class (Index in this case). It is a conventional name used in object-oriented programming to access attributes and methods of the class.
#This is an instance of HttpRequest provided by Django. It contains metadata about the request made by the user, including HTTP method, headers, body data, user information, and more.
#This stands for "arguments" and allows the method to accept any number of additional positional arguments. It is a way to handle more arguments than the ones explicitly defined.
#This stands for "keyword arguments" and allows the method to accept any number of additional keyword arguments. It is a way to handle named arguments that are not explicitly defined in the method signature.
        


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
       
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html') 



class Order(View):
    def get(self, request, *args, **kwargs):
        # Get every item from each category
        appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
        entrees = MenuItem.objects.filter(category__name__contains='Entre')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')

        # Pass into context
        context = {
            'appetizers': appetizers,
            'entrees': entrees,
            'desserts': desserts,
            'drinks': drinks
        }

        # Render the template with the context
        return render(request, 'order.html', context)

    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }
            order_items['items'].append(item_data)
        
        price = sum(item['price'] for item in order_items['items'])
        item_ids = [item['id'] for item in order_items['items']]
        
        order = OrderModel.objects.create(price=price)
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price
        }
        return render(request, 'order_confirmation.html', context)