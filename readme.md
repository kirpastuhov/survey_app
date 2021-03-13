Survey App
===

##  Description

Implement a simple API for creating surveys.

## Getting started
Go to project directory and start the server by pasting the following line into your terminal:

```
python3 manage.py migrate
python3 manage.py runserver 
```

This will fire up the server on *localhost:8000* 

## Create Admin User
Create new admin user who will have access to create and edit surveys.
```
POST /api/v1.0/users/

{
    "username":"name",
    "password":"pass"
}

```

## Get Token

In order to create a survey, you need to pass Authentication Token to your request. 
To get that token send
```
POST /api/v1.0/auth/

{
    "username":"name",
    "password":"pass"
}
```
If username and password are correct, you will a token that can be used in other requests 
```
{"token":"token_str"}
```

## Surveys

List all surveys
```
GET /api/v1.0/surveys/
```

Create new survey

```
POST /api/v1.0/surveys/ 
Authorization: Token <token>

{
    "title": "survey_title",
    "description": "survey_description",
    "end_date": "2022-01-01"
}
```

Update survey

```
PATCH /api/v1.0/surveys/<survey_id>/
Authorization: Token <token>

{
    "title": "new_survey_title",
    "description": "new_survey_description",
    "end_date": "2020-01-01"
}
```

Delete survey

```
DELETE /api/v1.0/surveys/<survey_id>/
Authorization: Token <token>
```

## Questions

List all questions
```
GET /api/v1.0/questions/
```

Create new question for survey

```
POST /api/v1.0/questions/ 
Authorization: Token <token>

{
    "text": "question_text",
    "type": "choices - TEXT/SINGLE/SEVERAL, deafult - TEXT",
    "survey": <survey_id>
}
```

Update question

```
PATCH /api/v1.0/questions/<question_id>/
Authorization: Token <token>

{
    "text": "question_text",
    "type": "choices - TEXT/SINGLE/SEVERAL, deafult - TEXT",
    "survey": <survey_id>
}
```

Delete question

```
DELETE /api/v1.0/questions/<question_id>/
Authorization: Token <token>
```

## Answers

Answer survey questions
```
POST /api/v1.0/answers/

{
    "answer": "answer_text",
    "user_id": 2,
    "question": <question_id>
}
```

Get user's answers by id

```
GET /api/v1.0/user_surveys/<user_id>/
```
