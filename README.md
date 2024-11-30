# Recipe Recommendation 

## Overview
This application helps users discover recipes based on the ingredients they have available. By entering a list of ingredients, users receive recipe recommendations from a preloaded recipe list, with cooking instructions.

## Features
- Recipes are preloaded in a CSV file.
- Input available ingredients to find matching recipes.
- View detailed recipe instructions for selected dishes.

## Setup Instructions
1. Clone the repository.
    ```
    git clone <repository_url>
    cd recipe-app
    ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

    ```
    python3 -m app.main
    ```
2. Follow the Menu Options:
    - Select "Find Recipes" to input your available ingredients and find matching recipes.
    - View detailed instructions and ingredients for the selected recipe.


## Testing
Run tests using pytest:

```
pytest
```
