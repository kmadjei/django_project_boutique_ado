![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
![CBC Logo](https://canadianbusinesscollege.com/wp-content/uploads/2020/09/CBC-New-Logo-Website.png)

# Milestone Project - Boutique Ado

Welcome to Project Boutique Ado, an E-commerce Web Application built with the power of Django - Python Framework. 

Features of this project includes:
- product search with filter functionalities
- Full functional payment system integration with Stripe
- Authentication system with email notification and user stories
- And realtime notifications that guide the user's experience

The project is deployed live on Heroku. Check the link below for quick access.
👉 [Quick Preview](https://kmadjei-boutique-ado.herokuapp.com/)

 
## UX
 
The purpose of this project was to build a web application based around business login used for selling products online to interested clientele. The site owner's goal is to make profits by selling products to customers through an online platform. The user's/customer's goals are met through finding products they need or want by browsing through the catalogs of products available on the website platform.

The **user stories** below showcases the variety of functionalities built into the project.

### E-Commerce User Stories

- **Viewing and Navigation**
    - As a shopper, I want to be able to view a list of products, so that I can select some to purchase
    - As a shopper, I want to be able to view individual product details, so that I can identify the price description product rating, product image and available sizes
    - As a shopper, I want to be able to quickly identify deals, clearance items, and special offers, so that I can take advantage of special savings on products i'd like to purchase
    - As a shopper, I want to be able to easily view the total of my purchases at any time, so that I can avoid spending too much

- **Registration and User Accounts**
    - As a site user, I want to be able to easily register for an account, so that I can have a personal account and be able to view my profile.
    - As a site user, I want to be able to easily login or logout, so that I can access my personal account information.
    - As a site user, I want to be able to easily recover my password incase I forget it, so that I can recover access to my account.
    - As a site user, I want to be able to receive an email confirmation after registering, so that I can verify that my account registration was successful.
    - As a site user, I want to be able to have a personalized user profile, so that I can view my personal order history and order confirmations, and save my payment information.

- **Sorting and Searching**
    - As a shopper, I want to be able to sort the list of available products, so that I can easily identify the best rated, best priced and categorically sorted products.
    - As a shopper, I want to be able to sort a specific category of product, so that I can find the best-priced or best-rated product in a specific category or sort the products in that category by name.
    - As a shopper, I want to be able to sort multiple categories of products simultaneously, so that I can find the best-rated products across broad categories, such as "clothing" or "home-ware".
    - As a shopper, I want to be able to search for a product by name or description, so that I can find a specific product I'd like to purchase.
    - As a shopper, I want to be able to easily see what I've searched for and the number of results, so that I can quickly decide whether the product I want is available.

- **Purchasing and Checkout**
    - As a shopper, I want to be able to easily select the size and quantity of a product when purchasing it, so that I can ensure I don't accidentally select the wrong product, quantity or size.
    - As a shopper, I want to be able to view items in my bag to be purchased, so that I can identify the total cost of my purchase and all items I will receive
    - As a shopper, I want to be able to adjust the quantity of individual items in my bag easily, so that I can easily make changes to my purchase before checkout.
    - As a shopper, I want to be able to easily enter my payment information, so that I can check out quickly and with no hassles.
    - As a shopper, I want to be able to feel my personal information is safe and secure, so that I can confidently provide the needed information to make a purchase.
    - As a shopper, I want to be able to view an order confirmation after checkout, so that I can verify that I haven't made any mistakes
    - As a shopper, I want to be able to receive an email confirmation after checking out, so that I can keep the confirmation of what I've purchased for my records.

- **Admin and Store Management**
    - As a stor owner, I want to be able to add a product, so that I can add new items to my store.
    - As a store owner, I want to be able to edit/update a product, so that I can change product prices, descriptions, images, and other product criteria.
    - As a store owner, I want to be able to delete a product, so that I can remove items that are no longer for sale.

### Mock Ups

**Home Page**
<img src="https://github.com/kmadjei/django_project_boutique_ado/blob/main/boutique-ado-mockups/home-desktop.PNG?raw=true" alt="Home-desktop Mock Ups" width="300" height="300">
<img src="https://github.com/kmadjei/django_project_boutique_ado/blob/main/boutique-ado-mockups/home-mobile.PNG?raw=true" alt="Home-mobile Mock Ups" width="300" height="300">

**Products Page**
<img src="https://github.com/kmadjei/django_project_boutique_ado/blob/main/boutique-ado-mockups/products-desktop.PNG?raw=true" alt="products-desktop Mock Ups" width="300" height="300">
<img src="https://github.com/kmadjei/django_project_boutique_ado/blob/main/boutique-ado-mockups/products-mobile.PNG?raw=true" alt="products-mobile Mock Ups" width="300" height="300">


## Technologies Used

- [HTML](https://www.w3schools.com/html/default.asp)
    - The project uses **HTML** to produce the web contents.

- [CSS](https://www.w3schools.com/CSS/default.asp)
    - The project uses **CSS** to create visually pleasing content.

- [Bootstrap 4.4](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - The project uses **Bootstrap** version 4.4, frontend design framework, to produce better UI/UX for mobile first development.

- [Python](https://www.python.org/doc/)
    - The project uses **Python** to process server side queries, such as processing payments and user authentications.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation for UI contents.

- [Django](https://www.djangoproject.com/)
    - The project uses the **Django** , Python Full Stack framework, to simplify and speedup the development of a Full Stack Web Application.

- [PostgreSQL](https://www.heroku.com/postgres)
    - In this project, **Heroku Postgres** is relational database addon chosen to handle database management when deployed.

- [AWS](https://aws.amazon.com/)
    - **Amazon Web Services (AWS)** is used to host the static files for the deployed project.

- [Stripe](https://stripe.com/en-ca)
    - **Stripe** is the software utilized for the payment system in this project .



## Testing

1. Responsive Web Design:
    1. User visits site on mobile or tablet device.
    2. The website adjusts to the different screen sizes and displays UI elements in a neat and clean structure for the user experience

2. Viewing and Navigation:
    1. User chooses a product category or filters out the list for a specific interests
    2. The web application retrieves the desired results for the user to find the best priced and best quality products.
    3. Selecting a product results in navigating to desired product page with detail of the product.
    4. Shopping bag also displays price for selected products, along with notifications allowing user to keep track of purchases
 

3. Registration and User Accounts:
    1. On registration page, submitting an empty form prompts user with an error message to fill out the required fields.
    2. On successful registration, user receives email notification and feedback message to check the personal email.
    3. Application sends feedback message for using a different user id for registration if the current ID already exist.
    4. Once logged in the user is able to log out with no issues.
        1. User is also capable of tracking payment records of purchased products.

3. Purchasing and Checkout:
    1. Clients buying a product on the site are able to update or delete the product with a feedback notification.
    2. On successful purchase of a product, stripe processes the payment information for irregularities and keeps record of the event in the backend dashboard.
    3. Testing the stripe webhook for avoiding repeated purchase of the same order cause by a customer mistake showed a successful response.
    4. Transactions completed by a shopper is not revealed to another shopper when checking their transaction records on their profiles.

4. Admin and Store Management:
    1. Store owner attempting to edit, delete, or add a product is capable of doing so with the admin login.
    2. Regular user's are unable to manipulate values of the products on the e-commerce site.

 

## Deployment

The E-commerce FullStack Django project has been deployed to 👉[Heroku.](https://kmadjei-boutique-ado.herokuapp.com/)👈

### Deploying To Heroku

1. In order to deploy to heroku, a Github repository was created for the project.
2. Make sure to have downloaded [Git Bash](https://www.atlassian.com/git/tutorials/git-bash)
3. Go to the root folder directory of the app on the local computer.
4. Right click it and select **Git Bash here** to open the CLI terminal.
5. Initialize the project directory by typing ```git init``` in the terminal and pressing the Enter key.
6. Copy the url of the Github repository created for the app.
7. On the terminal, add the url you copied, as a remote with the command 
    ```git remote add origin <paste your github URL here> ```
    1. Make sure to also install **gunicorn** with ```pip install gunicorn``` in the terminal, inorder to deploy to heroku
8. Next, commit all your changes to git with these commands
    ```bash
    git add . 
    git commit -m "Your message here. Example <First commit>"
    ```
9. Create the main branch of your repository with the command ```git branch -M main```
10.  After the steps above,  the project can now be pushed to the repository with the command ```git push```
11. Now the project is ready to be deployed to Heroku.
12. Before deploying our Python App to Heroku, 2 files will need to be created. **Procfile and Requirements.txt**
    1. In the gitbash terminal of the root folder directory of the project. Run these commands to create the procfile and requirements.txt. Note: Make sure you have downloaded and added python to your environment variables.
    ```bash
    pip3 freeze --local > requirements.txt
    touch Procfile
    ```
    2. Make sure the Procfile created has a capital "P" in the title. Open the Procfile in a text editor and add this line of text on the first line ```web: gunicorn boutique_ado.wsgi:application```. Note: make sure there is not extra line after the first one. Not even an empty line.
    3. Repeat step 8 and 10 of the steps above.
13. After creating an account on Heroku, an app name where the project is hosted will need to be created from the dash board.
<img src="https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/blob/master/static/images/herokudeploy/heroku-new.PNG?raw=true" alt="Deploy image">

14. Select the app created.
<img src="https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/blob/master/static/images/herokudeploy/appname.PNG?raw=true" alt="Deploy image">

15. Click on the settings tab and then click the **Reveal Config Vars** to add the config variables of the python application.
<img src="https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/blob/master/static/images/herokudeploy/settings.PNG?raw=true" alt="Deploy image">

16. The following are the config vars to be added. Note: Some were given upon integrating functionalities such as stripe intents and webhooks.
    1. AWS_ACCESS_KEY_ID
    2. AWS_SECRET_ACCESS_KEY
    3. DATABASE_URL
    4. EMAIL_HOST_PASS
    5. EMAIL_HOST_USER
    6. SECRET_KEY --> for django
    7. STRIPE_PUBLIC_KEY
    8. STRIPE_WH_SECRET
    9. STRIPE_SECRET_KEY
    10. USE_AWS = True
17. Once the config vars are added, navigate to the **Deploy** tab.
<img src="https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/blob/master/static/images/herokudeploy/deploytab.png?raw=true" alt="Deploy image">

18. In the diployment section, select Github for the deployment method and connect to the github repository for the project by searching for its name.
<img src="https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/blob/master/static/images/herokudeploy/deploy.png?raw=true" alt="Deploy image">

19. Further down the page you will have to select the automatic deployment and for the manual deploy section, choose main branch and click the ```Deploy Branch``` button.
<img src="https://github.com/kmadjei/MilestoneProject-Python-and-DataCentricDevelopment/blob/master/static/images/herokudeploy/viewlive.png?raw=true" alt="Deploy image">

20. The above steps will cause Heroku to process the project files and create a link for you to view the live deployment of the Flask Web Application Project.


## Credits

### Content
- The content to complete this [project](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546) was provided by the Code Institute.

### Media
- Media files for the E-commerce project was provided by the Code Institute. 

### Acknowledgements

- The completion of the Boutique Ado, Django Full Stack Development Project module, would not have been possible without the guidance of the Code Institute instructors and my instructor, Usmaan Mujtaba, at the Canadian Business

### other resources
- [Django Documentation](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/)
