from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'  # SQLite database
db = SQLAlchemy(app)

# Model Recipe
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    instructions = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Recipe {self.name}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for searching recipes
@app.route('/search', methods=['GET'])
def search():
    ingredients = request.args.get('ingredients')
    if not ingredients:
        return jsonify({'error': 'No ingredients provided'}), 400

    # Search recipes by ingredients
    recipes = Recipe.query.filter(Recipe.ingredients.contains(ingredients)).all()
    results = [{'name': r.name, 'ingredients': r.ingredients, 'instructions': r.instructions} for r in recipes]
    
    return jsonify(results)

# Route for adding a recipe (for testing purposes)
@app.route('/add', methods=['POST'])
def add_recipe():
    data = request.get_json()
    new_recipe = Recipe(name=data['name'], ingredients=data['ingredients'], instructions=data['instructions'])
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
