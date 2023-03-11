# Accounts app documentation

In this **accounts** application, You can create an account and the
you will be able to _signin_ in the system with it.

## Model

In the `models.py` we created a custom user model witch will be our default AUTH_USER_MODEL.

This time, the username field is `email` instead of `username` itself.

So when you create your account an then you want to signin, use your **email** as username
and make sure to enter the correct password.

## Views

We have only have one view. The **SignupView**

We use **APIView** to have more controle on our view

This **Signup View** allow people to create their account.

For more detail [see here][ref].

[ref]: http://localhost:8000/api/accounts/signup

## Urls

Use the link given above to [signup][ref] 
