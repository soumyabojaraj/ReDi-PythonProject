# Recipe Recommendation 

## Overview
This application helps users discover recipes based on the ingredients they have available. By entering a list of ingredients, users receive recipe recommendations from a preloaded recipe list, with cooking instructions.

## Features
- Recipes are preloaded in a CSV file.
- Input available ingredients to find matching recipes.
- View detailed recipe instructions for selected dishes.



## Setup Instructions
### Clone the repository

    ```
    git clone <repository_url>
    cd recipe-app
    ```

### **Setting Up the Virtual Environment**

1. **Create a Virtual Environment**:
   - Run the following command to create a virtual environment named `env`:
     ```
     python3 -m venv env
     ```

2. **Activate the Virtual Environment**:
   - On **Windows**:
     ```
     env\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```
     source env/bin/activate
     ```

3. **Install Dependencies**:
   - With the virtual environment active, install the required Python packages:
     ```
     pip3 install -r requirements.txt
     ```

4. **Verify Installation**:
   - Check if dependencies were installed correctly:
     ```
     pip3 list
     ```

---

### **Running the Application**
 
1. Run the application:
   ```
   python3 -m app.main

2. Follow the Menu Options:
    - Select 1 - "Find Recipes" 
    - input your available ingredients and find matching recipes.
    - enter the selected recipe to view detailed instructions
    - Select 2 - "Exit" to exit from the application

> NOTE: Please input any ingredients from the csv file for the application to work. (Eg: potato, tomato, spices)


## Testing
Run tests using pytest:

```
pytest
```
 ## Resources Used:
Virtual enovironment:
 https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/

Data: https://baduguru.wordpress.com/category/badugaru-recipes/ - (Personal blog)

Readme: https://www.markdownguide.org/basic-syntax/

Pytest: Chagpt reference code