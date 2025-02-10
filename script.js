function searchRecipes() {
    const ingredients = document.getElementById("ingredients").value;
    
    if (!ingredients) {
        alert("Please enter some ingredients.");
        return;
    }

    fetch(`/search?ingredients=${ingredients}`)
        .then(response => response.json())
        .then(data => {
            let recipesDiv = document.getElementById("recipes");
            recipesDiv.innerHTML = '';  // Clear previous results

            if (data.length === 0) {
                recipesDiv.innerHTML = '<p>No recipes found.</p>';
            } else {
                data.forEach(recipe => {
                    const recipeDiv = document.createElement("div");
                    recipeDiv.classList.add("recipe");

                    const name = document.createElement("h3");
                    name.innerText = recipe.name;

                    const ingredientsText = document.createElement("p");
                    ingredientsText.innerText = `Ingredients: ${recipe.ingredients}`;

                    const instructions = document.createElement("p");
                    instructions.innerText = `Instructions: ${recipe.instructions}`;

                    recipeDiv.appendChild(name);
                    recipeDiv.appendChild(ingredientsText);
                    recipeDiv.appendChild(instructions);

                    recipesDiv.appendChild(recipeDiv);
                });
            }
        })
        .catch(error => console.error("Error fetching recipes:", error));
}
