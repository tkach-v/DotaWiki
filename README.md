# DotaWiki
DotaWiki is a comprehensive encyclopedia for Dota  2, providing detailed information on heroes, items, skins, and guides. This project aims to be a one-stop resource for players, enthusiasts, and researchers looking to enhance their knowledge and understanding of the game. Explore the vast world of Dota  2 with DotaWiki, and elevate your gameplay to new heights.

Follow this link to view our project: http://ec2-75-101-200-171.compute-1.amazonaws.com/


## Features  
- In-depth profiles of all Dota  2 heroes, including abilities, stats, and lore. 
- Complete list of in-game items, with descriptions, stats, and crafting recipes. 
- Showcase of hero skins. 
- A collection of guides and tips for players of all skill levels, covering various aspects of the game.


## Authors
Roman Volskiy - romanvolskiy791@gmail.com, [Github](https://github.com/VolskiyRoman/)

Volodymyr Tkach - vovantkac5.work@gmail.com, [Github](https://github.com/tkach-v/), [LinkedIn](https://www.linkedin.com/in/volodymyr-tkach5/)

## Tech Stack
- Python
- Django
- MySQL
- HTML
- CSS
- SCSS
- JavaScript
- Bootstrap

## Setup
You can see deployed version here: http://ec2-75-101-200-171.compute-1.amazonaws.com/

If you want to set up and run the "DotaWiki" project locally, follow these steps:

1. Clone the repository:
```
git clone <repository_url>
cd DotaWiki
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # For Linux and macOS
venv\Scripts\activate     # For Windows
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Configure MySQL on your local machine and add a .env file to the project (the secret key, database configuration, etc). Use this .env file as an example:
```
SECRET_KEY=1111
DEBUG=True
DB_NAME=db
DB_USER=root
DB_PASSWORD=1111
DB_HOST=127.0.0.1
DB_PORT=3306
```

5. Run the database migrations:
```
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser for the Django admin panel:
```
python manage.py createsuperuser
```
Follow the prompts to create a username, email, and password for the superuser.


7. Run the development server:
```
python manage.py runserver
```
This will start the development server at http://localhost:8000/.

You should now be able to access the DotaWiki project in your web browser at http://localhost:8000/. You can log in to the admin site at http://localhost:8000/admin/ using the superuser account you created earlier.
