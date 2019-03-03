# Cuisine

Cusine is an online recipe book, where users can add, edit and delete the recipes on the site. Users can also search through the recipes, and see either a sorted or a refined view of the results. This project is the 4th requirement of the Code Institute's full stack web development course. The project showcases skills in: Python3, Flask and MongoDB.


Index:
-[User experience](#credits)
-[Features]()
-[Technologies Used]
-[Testing]
-[Deployment]
-[Credits]



## User experience 

Users wanted a way to be able to find new recipes written by real people, and also to easily share their own recipes. 

For example, please read the user stories below (from which we based our design decisions):

* **User A**: "I want to be able to find recipes, and be able to read theingredients from my smartphone on the go"   
    
* **User B**: "I want to be able to digitize my recipes, so I won't need to keepmy old cookbooks anymore"  
    
* **User C**: "I want to be able to find something to cook quickly and easily"

Therefore we concluded that users wanted a simple way to store recipes, in an easily accesible, readable and shareable way. They would therefore also need a method to edit the stored recipes, and also delete them should they wish.

Please look below at the wireframes for the original concept:



## Features

The main features of the app concerns the manipulation of the recipes, and can be divided into the following opperations:

* **Add**: users can add new recipes to the database by: 
   1. clicking either "Add a recipe" in the side navigation bar, or the "Add" button on the welcome page.
   2. This takes the user to the "Add a recipe" page where users fill out all the fields in the form, and click the 'Add recipe' button to add their recipe.
   
   * If the input author name is not currently in the databse, it is added to the "authors" collection.
   
   * Users are provided instructions, via hover tooltips and messages in the input fields, on how to input their recipe, and have it shown correctly.
   
   * Users can also add new **category values** (i.e: a new meal type, cuisine type, serving size and/or cooking duration) if they can't find a value that best suits their recipe, at the bottom of the page. Users can add a new category value by choosing the cateogry they wish to add to, clicking add, and then following the instructions on the pop up modal window. Users cannot submit something another value that is the same as another entry in the database, and will see an error message ("We alrady have a 'category name' called 'invalid input value'")
   
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
   * Users can delete recipes in the databse by clicking the "Delete" button on the recipe's specific page.
   * Users cannot delete category types because it may negatively impact the database, and the app.
   * Category types and authors are kept in the database even if no recipes currently use these values because they may be needed in the future, and thus will be ready for users.  

#### Features left to implement

The following features were not added for 3 reasons: time constraints, they weren't a requirement for the project and/or I do not cuurently have the knowledge to implement the feature.

1. Allowing users to store images in the MongoDB database, or in another easily scallable method.
2. Providing the ability for users to create user profiles, for grouping their favourite recipes. And possibly refining editing and deletion of recipes to the author and admin alone.


## Technologies Used


In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

JQuery
The project uses JQuery to simplify DOM manipulation.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

The project is deployed on Heroku, and can be accessed [here](https://recipe-app-python.herokuapp.com)  

Deployment to Heroku required 3 things:

**1-** Creation of "requirements.txt" file, which displays the additional libraries and requirements to run the project.

 Use the command below (in the command line) to install requirements:
 ~~~
 pip3 install -r requirements.txt
 ~~~

**2-** Creation of a "Procfile", which tells Heroku how to run our app

**3-** Setting environment variables on Heroku. 
Within our flask main code (i.e: app.py) we set the variables for IP, PORT and the SECRET_KEY to environment variables, which are retrieved from Heroku.



There are no differences between the deployed and development version of the app. However, for purposes of securing the app, the following variables were set as environmental variables: IP, PORT and the SECRET_KEY. Each of these were set and are retireved from Heroku.


## Credits

#### Content

The photos used in this site were obtained from [unsplash.com](https://unsplash.com)


