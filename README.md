<div align="center">![Page Logo](static/images/logo.png?raw=true "Logo")</div>

# Love Recipes

This is a website where a user can go to either find a recipe or add their own recipe to share with other users. It's an online cookbook that users can add to, edit or delete recipes from, making it more versatile and than a physical book.

Users can find recipes anywhere and anytime as the site is mobile friendly as well as working on larger screen sizes.

## UX

The website is designed for users who are looking for inspiration on what to cook and also how to cook it. It is also designed to promote an online kitchenware store, offering deals for shopping there through links on this website.

The navigation bar has clearly labled options so it is easy for a user to navigate around the site. They can either search the existing recipes or they can add their own. There is also a home button to take them back to the main page if needed.

Each recipe view has clearly labled buttons in order to view, edit or delete recipes and the pages for editing or adding a new recipe have clearly marked input fields with errors if a required field isn't supplied and the therefore the save unsuccessful. 

The online kitchenware store is clearly labled on the homepage and within the full recipe views making it easy for user to navigate to the website from within Love Recipes and receive their discount from doing so.

User type examples:

1. I am a parent wondering what to cook for dinner for my family. I don't know what I want to cook, i'm looking for inspiration as well instructions.

- To acheive their goal, the above user type would only need to open up Love Recipes and then there is a link to search the recipes on the home page and in the navbar. They can then choose the mealtype they want and this will show just the names of all the recipes for that meal type on the website. Clicking on the names brings up a short description of the recipe and so the user would just need to click on the full recipe once they have made their decision. 

2. I want to cook something inspiring, I like the sound of a specific recipe but I don't think I have all the tools I need to make it. 

- The above user type would either see the link on the homepage with the discount to the online kitchenware store, or from within the recipe that they wanted to make but didn't have the tools for. This means it is easy for anyone who finds a recipe they really want to try to buy discounted equipment in order to make it possible.

3. I have previously added my own recipe to the website but have since discovered that it works even better when I use slightly different ingredients or preparation method.

- The above user would only need to navigate to the search function on the website, type in their recipe name to bring up the full recip view and click on the 'Edit' button at the bottom of the screen. They can then make any changes they wish to the recipe in order to share the improved version with the world.

