# ChefGPT

A chatbot for our culinary needs. Chinese version

## Features

1. Finds a chinese dish that you can make using some given ingredients.

   Exception Handling: If no chinese dish is possible with the given combination of ingredients, it'll be pointed out.

   ![image](assets/dish-generator.png)

2. Generates a recipe for a chinese dish. If dish is not chinese, then it would not be handled

   ![image](assets/recipe-generator.png)

   Exception Handling: If the input is not a dish, it'll be pointed out.

   ![image](assets/recipe-generator-not-chinese.png)

3. Gives feedback on the user's recipe.

   Exception Handling: If the input is not a recipe, it'll be pointed out.

## Observations

- Whenever a valid recipe is inputted, the chatbot finds a way to make some improvements to it.
- The chatbot can identify irrelevant messages and decline to respond to them.

## Running the Code

1. Create a virtual environment.

   ```sh
   python -m venv chefgpt
   ```

2. Activate it.

   - Windows

     ```ps
       .\chefgpt\Scripts\Activate.ps1
     ```

   - Linux

     ```sh
     source chefgpt/Scripts/activate
     ```

3. Install dependencies.

   ```sh
   pip install -r requirements.txt
   ```

4. Run the program.

   ```sh
   python main.py
   ```
