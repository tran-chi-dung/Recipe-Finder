# Recipe Finder Application (alpha-1)

The **Recipe Finder** application helps users search for recipes based on the ingredients available in their refrigerator. The application uses **Flask** to create a web server and **SQLite** to store recipe data.

## Key Features

- **Recipe Search**: Users can enter available ingredients and the application will search for recipes that match those ingredients.

- **Recipe Database**: Recipes are stored in a SQLite database.

- **Simple User Interface**: The search interface is very easy to use, allowing users to quickly search and browse through recipes.

## Installation

### Prerequisites

To run this application, you need to have **Python 3.x** and **pip** installed on your computer.

### Install required libraries

1. **Clone repository**:

```bash
git clone https://github.com/username/recipe-finder-app.git
cd recipe-finder-app
```

2. **Install required libraries**:

```bash
pip install -r requirements.txt
```

### Configure database

The app uses **SQLite** to store recipes. After installing the libraries, you need to create the database by running:

```bash
python
from app import db
db.create_all()
```

### Run the app

1. **Run the Flask app**:

```bash
python app.py
```

2. Access the app via a browser at **http://127.0.0.1:5000**.

## How to use

1. Open the application in the browser.

2. Enter the list of available ingredients (e.g. "chicken, rice, carrots") in the search box.

3. Press the **Search** button to find recipes that match the entered ingredients.

4. Recipes will appear below the search box, including the dish name, ingredients, and cooking instructions.

## Tools used

- **Flask**: Web framework for Python.

- **Flask-SQLAlchemy**: ORM for working with SQLite databases.

- **HTML, CSS, JavaScript**: User interface.

## Future improvements

- **User login and registration**: Add user account management feature, helping to save favorite recipes.

- **Add recipe to favorites list**: Users can save recipes to their favorites list.

- **Ingredient-based recipe suggestions**: Automatic recipe suggestions based on available ingredients.

## Contact

If you have any questions or suggestions, please contact us via GitHub or email: **youremail@example.com**

## License

This application is released under the **MIT** license. See [LICENSE](LICENSE) for more information.

---
