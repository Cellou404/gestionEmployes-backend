# `projects` app documentation

In this application, **user** can:

- create project
- update project
- delete project
- mark it as completed

## 1 - Models

We have two model

### First model

The first one is called `Project`

Fields given are:

- title
- owner
- description
- complete
- created
- slug

### Second model

The second on is `ProjectTask`

Fields given are:

- project
- task name
- description
- complete
- created
- slug

We have a `save` method that will fill the slug field so the we don't have to manualy type it

    The relation between these models is that each project can have multiple tasks witch 
    should be completed. When all tasks are completed, we suppose that the project is also completed

## 2 - Serialzer

We also have two serializers class

In the `serializers.py` file, we have these serializers classes that *serialize* our datas

The First one is `ProjectSerializer` and the second one is `ProjectTaskSerializer`

we used StringRelatedField() method for foreign objects *owner* and *project*

In the meta class:

the target models are `Project` and `ProjectTask`

`__all__` all fields will be serailized

## 3 - Views

Here are our views:

1. ProjectView

   Replace #slug by an employee slug

   Returns a list of all **projects** from the database.

    Create **projects** in the database.

    For listing & Creation [see here][ref].

    [ref]: http://localhost:8000/api/projects/

2. ProjectTaskCreateView

   Creatin a model instance.
    Create **project tasks** in the database.

    For creation [see here][ref].

    [ref]: http://localhost:8000/api/projects/`project-slug`/project-task-create/

    Replace `project-slug` by particular project slug since the lookup field is `slug`

    Or [see here][ref].

    [ref]: .views.py

3. ProjectTaskListView

    Returns a list of all **project tasks list** from the database.

    Each project can have mutiple tasks that have to be completed

4. ProjectTaskUpdateDeleteView

    Retrieve, Update and Delete project **tasks**

## 3 - Urls

We have four roots:

1. The default root is: http://localhost:8000/api/projects/

2. http://localhost/projects/project_slug/project-task-create/

3. http://localhost/projects/project_slug/project-tasks/

4. http://localhost/projects/project_slug/project-tasks/pk/

The lookup fields are `slug` and `pk`. So replace `...__slug` by a real slug text.