I created an initial wireframe for the project using [Lucid Chart](https://www.lucidchart.com/pages/home) which is linked [here](static/images/online_cookbook.pdf).

## Existing Features

- Navigation bar - allows user to easily move between pages of the website depending on what they want to do.
- Search bar - allows user to search by recipe name.
- Add own Recipe - allows users to input their own recipe and upload it onto the site.
- Edit button - allows user to make changes to an existing recipe.
- Delete button - allows user to delete recipes from the site. 
- View full recipe button - allows user to view a single recipe fully, not just the summary.
- shop Now button - allows user to navigate to the online kitchenware store through a link that will give them a promotion which can be changed but is currently 10% off.

## Features Left to Implement

- In the future I would like to add a user feature where customers have their own login for the website and can leave comments on recipes if they want to.
- I would also like to add a feature that allows customers to upload pictures of their attempts at recipes.

## Technologies Used

- [Materialize](https://materializecss.com/)
    - To allow the use of frameworks.

- [jQuery](https://jquery.com/)
    - To allow the use of certain pre-written functions.

- [Google Fonts](https://fonts.google.com)
    - To allow the use of a wider range of fonts.

- [MongoDB](https://www.mongodb.com/)
    - To incorporate a database that can be manipulated from within the website.

- Python
    - To render each page template and incorporate the information from the database.

- Javascript
    - For the funcionality of the framwork.

- HTML
    - For the design and background elements.

- CSS
    - To style the HTML.

## testing

1. Navigation Bar: All the buttons on the nav bar are linked to the correct page and they also collapse down when the screen size is made smaller.
2. Search bar: The search bar functions by finding the recipe in the database that has the same name as the one that is typed in. Capital letters do not effect the search but the name must match. If no results are found then you are taken to a page that lets you know this and has the add recipe function.
3. Add recipe: All required feilds must be filled in in order to successfully save the new recipe and error messages will pop up for all feilds where they don't explicitly state they are required. Saving the recipe will successfully add it to the database.
4. Edit recipe: Pressing on this button will take you to a page wherethe original data is filled in, making it easy to ick out what it is you want to edit without having to re-enter the other details. Saving changes will successfully update the entry in the database.
5. Delete recipe: Pressing this will successfully remove the entire entry from the database.

I tested the speed of my website using the full page test in [Pingdom](https://tools.pingdom.com/) Tools.
This specific test was done on July 19. The web page took 236 ms to load, used 13 requests, and weighed in at 815.3 KB.
The Google Page Speed performance grade for this web page is 86/100.
More information on this test can be found [here](https://tools.pingdom.com/#5cd9d3fdf9800000)

Screensizes and Devices:

- I tested the website to make sure it functioned correctly and displayed well on every device given using Chrome Developer Tools when viewing the site in a browser and also that it transitioned well when changing the screensize 
gradually from large to small.
- I tested the website on a number of browsers including chrome and firefox to make sure it functioned as expected on 
all of them. 
- I tested the website on different laptop types including Acer Chromebook, Dell Inspiron and a ThinkVision 4K external 
screen.
- I tested the website on a number of mobile devices to make sure it displayed correctly and worked as expected. These 
included a Moto g6 play, Huawei p20, Samsung S7, iPhone 5s and a Samsung S8.

## Deployment

In order to deploy this website using Heroku I navigated to the app within Heroku. I then clicked on settings and scrolled down to domains. The URL is shown here with the link to the published app showing as https://love-recipes.herokuapp.com/.


In order to deploy the website locally you would need to go to the GitHub repository directly. You would then need to click download 
and copy the link that it gives you. Next go to your terminal, enter the directory you wish to clone it to using the cd 
command and then type git clone and paste in the link you just copied. You can then enter the website directory again 
using the cd command and ls will bring up a list of the files. These can then be opened in your choice of editor.

## Credits

### Content
- The HTML used for the full page background was copied from [CSS-TRICKS, article ‘Perfect Full Page Background Image'](https://css-tricks.com/perfect-full-page-background-image/).
- The code used for the search function was modified from [MouseVsPython](https://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/) and [stackoverflow](https://stackoverflow.com/questions/7101703/how-do-i-make-case-insensitive-queries-on-mongodb).
- The code used to find the last inserted id to view the full recipe was modified from [stackoverflow](https://stackoverflow.com/questions/8783753/how-to-get-the-object-id-in-pymongo-after-an-insert)
- The recipes pre-entered on the website were all obtained from [BBC goodfood](https://www.bbcgoodfood.com/).
- The idea to use the 'pre' tag for formatting the recipe view was taken from [stackoverflow](https://stackoverflow.com/questions/8573890/using-new-line-n-in-string-and-rendering-the-same-in-html).
- The method of formatting the 'pre' tag so the text wasn't all on a single line and fit the window size was taken from [stackoverflow](https://stackoverflow.com/questions/7132371/can-i-adjust-the-width-of-a-pre-area-to-fit-the-text).
- The code used to add the error 404 page was found at [Code Maven](https://code-maven.com/flask-return-404).

### Media
- The background photo for this website was obtained from [pxfuel](https://www.pxfuel.com/en/free-photo-omiog).
- The photo on the index page was obtained from [PxHere](https://pxhere.com/en/photo/1453277).
- The 'Shop now!' button currently links to the Amazon site for cookware [here](https://www.amazon.co.uk/kitchen-cookware-dining-glassware-cutlery-pans/b?ie=UTF8&node=392546011)
- The photo on the recipe view was obtained from [flickr](https://www.flickr.com/photos/30478819@N08/48558169527/)