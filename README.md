# THIS PROJECT IS NOT MAINTAINED AND NEVER WAS IN A USABLE STATE IN ANY POINT IN TIME WITH ANY DJANGO VERSION!!!

If you need this functionality, please use [django-admin-toolbox](https://github.com/gbdlin/django-admin-sidebar) which aims to bring more than just a sidebar.

# Admin sidebar

This django app adds sidebar to the left of standard django admin template.
It also replaces index screen with simple message.

Purpose of this sidebar is to replace default list of models in django admin with
something more customizable and useful.

## Instalation
    1. clone it to your project (no pip package yet) using:

        git clone git://github.com/gbdlin/django-admin-sidebar.git@latest admin_sidebar

    2. add `admin_sidebar` (or anything you've named it) at the top of your `INSTALLED_APPS` (at least above `django.contrib.admin`)
    3. add `admin_sidebar.context_processors.admin_sidebar_content`

## Configuration

TBD
