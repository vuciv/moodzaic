# moodzaic

# For graders!

## Initial Setup

Clone https://github.com/reyesj5/moodzaic

Cd into `/moodzaic/moodzaic_django/frontend`

Run `npm install`

Run `npm install node.js`

Run `npm run start`

In a new window, cd into `/moodzaic/`

Run `python3 -m venv env` (make sure to have virtualenv installed with python's pip)

Run `source env/bin/activate`

Run `pip install -r requirements.txt`

Cd into `/moodzaic/moodaic_django`

Run `python3 manage.py makemigrations`

Run `python3 manage.py migrate`

Run `python3 manage.py runserver`

It will possibly fail, so run  python3 manage.py runserver again until it works

## Navigation

Go to http://127.0.0.1:8000/ to see the login screen

Go to http://127.0.0.1:8000/api/users/ to add a user, then click Post to submit

Return to http://127.0.0.1:8000/ and login with the credentials you just created

Enjoy the Profile page, and feel free to click the Record Mood link to see the Record Mood page

# Summary Workflow
The following is a basic workflow that you can use as a quick reference for developing a Django Project.

## Django Setup
Within repo directory, create and activate a virtualenv.

`python3 -m venv path/env`

`(Linux/mac) source env/bin/activate`

`(windows) \env\Scripts\activate.bat`

Install Django and other dependencies.

`pip install -r requirements.txt`

(optional) Create your project:

`django-admin.py startproject <name>`

Create a new app (inside django project folder):

`python manage.py startapp <appname>`

Add your app to the `INSTALLED_APPS` tuple in project `setting.py`


## Add Basic URLs and Views
Map your Project’s `urls.py` file to the new app.
In your App directory, create a urls.py file to define your App’s URLs.
Add views, associated with the URLs, in your App’s `views.py`; make sure they return a HttpResponse object. Depending on the situation, you may also need to query the model (database) to get the required data back requested by the end user.

## Templates and Static Files
Create a templates and static directory within your project root.
Update settings.py to include the paths to your templates.
Add a template (HTML file) to the templates directory. Within that file, you can include the static file with - `{% load static %}` and `{% static "filename" %}`. Also, you may need to pass in data requested by the user.
Update the views.py file as necessary.

## Models and Databases
Update the database engine to `settings.py` (if necessary, as it defaults to SQLite).
Create and apply a new migration.
Create a super user.
Add an `admin.py` file in each App that you want access to in the Admin.
Create your models for each App.
Create and apply a new migration. (Do this whenever you make any change to a model).

## Forms
Create a forms.py file at the App to define form-related classes; define your ModelForm classes here.
Add or update a view for handling the form logic - e.g., displaying the form, saving the form data, alerting the user about validation errors, etc.
Add or update a template to display the form.
Add a urlpattern in the App’s `urls.py` file for the new view.

## User Registration
Create a UserForm
Add a view for creating a new user.
Add a template to display the form.
Add a urlpattern for the new view.

## User Login
Add a view for handling user credentials.
Create a template to display a login form.
Add a urlpattern for the new view.

## Setup the template structure
Find the common parts of each page (i.e., header, sidebar, footer).
Add these parts to a base template
Create specific. templates that inherent from the base template.

# Running Front-End Scripts

## Set-Up
In /user-interface/moodzaic, and with yarn installed, run "$yarn start" to launch the React App in a browser, and "$yarn test" to run the included test suites.

# Information for Milestone 3.b (11/14/19)
As we've learned, making a web app is complicated, and our goals for the first iteration were overly ambitious. Nevertheless, we've built an app over the past week that works a long way (but not all the way) towards our goals. Laying out Moodzaic It.1:

On the front-end (Molly and Daniel), we have 14 React components, which are spread across 7 screens: log-in, sign-up, account setup, mood input, profile, my communities, and individual communities. These screens are actually all part of a single page web app that uses routing to redirect the user. Through Axios and REST APIs, this front-end is integrated with models for users and profiles (Emil and Hunter), communities (Zippy and Jersey), and observations (as part of the larger ML suite worked on by Marco and Chema).

Notably, logging in and signing up operate through the User API to get users and post new ones, respectively. Communities can be created and deleted from the communities tab, with corresponding changes on the back-end. Recording your mood posts the observation to the back-end, where it's used to train the ML algorithm for predicting mood.

Signing out takes you back to the log-in screen. Additionally, make sure to click the red panda icon!

## Notes
To signup, after hitting the sign-up button on the log-in landing, you must reload to see the changes take effect. This is the only routing case where this happens, and we're not sure why.

Despite the components all rendering, many of the front-end (React App) render tests are failing. This is due to an annoying bug from routing, which is making our components unable to directly render to the DOM without a routing table. Know that the functionality is there, but we didn't manage to change the tests to accomodate it.
