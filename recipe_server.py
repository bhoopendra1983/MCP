
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Recipe MCP Server")

RECIPES = [
    {
        "name": "Potato Curry",
        "vegetarian": True,
        "ingredients": [
            "Potatoes",
            "Onion",
            "Tomatoes",
            "Turmeric",
            "Salt",
        ],
        "steps": [
            "Boil and chop the potatoes.",
            "Cook onion and tomatoes with spices.",
            "Add potatoes and simmer until cooked.",
        ],
    },
    {
        "name": "Vegetable Fried Rice",
        "vegetarian": True,
        "ingredients": ["Cooked rice", "Carrots", "Peas", "Soy sauce"],
        "steps": [
            "Chop the vegetables.",
            "Stir-fry the vegetables.",
            "Add rice and soy sauce and mix well.",
        ],
    },
]


@mcp.tool()
def search_recipes(
    ingredient: str,
    vegetarian_only: bool = False,
) -> list[dict]:
    """Search recipes by ingredient."""
    matches = []

    for recipe in RECIPES:
        contains_ingredient = any(
            ingredient.lower() in item.lower()
            for item in recipe["ingredients"]
        )

        if contains_ingredient and (
            not vegetarian_only or recipe["vegetarian"]
        ):
            matches.append(recipe)

    return matches


@mcp.tool()
def get_recipe(name: str) -> dict:
    """Get the ingredients and steps for a recipe."""
    for recipe in RECIPES:
        if recipe["name"].lower() == name.lower():
            return recipe

    return {"error": f"Recipe not found: {name}"}


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
