# Vinyl Punks

![readmehero](documentation/images/header.jpg)
[Live website](https://vinyl-punks.herokuapp.com)

## Quick start

If you want to try out the app right away, you can either create a new user or log in with:

username: testuser  
password: testuser

## Introduction

Vinyl Punks is an fictional, online record store specializing in in the punk genre and vinyl format. For ease of use, registering for a profile is not needed to make a purchase. However, registering for a profiles opens the possibility to write reviews and rate the different albums. In addition, registering also let's a user store their shipping details and gives access to previous purchases. 

## Databases

The utilized database system for this project is [SQLite](https://www.sqlite.org/) in development and [PostgreSQL](https://www.postgresql.org/) in the deployed version. 

![erd](documentation/images/erd.jpg)

The diagram displays all the databases (models) in the project as well as their relationships. Some of the models also have associated functions which are important to understand to get a full understanding of all the databases functionality. This goes especially for the models of the checkout app.   
 
## UX

### General

The owner of the website(read: the team) recognizes the need for an online record store that specializes in the punk genre and the vinyl format. Vinyl as a format is on the rise, and punk as genre just won't die. These facts combined gives reason for the owner to believe that there's a market for such a record store.

Similarly, from a consumer's point of view, there's a need for a record store that specializes in providing music in the punk genre in the vinyl format. 


### Typography

The website uses two fonts from [Google Fonts'](https://fonts.google.com/) library called [Shadows Into Light](https://fonts.google.com/specimen/Shadows+Into+Light) and [Reenie Beanie](https://fonts.google.com/specimen/Shadows+Into+Light)

"Shadows Into Light" is used for most headings, while "Reenie Beanie" is only used for the main nav links. These two fonts were chosen for their handwritten, playful style and should somewhat reflect a 'punk' attitude.  All other text is [Roboto](https://fonts.google.com/specimen/Roboto?query=roboto).



### Colors

The website relies heavilly on bootstrap's color palette. Dark/black and red are used as primary colors. Since there's a profound presence of buttons across the website, it's important that these match the ever present header and navbar. "Danger" meets this criteria, and in the spirit of punk it breaks with a more traditional design where green ("success") has positive connotations and would typically be applied to "add to cart" and "checkout" buttons.

![Color](documentation/images/bscolors.JPG)

#### Danger
- Buttons for adding to cart
- X for deleting from cart
- X for deleting tracks (superuser view)
- All save buttons
- Checkout button
- Error toast

#### Warning
- Edit button for products (superuser view)

#### Info
- Header of info toast

#### Success
- Header of success toast

#### Light
- Background of every other element created by a template loop (comments, order history, tables)





### Bootstrap
[Bootstrap](https://getbootstrap.com) was chosen as CSS library for this project. There are several reasons for this: responsive grid, helper-classes and an excellent documentation are some of them. 

### User Stories

- I want to see a navigation bar at the top of the site. The navigation should either follow the page down as I scroll (sticky) or provide some other way to quickly access the navigation bar, independently on how far down the page I currently am.

- Upon entering the website I can immediately see what events I can visit to see the team in action.

- As a non-member of the team, I want to be able to get information about the members of the team.

- As a member of the team, I want to be able to add content to the website in the form of blog posts and workouts.

- As a member of the team I want to be able to edit and delete content that I have added. I also want to be able to remove myself as a member of the team.

- I want to be able to navigate to a section that displays my personal profile, and displays content that I've added to the site.

- At the bottom of the site I want to see a footer containing links to relevant social media sites.

### Wireframes

The wireframes somewhat deviates from the finished website as some of the ideas and features came into existence after the planning process. The "Events" view for instance, was an idea I just wanted to try out at the last stages of development and lacks wireframes. Other than that, there's wireframes for different screen sizes of views where this is relevant.    

- [Blog-posts](https://github.com/thorole/the-running-team/tree/master/documentation/wireframes/blog_post.pdf)
- [Workout-posts](https://github.com/thorole/the-running-team/tree/master/documentation/wireframes/workout.pdf)
- [Team page](https://github.com/thorole/the-running-team/tree/master/documentation/wireframes/team.pdf) | [Team page layout plan](https://github.com/thorole/the-running-team/tree/master/documentation/wireframes/team_all_sizes.pdf) | [Team page small screen and tablet](https://github.com/thorole/the-running-team/tree/master/documentation/wireframes/team_phone_tablet.pdf)
- [profile](https://github.com/thorole/the-running-team/tree/master/documentation/wireframes/profile.pdf) | [Profile small screen](https://github.com/thorole/the-running-team/tree/master/documentation/wireframes/profile_small.pdf)
- [Forms](https://github.com/thorole/the-running-team/tree/master/documentation/wireframes/forms.pdf) | [Forms small](https://github.com/thorole/the-running-team/tree/master/documentation/wireframes/forms_small.pdf)



## Features and views

The website has three main views. One view for users who are not logged in, one for when the user's logged in, and one for logged in users with administrator rights.   


### Nav bar
![Navbar](documentation/images/navbar.PNG)

The nav bar comes from Materialize's library and collapses to a "hamburger" on smaller screens. In addition, the navbar is wrapped inside an element containing the background image. Each nav link changes color on hover. 

### Events view (entry point)

![Events](documentation/images/events.PNG)

This is the entry point for the website. All events the team will be participating in is displayed in a materialize carousel. This view is accessible for all users, but only logged in users with administrator rights can add, edit and delete events. The subheader text changes depending if there's a logged in user or not.

### The Team view

![The Team](documentation/images/theteam.PNG)

The team section is accessible for all users. All registered users (team members) are displayed in clickable materialize cards. When clicked, the cards display the team member's full name and stats in the for of progression bars.

![Member Stats](documentation/images/progression.PNG)

If the user has a slogan, that will be displayed as well.

### Training Blog view
![Training Blog](documentation/images/training.PNG)

This section is restricted to logged in users. Here, the user can add new workouts and blog posts as well as edit and delete posts that belongs to the current user. Each post is displayed on a simple materialize card. If the user wants to add a post, the form pops up in a modal.

![Training Blog](documentation/images/newpost_modal.PNG)

The user can use the tabs to filter workouts and blog posts.

![Blog](documentation/images/blog.PNG)

Both workout posts and blog posts has some additional features, where the users can interact with the posts. All workout posts has an "attend/unattend" button to let other users know that they are attending/not attending the particular workout. All attending users are displayed in a section just beneath the body of the post. All of the blog posts can be commented. All comments, including the input field is displayed in a materialize collapsible beneath each post.

![Comments](documentation/images/comments.PNG)

### Profile view

![Comments](documentation/images/profile.PNG)

In the profile section, the user can edit and even delete their account. The profile image can be edited without editing the entire account by clicking on it. In addition, all the user's workout- and blog posts are displayed in collapsibles. All the workouts the user is attending are also displayed in collapsibles. This way, the profile page works like a dashboard for the user, containing all information relevant to them.

### Register view

This section is simply a form for the user to fill in and submit. If all required fields are valid, a new record is inserted into mongoDB, the user is redirected to their profile page, and can start using the website.

### Log in/out

This simply allows user to log in and out of the site. Logging in redirects the user to their profile while logging out redirects to The Team section.


### Features Left to Implement

All of the features that was planned for on this website was executed. However, there are almost an endless array of features that can be implemented to make the site even more functional. Here are a few ideas of features that would improve the site (in loosely prioritized order):

- Using AJAX for posting comments and attend/unattend functionality.
- Pagination in the training blog section
- File upload for profile image
- Administrator dashboard
- E-mail confirmation when registering
- Back-end validation of forms 

## Technologies Used

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [VS Code](https://code.visualstudio.com/)
- [HTML5](https://www.w3.org/) 
- [CSS3](https://www.w3.org/)
- [Python](https://www.python.org/)
- [Pip](https://pip.pypa.io/en/stable/)
- [mongoDB](https://www.mongodb.com/)
- [JavaScript](https://www.javascript.com/)
- [jQuery](https://jquery.com/)
- [Materialize](https://materializecss.com)
- [Google Fonts](https://fonts.google.com/)
- [Git](https://git-scm.com/)
- [Github](https://www.github.com)
- [Heroku](https://id.heroku.com/)
- [WSL | Ubuntu](https://ubuntu.com/wsl)


## Testing

The testing of the website, both in development and as a finished product has been done through manual testing. As the manual test documentation became very long, it can be viewed in [this document](https://github.com/thorole/the-running-team/blob/master/documentation/testing/TESTING.md).

### Notes on defensive design

Since this website relies heavilly on the user for adding content, some measures has been implemented to prevent misuse. The most important feature is registering/login functionality. Even though this project does not focus on user authentication, this feature was added to the project to prevent random users to add, edit or even delete documents in the database.

In addition to authentication, back-end functions prevents users to brute-force deleting (via url field in browser) content that does not belong to them.

All comments, posts and events have a key called "element_id" which is set by the `get_random_string(length)` function. This assigns the key with a random string. This string is used to set the `id` of repeatedly generated elements, like delete modals. This way the ids of otherwise identical elements won't be repeated. Another solution would be to use the `_id` of the current item in the loop, but I chose this method to avoid exposing the `_id` of the item in the generated html. 

Other than that, all forms uses `required`, `max/min-length` and `pattern` attributes where relevant.

It's worth mentioning that regex for url inputs (like profile image) is somewhat strict, and users may experience that some urls does not fulfill the rquirements, even though it's a valid url. This is why a file upload should replace this feature in future updates of the site. The regex was picked up from [regex pattern](https://stackoverflow.com/questions/4098415/use-regex-to-get-image-url-in-html-js) and modified.

### Bug report

Through out development, there has been a series of minor and more complex bugs. The most important tool for debuggin has been printing information in the cli while the app is running. 

![Cli debug](documentation/images/db_debugging.png)

Debugging login

![Login debug](documentation/images/login_debugging.png)

The console was used to debug javascript. This image displays debugging of the function that sets the colors and widths of the progression bars.

![Progression bars debug](documentation/images/debug_progress_bar.png)

The built-in werkzeug-debugger has also been a very important tool to deal with bugs.

![Werkzeug-debugger](documentation/images/werkzeug_debug.PNG)

Other than this, printing variables directly on the templates using jinja has also been a method of debugging.

There is currently one known bug in the app. This bug is related to users who view the site on ios devices. All select inputs are more or less non-functional. When touching the select, the drop down of options is displayed, as intended. However, the user will be unable to choose their desired option. Instead, when pressing an option, what seems like a random option is selected. Luckily, just beneath the input, a small downward pointing arrow is visible, which lets the user utilize a standard select instead, which works as it should.

![ios select](documentation/images/ios_select.jpg)

This is a known issue with materialize selects and ios devices. Currently there are no known quick fixes. Some users on github has tried to provide solutions with javascript. Some of these were tried out for the project, but without success.

You can read more about the issue in this github thread:
[ios selects](https://github.com/Dogfalo/materialize/issues/6464)

*Note: this bug only arises on physical ios devices. In chrome dev-tools, when choosing an iphone, the select behaves as intended.*



### Testing and Responsiveness across browsers and devices
The website was built and tested in Chrome throughout the construction. In addition it has been tested
in Mozilla Firefox, MS Edge and Mac OS Safari. The website is responsive as intended across
all browsers used in testing.

The website has also been tested physically on iPhone S, ipad 2nd gen., iPhone 7 and Mi a2 Redmi note 7.
The website responds well to smaller screen sizes and no major problems have appeared, except for the select issue on ios. The site utilizes the materialize grid system and changes column sizing from small and up to x-large screens, depending on the view. For instance, the forms is either single column or two-columns, while "The Team" view has breakpoints for small, medium, large and x-large screens. During construction the site was constantly tested on phone sized
screen in the Chrome dev. tools to make sure it looked good and behaved as intended.

#### Tools used in testing
- [JsHint](https://jshint.com/) (0 warnings)
- [PEP-8 checker](http://pep8online.com/)(All right)
- [W3C Markup Validation](https://validator.w3.org/) (0 errors in html.)
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input)(0 errors in local css) 
- [Accessibility checker](https://www.achecker.ca) (Multiple known problems, all related to use of `<i>` for icons. In most cases, swapping with `<span>` solves the problem, but this does not translate well with materialize.)
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)


## Deployment

**This procedure was followed to deploy The Running Team**
For step 1 and 2, make sure you are in the root directory of your project. Don't forget to push the two new files to github before proceeding with the deployment.

1. Create a requirements file. In the cli it can be done by running the following command:
`pip3 freeze --local > requirements.txt`
2. Create a procfile. In the cli it can be done by running the following command: `echo web: python app.py > Procfile`
3. Log in to Heroku, click "New" > "Create new app"
4. Give the project a unique name, choose region and click "Create app".
5. Scroll down to "deployment method"-section. Choose "Github" for automatic deployment.
6. From the inputs below, make sure your github user is selected, and then enter the name for your repo. Click "search". When it finds the repo, click the "connect" button. 
7. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up your variables for IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME.
8. Scroll back up and click "Deploy". Scroll down and click "Enable automatic deployment". 
9. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.

**To clone the repository, follow these instructions:**

1. Navigate to the [repository](https://github.com/thorole/encryptinator)
2. Click **Clone or download**
3. Copy the url from the **Clone or download** dropdown.
4. In cli, navigate to the folder where you want to clone the repository.
5. Type *git clone*, and then paste the URL you copied in Step 3.
6. Press Enter

*Note: You will have to install all the dependencies from [requirements](https://github.com/thorole/the-running-team/blob/master/requirements.txt) for the app to work. In the cli, you can run the command* 

`pip install -r requirements.txt`

*You will also have to set up an* `env.py` *file in the root directory of your project, and set up variables for IP, PORT, SECRET_KEY, MONGU_URI and MONGODB_NAME. In addition, you will have to setup a new collection and databases for the project in mongoDB.*

For more information, visit [Cloning a repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
on github.

## Credits

### Content
The background image in the nav bar section was taken from [Worlds Marathons](https://worldsmarathons.com/fr/article/why-are-east-african-runners-so-dominant-).

The image used in the favicon and as default profile image was taken from [Vectorstock](https://www.vectorstock.com/royalty-free-vector/running-runner-man-marathon-logo-jogging-emblems-vector-13465761).

Image in 404 page was taken from [this](http://glosfit.co.uk/10-reasons-not-improving/sad-runner/) website.

All other images are provided by the users.


### Acknowledgements

Some inspiration for "The Team" section was picked up from the home of football team [Real Madrid](https://www.realmadrid.com/en/football/squad).

Thanks to my mentor [Jonathan Munz](https://github.com/jpmunz) for guidance on the project and for providing online litterature.

Thanks to [Tim](https://github.com/TravelTimN) at [Code Institute](https://github.com/Code-Institute-Org) for letting me preview the updated videos of the mini project [Task Manager](https://github.com/TravelTimN/flask-task-manager-project). Large parts of the register and login/log out functionality were picked up from these videos.

