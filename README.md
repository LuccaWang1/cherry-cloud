<a name="top"></a>

# Cherry Cloud

<img src="/static/images/cherry.webp" alt="Cherry Logo" width="100px" height="100px" />

_The Cherry Cloud logo_

<a name="desc"></a>

## Description

Cherry Cloud is a full stack web app built from scratch by Agne Djacenko and Lucca Wang. The collaborative project is a platform, where users can create an account, shop, blog, and play the game Flappy Cherry.

<a name="index"></a>

## Table of Contents

- [Name](#top)
- [Logo](#top)
- [Description](#desc)
- Index
- [Features](#features)
- [Technologies and Requirements](#tech)
- [Data Model](#model)
- [How To Run](#run)
- [Authors](#authors)
- [How to Contribute (for collaborative authors)](#contribute)

<a name="features"></a>

## Features

- Blog
- Shopping cart
- Products page + cards
- React game
- User authentication (user accounts) and a Postgres database
- Password hashing (security within authentication)
- Weather updates and conditions (API)
- Payment processing (API)
- Dark mode
- Romantic mode
- User feedback, ongoing maintenance

[Back to the Table of Contents](#index)

<a name="tech"></a>

## Technologies and Requirements

- Python (backend)
- CSS (frontend)
- Data model (pre-backend work, sets up Postgres database)
- Flask (Python framework)
- HTML (frontend, templates)
- JavaScript (frontend)
- Jinja2 (Python templating engine)
- Markdown (used to create README)
- Payment processing API (API integration and calls)
- Passlib and Argon2 (password hashing)
- PostgeSQL (relational database)
- React (Flappy Cherry game, reuseable components update in real time without refreshing the page)
- Weather API (API integration and calls)

[Back to the Table of Contents](#index)

<a name="model"></a>

## Data Model

This will be updated

[Back to the Table of Contents](#index)
<a name="run"></a>

## How to Run

Expose environment variables:

```bash
This will be updated
```

Install the project:

```bash
$ git clone https://github.com/LuccaWang1/cherry-cloud
$ virtualenv env
$ source env/bin/activate
(env) $ pip3 install -r requirements.txt
(env) $ createdb cherry-cloud
$ python3 model.py
```

To run the server:

```bash
$ python3 server.py
open localhost:5000
```

Run the tests:

This will be updated

```bash
$ python3 tests.py
```

[Back to the Table of Contents](#index)

<a name="authors"></a>

### Authors

- Agne Djacenko
- Lucca Wang

[Back to the Table of Contents](#index)

<a name="contribute"></a>

### How to Contribute

You can only contribute to this project if you are listed as a collaborator on the project remote repo in GitHub. (You must respond to the email sent to you from Github and accept the invitation to become a contributor on the project.)

#### Git

##### First getting started:

1. Clone the repo onto your local machine
   `git clone https://github.com/LuccaWang1/cherry-cloud`

##### Creating a branch

1. `cd` into your project directory
2. `git branch` to check what branch you are currently on (you will see a star next to it)
3. Make sure you are on your main branch
   `git checkout main`
4. It's good practice to pull from main before creating a new branch. (This will help you avoid merge conflicts.) (Github = origin)
   `git pull origin main`
5. Create a new branch every time you work on something new (each ticket). The branch name should be short and descriptive.
   `git checkout -b trello_ticket_number_then_branch_name`

##### Working on your branch

1. `git branch` to make sure you're on your new branch. If not, `git checkout` like above to get on your new branch.
2. Work on your code, make your changes
3. Commit often after any change

   ```
   git status
   git add .
   git commit -m "descriptive message of changes - in past tense format"
   ```

##### Pushing your code to Github

1. Push the changes in your branch to Github
   `git push origin branch_name`
2. Now if you look at the repo on Github you will see 'Your recently pushed branches.'
3. Click on 'Compare & pull request'
4. See the changes you made and click the green button 'Create pull request'

##### Pull your changes

1. In the previous step, you created a pull request, which is a request to merge your branch into the main branch.
2. You will be able to see if you have merging conflicts or not.
3. If you get a green thumbs up, click the green button 'Merge pull request'.
4. Now your branch and code has merged into the main code base.

##### Update local main and delete feature branch

1. Return to the main branch
   `git checkout main`
2. Make sure to update the code on your local machine to match the most up-to-date code living in the main branch on Github.
   `git pull origin main`
3. It's good practice to delete the old branch.
   `git branch -D branch_name`
4. Create a new branch off of main to keep on coding.
   `git checkout -b new_branch_name`

[Back to the Table of Contents](#index)

[Back to Top](#top)
