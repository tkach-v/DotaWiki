# DotaWiki
DotaWiki is a comprehensive encyclopedia for Dota  2, providing detailed information on heroes, items, skins, and guides. This project aims to be a one-stop resource for players, enthusiasts, and researchers looking to enhance their knowledge and understanding of the game. Explore the vast world of Dota  2 with DotaWiki, and elevate your gameplay to new heights.


## Features  
- In-depth profiles of all Dota  2 heroes, including abilities, stats, and lore. 
- Complete list of in-game items, with descriptions, stats, and crafting recipes. 
- Showcase of hero skins, including previews, rarity, and release dates. 
- A curated collection of guides and tips for players of all skill levels, covering various aspects of the game.


## Authors
Roman Volsky - email@gmail.com, [Github](), [LinkedIn]()

Volodymyr Tkach - vovantkac5.work@gmail.com, [Github](https://github.com/tkach-v/), [LinkedIn](https://www.linkedin.com/in/volodymyr-tkach5/)

## Tech Stack
- Python-Django
- MySQL
- External APIs
- HTML
- CSS
- JavaScript
- Bootstrap

## Setup
Since this project is not yet deployed, you need to run it on your local machine to try it out.

To set up and run the "DotaWiki" project locally, follow these steps:

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

4. Run the database migrations:
```
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser for the Django admin panel:
```
python manage.py createsuperuser
```
Follow the prompts to create a username, email, and password for the superuser.


6. Run the development server:
```
python manage.py runserver
```
This will start the development server at http://localhost:8000/.

You should now be able to access the DotaWiki project in your web browser at http://localhost:8000/. You can log in to the admin site at http://localhost:8000/admin/ using the superuser account you created earlier.

## How to Contribute
Pull requests are welcome. If you'd like to contribute, please fork the repository and make changes as you'd like.

Steps to contribute:
1. Fork this repository (link to repository)
2. Create your feature branch: `git checkout -b feature/fooBar`
3. Commit your changes: `git commit -am 'Add some changes'`
4. Push to the branch: `git push origin feature/fooBar`
5. Create a new Pull Request
