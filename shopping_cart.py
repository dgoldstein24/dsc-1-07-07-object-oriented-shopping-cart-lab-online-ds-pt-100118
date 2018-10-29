class ShoppingCart:
    def __init__(self, discount = None):
        self._total = 0
        self._items = []
        self._employee_discount = discount

    def total(self):
        return self._total
    
    def items(self):
        return self._items
    
    def employee_discount(self):
        return self._employee_discount
    
    def add_item(self, item, price, quantity = None):
        if quantity is None:
            self._total += price
            self._items.append({item: {price : 1}})
        else: 
            self._total += price * (quantity)
            self._items.append({item: {price : quantity}})
        return self._total
    
    def mean_item_price(self):
        number_of_items = 0
        for grocery in self._items:
            items = list(grocery.keys())
            for item in items:
                price_and_quantity = grocery[item]
                prices = list(price_and_quantity.keys())
                for price in prices:
                    number_of_items += price_and_quantity[price]
        return self._total / number_of_items  
    
    def median_item_price(self):
        list_of_prices = []
        for grocery in self._items:
            items = list(grocery.keys())
            for item in items:
                price_and_quantity = grocery[item]
                prices = list(price_and_quantity.keys())
                for price in prices:
                    for count in range(0, price_and_quantity[price]):
                        list_of_prices.append(price)
        sorted_prices = sorted(list_of_prices)
        length = len(sorted_prices)
        if length % 2 == 0:
            return (sorted_prices[int(length/2)] + sorted_prices[int((length/2)+1)]) / 2
        elif length % 2 == 1:
            return sorted_prices[int(length/2)]
  
    def apply_discount(self):
        if self._employee_discount is None:
            return "Sorry, there is no discount to your cart :("
        else:
            return self._total * ((100 - self._employee_discount) / 100)
   
    def item_names(self):
        list_of_items = []
        for grocery in self._items:
            items = list(grocery.keys())
            for item in items:
                price_and_quantity = grocery[item]
                prices = list(price_and_quantity.keys())
                for price in prices:
                    for count in range(0, price_and_quantity[price]):
                        list_of_items.append(item)
        return list_of_items
    
    def void_last_item(self):
        if len(self._items) == 0:
            return "There are no items in your cart!"
        else:
            last_item = self._items[-1]
            #{burger: {price : quantity}}
            key = list(last_item.keys())[0]
                #burger
            price_key = list(last_item[key].keys())[0]
                   #price
            quantity_value = last_item[key][price_key]
                    #value
            self._total -= price_key
            last_item[key][price_key] -= 1
            if last_item[key][price_key] == 0:
                self._items.pop()
        return
