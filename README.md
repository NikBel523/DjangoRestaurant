## DjangoRestaurant

### Description

This Django app is designed for small restaurants or cafes to manage their sales and inventory. 
The app allows you to add menu items, list ingredients in storage, and produce a recipe based on the menu item 
and available ingredients. Additionally, you can enter a purchase of a menu item, and the app will check if all the 
necessary ingredients are available to sell that menu item. If the purchase is made, the amount of ingredients decreases 
accordingly. The app also includes a view that shows the overall profits based on menu item selling price and ingredient 
costs.

### Features

- Add menu items
- List ingredients in storage
- Produce a recipe based on menu item and available ingredients
- Check ingredient availability before selling menu item
- Decrease ingredient quantity upon sale
- View overall profits based on menu item selling price and ingredient costs

### Installation

To install this app, follow these steps:

1. Clone the repository from GitHub
2. Create a virtual environment
3. Install dependencies from `requirements.txt`
4. Run migrations
5. Start the development server

### Usage

To get to the authorized views of the app create superuser (python manage.py createsuperuser) anf than
simply navigate to the app's URL on your browser (http://127.0.0.1:8000/inventory).  
From there, you can add menu items, list ingredients,
produce recipes, and make sales. The app also includes a view to show the overall profits.  

