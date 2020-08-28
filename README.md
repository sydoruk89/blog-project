# Django Models

**Author:** Roman Sydoruk **Version:** 1.0.0

## Description

The application creates a blog project with one model and wire up that model using Django Views.

## Architecture

* Python 3.8.3
* Poetry
* Django

## Usage 
* create blog_project project
* create blog app
* migrate data
* create Post model
    * add title as a CharField with maximum length of 64 characters.
    * add author ForeignKey related to Django’s built in user model with CASCADE delete option.
    * add body TextField
* add model to admin
* modify Post model have user friendly display in admin
* create migrations and migrate data
* create a super user
* Add a few posts via Admin panel
* Addtemplates folder in root of project
    * register templates folder in project settings
* create HomePageView
    * extend ListView
    * give a template of home.html
    * associate Post model
* create home.html template
    * use Django Templating Language to display each post’s title
* create base.html ancestor template
    * add main html document
    * use Django Templating Language to allow child templates to insert content
* update url patterns for app and project
* view home page and confirm posts showing properly
* add detail view
    * link post_detail.html template
    * associate Post model
* create post_detail.html template
    * template should extend base
    * content should display post title and body
