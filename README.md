# Cuisine

See the app [here](https://recipe-app-python.herokuapp.com)

Cuisine is an online recipe book, where users can add, edit and delete the recipes on the site. Users can also search through the recipes, and see either a sorted or a refined view of the results. This project is the 4th requirement of the Code Institute's full stack web development course. The project showcases skills in: Python3, Flask and MongoDB.


**Index:**
1. [User experience](#user)
2. [Features](#features)
3. [Technologies Used](#technologies)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Credits](#credits)



## User experience 

Users wanted an easy way to find new recipes, written by people of all skills and abilities, and also to easily share their own recipes. 

For example, here are some user stories below:

* **User A**: "I want to be able to find recipes, and be able to read the ingredients from my smartphone"   
    
* **User B**: "I want to be able to digitize my recipes, so I won't need to keep my old cookbooks anymore"  
    
* **User C**: "I want to be able to find something to cook quickly and easily"

Therefore we concluded that users wanted a simple way to store recipes, in an easily accessible, readable and shareable way. They would therefore also need a method to edit the stored recipes, and also delete them should they wish.

Please look below at the wireframes for the original concept:

![index/welcome page](https://github.com/brookk16/Cuisine/blob/master/course%20files/index.jpg)
![Add and edit recipe page](https://github.com/brookk16/Cuisine/blob/master/course%20files/add_edit.jpg)
![search for a recipe](https://github.com/brookk16/Cuisine/blob/master/course%20files/search.jpg)

Below you can see the schema and layout for the MongoDB database:

Recipes follow this format:
~~~
{
    "_id": {
        "$oid": "5c5b2f9bfb6fc06f4f571c28"
    },
    "meal_type": "dinner",
    "recipe_name": "A simple teriyaki chicken with noodles",
    "ingredients": "1tb honey, 1/2 cup soy sauce, 1/3 cup red wine vinegar, 250g noodles, 2 peppers, 2 onions, 500g chicken",
    "cuisine_type": "asian",
    "recipe_instructions": "To prepare the sauce: mix the honey, soy sauce and red wine vinegar, then set aside. Bring a large pot of water to boil, add a little salt and the noodles, Dice the chicken, and cook until ready. Whilst the chicken is cooking, chop the onions and peppers, and when the chicken is ready add the vegetables. Once the noodles and the vegetable/chicken mix is cooked, combine them and add the sauce. Continue cooking whilst moving the mix as to avoid burning, for a further 5 minutes",
    "author": "Bob Dylan",
    "cooking_duration": "30",
    "serves": "4",
    "recipe_description": "Noodles with chicken, peppers and onions in a sweet teriyaki sauce"
}
~~~

The rest of the collections follow this format:
~~~
{
    "_id": {
        "$oid": "5c62e732fb6fc01c4ce267f4"
    },
    "author": "Bob Dylan"
}
~~~

![Data schema for the MongoDB used in this app](https://github.com/brookk16/Cuisine/blob/master/course%20files/recipesdb_schema.jpeg)



## Features

The main features of the app concern the manipulation of the recipes, and can be divided into the following operations:

* **Add**: users can add new recipes to the database by: 
   1. Clicking either "Add a recipe" in the side navigation bar, or the "Add" button on the welcome page.
   2. This takes the user to the "Add a recipe" page where users fill out all the fields in the form, and click the 'Add recipe' button to add their recipe.
   
   * If the input author name is not currently in the database, it is added to the "authors" collection.
   
   * Users are provided instructions, via hover tooltips and messages in the input fields, on how to input their recipe, and have it shown correctly.
   
   * Users can also add new **category values** (i.e: a new meal type, cuisine type, serving size and/or cooking duration) if they can't find a value that best suits their recipe, at the bottom of the page. Users can add a new category value by choosing the category they wish to add to, clicking add, and then following the instructions on the pop up modal window. Users cannot submit something another value that is the same as another entry in the database, and will see an error message ("We already have a 'category name' called 'invalid input value'")
   
* **Search**: users can search by: author, cooking duration, cuisine type, meal type and serving size. They can search the recipes in two different ways:
   * Sort results: users can view sorted results that group by the chosen category, and can either be ordered high-low or low-high (based on switch input). They can do this by adding an option to the "Order results by" dropdown, and clicking the "search" button. Users should ignore the second dropdown that appears if they want a sorted view of results.
   * Refined results: users can view only the recipes that match their choices, by adding a value to both the first input field ("Order results by") and also in the second dropdown that appears (which shows all the options in the database for the chosen search category), and clicking search.
   * Users are also shown the number of results returned at the top of the page, out of the total results. And also their search choices.

* **Edit**: users can edit recipes in the database by:
   1. Clicking on the 'Edit' button on the recipe page that you wish to edit.
   2. This will take you to the 'Edit a recipe' page, where users will see a form. This form is prepopulated with the values already in the database.
   3. Users need only change the fields they wish, and click the "Submit changes" button to save.
   
   * Users cannot edit category values because they could negatively affect the database, and cause errors on the site.

* **Delete**: 
   * Users can delete recipes in the database by clicking the "Delete" button on the recipe's specific page.
   * Users cannot delete category types because it may negatively impact the database, and the app.
   * Category types and authors are kept in the database even if no recipes currently use these values because they may be needed in the future, and thus will be ready for users.  

Please note that only the Github logo in the footer works (will take user to the Github page). The Facebook and Twitter logos currently do not go anywhere.
#### Features left to implement

The following features were not added for 3 reasons: time constraints, they weren't a requirement for the project and/or I do not currently have the knowledge to implement the feature effectively.

1. Allowing users to store images in the MongoDB database, or in another easily scalable method.
2. Providing the ability for users to create user profiles, for grouping their favorite recipes. 


## Technologies Used

#### Front-end

[Fonts awesome](https://fontawesome.com) & [Material icons](https://material.io/tools/icons/?style=baseline):
* Provide the icons for the project (awesome fonts was used as well as Material icon to provide the icons for the links to: Github, Facebook and Twitter)

[Materialize](http://archives.materializecss.com/0.100.2/) (0.100.2):
* Provides a grid system to structure html code, basic css styling and also javascript components for the app
* Used Materialize components are:
  * Side navigation bar (hiding on smaller screens and displaying a hamburger icon)
  * Modal pop ups for adding categories (add and edit recipes.html)
  * Parallax images on all pages
  * Dropdown menus

[Google Fonts](https://fonts.google.com):
* Fonts "Montserrat" and "Libre Baskerville" used

[Jinja2](http://jinja.pocoo.org/docs/2.10/) (2.10):
* Used to provided backend connectivity with flask and  to render data from the database 

[JQuery](https://jquery.com)(3.2.1)
* Provides DOM manipulation, and allows use of materialize javascript components

#### Back-end

[Python3](https://www.python.org/download/releases/3.0/) (3.4.3):
* Used to write the logic for this app (which can be seen in [app.py](https://github.com/brookk16/Cuisine/blob/master/app.py))

[Flask-Pymongo](https://flask-pymongo.readthedocs.io/en/latest/) (3.7.2):
* Python-Flask tools for connecting to and manipulating the MongoDB database

[Flask](http://flask.pocoo.org) (1.0.2):
* Acts as a framework for the app

#### Database

[MongoDB](https://www.mongodb.com) with [mlab](https://mlab.com):
* MongoDB provides the non-relational database, whilst mlab hosts our database (allowing users access)


The code editor used to create the project was [Cloud9](https://c9.io/signup).

The project uses [Git](https://git-scm.com) for version control.

For the additional tools and libraries needed to run the app, please refer to [requirements.txt](https://github.com/brookk16/Cuisine/blob/master/requirements.txt)

## Testing

<details>
<summary>User stories</summary>
<br>
User stories were checked to ensure this project meets their requests:

1. Users can easily and quickly search results, by either grouping results (with the additional choice of grouping high-low or low-high) or by searching for results with specific values. In addition, the number of results are displayed with the total number of entries in the database. Appropriate error messages are displayed for user error and no results found.
2. Users can easily add recipes to the database, and then edit and delete said recipes if required. 
3. The site is fully responsive and thus can effectively be used on smaller screen sizes.

</details>

<details>
<summary>Manual Testing</summary>
<br>
Manual testing was conducted on all main features of the app (features outlined [here](#features)).

> note: all tests begin by starting at the index/welcome page.

> note: all tests (excluding search functionality and working with category values) use the recipe created in test 1.

> note: all tests are from the desktop perspective. For mobile, any references to a "side nav bar", will require clicking on the "&#8801;" symbol first to reveal the menu.

**1. Testing adding a recipe**
* Started by clicking on "Add a recipe" in the side nav bar, or the "Add +" button in the welcome message box.
* Redirects user to the correct "addrecipes.html" page
* Each form field was then filled following the tooltips and messages in the form with random data
* Then submitted using the "Add a recipe" button
* User is then redirected to "searchrecipes.html" and the created recipe can be seen

Also tested whether a new author was added to the database (if it doesn't already exist) by adding a new author name to the "Author" field in the form.


**2. Testing searching for a recipe**
<br> 
* Started by clicking on "Search recipes" in the side nav bar, or the "Search" button in the welcome message box.
* Redirects to "searchrecipes.html" page
* Default view shows: all recipes (high to low) and the number of recipes the database currently contains.>]

> Changing the switch from high-low to low-high changes the order of search results (to low to high).

We needed 2 different tests here:

1. Grouping search results:
   * Clicked on the dropdown menu and chose a search category
   * Ignored the prompt and 2nd the drowdown menu
   * Clicked on the "Search" button
   * Get redirected back to the "searchrecipes.html" page, with recipes ordered by the chosen search category (ordered high-lor or low-high based on switch position)
   * Correct message displays the search category and number of results (also whether the results are ordered high-low/low-high)

Tests were repeated for each of the 5 search categories (Authors, Cooking duration, Cusine type, Meal type and Serves)

2. Refining search results
  * Clicked on the dropdown menu and choose a search category
  * Followed the prompt and add a search value from the dropdown that appears
  * Then clicked on "Search"
  * Get redirected back to the "searchrecipes.html" page, with only the recipes that match the search category and value will be displayed
  * Correct message displayed the number of search results for the chosen search category and value

Tests were repeated for 3 random values for each search category

If no results were found a message displaying: "No recipes are found for (search category chosen)" of (search value chosen)""
 
**3. Testing viewing full recipe information**
Started on the search recipes page (searchrecipes.html).

* Chosen the created recipe, and clicked on the "Full Recipe" button
* Redirects to the recipe's main page, showing all information in the database concerning the chosen recipe

**4. Testing editing a recipe**
<br>
Users can only edit recipe content from the recipe's main page

* Clicked on the "Edit" button to the right of the recipe card 
* Redirected to the "Edit a recipe" page (editrecipes.html) 
* Form is prepopulated with the chosen recipe's information.
* Edited each field by adding 123 to the beginning of the input (where possible)
* Then clicked the "Submit Changes" button
* Redirected to the search recipes page, which displayed our edited recipe.

**5. Testing deleting a recipe**
<br>
Users can only delete a recipe from the recipe's main page

* Clicked on the "Delete" button to the right of the recipe card
* A modal popup appeared asking me "Are you sure you want to delete this recipe?"
* Clicked on the "Delete" button in the modal to delete the recipe
* Redirected to search recipes, where the test recipe was deleted

**6. Testing adding a new category value**
<br>
Users can add new category values, but cannot delete or edit them.
They can add new values on the "Add a recipe" and the "Edit a recipe" pages.

* Go to the bottom of the form (add or edit a recipe)
* Clicked the "Add +" button (repeated for each of the 4 categories)
* Followed instructions to add a new value
* Then clicked the  "Add a new (category name)+" button
* Redirected back to the form with new category value in its dropdown menu

If the added category value is already in the database, the new value will not be added, and a message will appear saying "We already have a (category type) of (category value)".
</details>

<details>
<summary>Further testing and Issues</summary>
<br>
1. HTML and CSS code were both validated using W3C [HTMl](https://validator.w3.org) and [CSS](https://jigsaw.w3.org/css-validator/) validator.

> note: HTML validation threw up errors, although these were concerning the Jinja2 templating language used in the html templates.

2. Users have tested the site and provided feedback:
  * **Ex:** "Searching for recipes was a little confusing, I didn't know why the 2nd dropdown appeared" This was solved by adding bold font to the prompt, making it easier to read/understand.

3. The site was tested across all screen sizes.

4. Google devlopper tools audits were also conducted. 

Issues:
* Testing revealed: 
  * lack of detail in explaining how to search through recipes, add and edit them. Thus more comprehensive tooltips and prompts were added. 
  * users were wrongly redirected after submitting new categories (users always sent back to "addrecipes.html" even when they added the new category on "editrecipes.html")

* The author is not yet skilled in automated testing, and as such was unable to adhere to a test driven development approach. 
</details>



## Deployment

The project is deployed on Heroku, and can be accessed [here](https://recipe-app-python.herokuapp.com) 

The Github for this project can be found [here](https://github.com/brookk16/Cuisine). And can also be accessed via the github logo in the footer of the website.

Download the code from github, and place into your project. 

Or clone the project into your working environment, using the command line:

~~~
git clone https://github.com/cp-example/c9_flask_portfolio_app.git
~~~

##### To deploy to Heroku:
1. Start by creating an account on [Heroku](https://www.heroku.com/)
2. Create a new app (either via the website or command line)
3. login to Heroku in the command line (of your ide)
    ~~~
    heroku login
    ~~~
4. Check your current apps, to check the app has been created
    ~~~
    heroku apps
    ~~~

##### You will also require 2 additional files: 
    
5. Creation of "requirements.txt" file, which displays the additional libraries and requirements to run the project.

Use the command below to create the requirements.txt:
~~~
sudo pip3 freeze --local > requirements.txt 
~~~

6. Creation of a "Procfile", which tells Heroku how to run our app
~~~
echo web: python app.py > Procfile
~~~

##### Then add the environmental variables 

7. Go to [Heroku](https://www.heroku.com/)
 * Go to Settings
 * Reveal config vars
 * Set IP: 0.0.0.0 Port: 5000

You will also need to set a SECRET_KEY here in config vars, to keep the SECRET_KEY private and secure. Follow the same process above and add:
 * SECRET_KEY: (Place your character string here)

##### Finally, link to Github and deploy!

8. Start by using the following commands to create your repository:
    ~~~
    git init
    git add .
    git commit -m "Initial commit"
    ~~~
 9. Then link to Heroku:
 * Go to Heroku
 * Then to deploy
 * Choose "Github" as the Deployment method
 * Login and connect to your Github repository (for the project)
 * Then "enable automatic deploys"

10. If you now go into the command line in your IDE you can push the code to Heroku:
~~~
git push heroku master
~~~

11. Then set up the dynos: 
~~~
heroku ps:scale web=1
~~~

You can now view your project either via the "open app" button on Heroku, or by using the generated url in Heroku.


## Credits

#### Content

All the images used in the parallax for this site were obtained from [unsplash.com](https://unsplash.com).

The logo was created using [hatchful](https://hatchful.shopify.com).

#### Acknowledgements

The Code Institute's full stack web development course provided the knowledge for creating the app.

Inspiration for this project came from [momofuku.com](https://momofuku.com).

