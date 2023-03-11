# `employees` app documentation

In this Tasks application, Users will create their daily tasks and will should complete
them

## 1 - Model

In `models.py` file we have a model called `Task`

Fields given are:

* title
* owner
* description
* complete
* created
* slug

We have a method  `save` that will fill the slug field so the we don't have to manualy type it

## 2 - Serialzer

In the `serializers.py` file, we have this serializer class that *serialize* our datas

In the meta class:

the target model is `Task`

`__all__` all fields will be serailized

## 3 - Views

Here are our views:

1. TasksListView

   View for Listing or  Creating a model instance.

    Returns a list of all **tasks** from the database.
    Create **tasks** in the database.

    For listing & Creation [see here][ref].

    [ref]: http://localhost:8000/api/tasks/

2. TaskDetailView

    Retrieve, Update an delete a **task** from the database.

    For more details [see here][ref].

    [ref]: http://localhost:8000/api/tasks/#task_slug/

    Replace **#task__slug** by an existing **task slug**

## 3 - Urls

We have two roots:

The first path will display tasks list. Its also used for tasks creation
since in the **views** we used `ListCreateAPIView`

The second path is used for **rud** (retrieve - update - delete) actions for a
particular task

**NB:** The lookup field is `slug`
