# `employees` app documentation

It's in this application that we will create employees and their informations.

## 1 - Model

In `models.py` file we have a model called `Employee`

Fields given are:

* name
* email
* avatar
* designation
* bio
* phone
* address
* salary
* date hired
* slug

We have a method  `save` that will fill the slug field so the we don't have to manualy type it

## 2 - Serialzer

In the `serializers.py` file, we have this serializer class that *serialize* our datas

In the meta class:

the target model is `Employee`

`__all__` all fields will be serailized

## 3 - Views

Here are our views:

1. EmployeeListView

   Returns a list of all **employees** in the database.

   Create **employees** in the database.

   For listing [see here][ref].

   [ref]: http://localhost:8000/api/employees/

   For Creation [see here][ref].

    [ref]: http://localhost:8000/api/employees/#slug

   Replace #slug by an employee slug

2. EmployeeView

    Retrieve, Update and Delete a single **employee** from
    database

    For more details please [see here][ref].

    [ref]: http://localhost:8000/api/employees/

    The lookup field is `slug`

3. Urls

    We have two roots:

    The first path will display Employees list. Its also used for employee creation
    since in the **views** we used `ListCreateAPIView`

    This second path is used for **rud** (retrieve - update - delete) actions for a
    particular employee

    The lookup field is `slug`
