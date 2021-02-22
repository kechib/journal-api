## Journal Mia - A Music Journal

## Links
[Front End Repo -->](https://github.com/kechib/journal-client)
[Journal-Mia App -->](https://kechib.github.io/journal-client)


## Description:
Journal Mia is a music journal web application that allows users to create an account and make Journal Entries with a content description of their choice. Users can add embed Apple Music songs to describe their feelings at the moment of their entry. Users will be able to see and reflect on their entries by date.This project was created with Django and postgresql. The api uses models, views and curl-scripts to create the backend application.


## Planning Story
- Create wireframes and ERD.
- Create user and journal models.
- Make migrations
- Create user and journal views.
- Create user  and journal serializers.
- Create and test authorization events using curl scripts.
- Create and test journal routes using curl-scripts



## User Stories
User

- As a user I want to be able to sign-up/sign-in
-	As a user I want to be able to change-password
-	As a user I want to be able to sign-out

Journal

-	As a user I want to make a journal entry
-	As a user I want to view a single journal entry
-	As a user I want to view all my journal entries
-	As a user I want to edit an entry I created
-	As a user I want to delete an entry I created


## Technologies Used
- Django
- Postgresql
- Heroku
- Python


## Authentication
| Verb   | URI Pattern             | Controller#Action |
|:-------|:----------------------- |:------------------|
| POST   | `/sign-up/`             | `users#signup`    |
| POST   | `/sign-in/`             | `users#signin`    |
| PATCH  | `/change-password/`     | `users#changepw`  |
| DELETE | `/sign-out/`            | `users#signout`   |

## Journal Routes
| Verb   | URI Pattern                | Controller#Action|
|:-------|:----------------------     |:-----------------|
| GET    | `/journals/`               | `journals#index` |
| GET    | `/journals-show/:journalId`| `journals#show`  |
| POST   | `/journals-create/`        | `journals#create`|
| PATCH  | `/journals-edit/`          | `journals#update`|
| DELETE | `/journals/:journalId`     | `journals#destroy`

## WireFrames
![ERD](./erd.png)
