<h1 align="center">TAMID at Yale URL Shortener</h1>

The [TAMID at Yale URL Shortener](https://urlshortnertamid.herokuapp.com/) is a URL shortening web application.

## Overview

The [TAMID at Yale URL Shortener](https://urlshortnertamid.herokuapp.com/) is a RESTFUL web service that permits users to POST a URL and recieve a shorter URL in return.


The backend of the project was built using the high-level Python web framework [Django](https://www.djangoproject.com/).
The frontend of the project was built using custom styling via [CSS](https://www.w3.org/Style/CSS/Overview.en.html) and pre-built styles and themes from [Bootstrap](https://getbootstrap.com/).

## Access

To experiment with and use the web application, visit The [TAMID at Yale URL Shortener](https://urlshortnertamid.herokuapp.com/), and follow the directions to have a fun time!

However, for examples of how the web application works, long URLs such as http://catalog.yale.edu/ycps/subjects-of-instruction/computerscienceandeconomics/ would be shortened to https://urlshortnertamid.herokuapp.com/dd96f, for a more easily accessible link.

## Features
- [x] Fast and lightweight
- [x] RESTFUL web service that allows users to POST a URL and recieve a shorter URL
- [x] A web application for users to access the service's features

## Run Locally and Install Requirements

To run this project locally, first clone the repository and then install all of the necessary dependencies by running `install all of the necessary dependencies`. Once you have done that, run `python manage.py makemigrations` and `python manage.py migrate` to make your migrations and `python manage.py runserver` to run your web application locally.

## Developement Process

While I had initially built this web application using both Vue.js and Node.js, I ultimately decided to switch to a Django implementation because of its ease of deployement. Further, while I had initially set out on doing all of the stying for the project by myself, I came to the conclusion that doing so would tedious and also not yield the best results. Thus, I favored using Boostrap themes in my web application, to make it look more clean and appealing.

While implementing this URL shortener some challenges I faced were redesigning my implementation to match the requirenments of all of the different frameworks that I experimented with. While choosing just one framework initially and then running with it would have been the smartest idea, because I did not do so, I faced the challenge of having to restart my project and sometimes even switch languages, several times over the course of my developement process.

This being said, having to redesign my implementation so many times gave me inspiration for additional features that I hope to add to my web application in the future. These features include being able to keep track of all of the URLs that you have shortened and how many times they have been used (Which I had initially implemented in my Node.js implementation), creating a login and registration portal, and being able to provide your own custom ID for the shortened URL.