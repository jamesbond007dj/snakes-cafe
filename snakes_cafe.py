s = f"""
{'*'*35}

{'*'*2} Welcome to the Snakes Cafe! {'*'*2}

{'*'*2} Please see our menu below. {'*'*2}

{'*'*2} 

{'*'*2}To quit at any time, type"quit"{'*'*2} 

{'*'*35}

Appetizers

{'-'*6}

Wings

Cookies

Spring Rolls

Entrees

{'-'*6}

Salmon

Steak

Meat Tornado

A Literal Garden

Desserts

{'-'*6}

Ice Cream

Cake

Pie

Drinks

{'-'*6}

Coffee

Tea

Unicorn Tears


{'*'*35}

{'*'*2} What would you like to order? {'*'*2} 

{'*'*35}

"""
print(s)

import sys

menu = {
    'Wings': 0,
    'Cookies': 0,
    'Spring Rolls': 0,
    'Salmon': 0,
    'Steak': 0,
    'Meat Tornado': 0,
    'A Literal Garden': 0,
    'Ice Cream': 0,
    'Cake': 0,
    'Pie': 0,
    'Coffee': 0,
    'Tea': 0,
    'Unicorn Tears': 0
}

def exit_app():
    print('adios')
    sys.exit()

while True:
    answer = input ('')
    if answer == 'quit':
        exit_app()
    if answer in menu:
        menu[answer] +=1
        t = menu[answer]
        print('*'*2+str(t)+' orders of '+answer+' have been added to your')
    else:
        print('Your request is not in our menu,please make orders from our menu')
        print (f"""
        {'*'*35}

        {'*'*2} What would you like to order? {'*'*2} 

        {'*'*35}
        """)
        
        
        



