Message Wall : A mini blog hosted by pythonanywhere.com implemented using Flask framework.


Description:

    A very simple project to get a feel of Flask framework and building a blog from scratch.
This website uses a SQL-Alchemy database to support user login, user posts, and other functionalities
and information about the user. 

Tables for Message Wall database:
    +--------------------------------+
    | Tables_in_endlessLoop$comments |
    +--------------------------------+
    | alembic_version                |
    | comment                        |
    | comment_popup                  |
    | followers                      |
    | message                        |
    | notification                   |
    | post                           |
    | user                           |
    +--------------------------------+

    A rudimentary ansynchronyous email sending is implenmented when the user request a password reset.
This asynchronyous functionality is allowed by importing Python's Threads in the email.py module.

Language: Python3.7
 
 
Website:    https://endlessloop.pythonanywhere.com



Reference:
    https://blog.miguelgrinberg.com/
    https://flask.palletsprojects.com/en/1.1.x/
    https://getbootstrap.com/docs/4.4/getting-started/javascript/
    https://getbootstrap.com/docs/4.4/components/popovers/
