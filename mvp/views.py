# Create your views here.
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from mvp.models import Wish, Student, Tag

from controls import *

@csrf_protect
def main( request ):

    return render_to_response( "main.html", {
            "title": "Test",
        },
        context_instance = RequestContext( request )
    )

def add( request ):
    # fetch tags
    # tags = request.POST["tags"]
    # tags = tags.split(",")

    tags = extract_tags( request.POST["tags"] )

    # create student
    user = User.objects.get( username="ilyakh" )
    student = Student( user=user )
    student.save()

    # create wish
    wish = Wish( student=student )
    wish.save()

    # generate tag objects (fires off only if there are elements in tags)
    for t in tags:
        candidate = Tag.objects.get_or_create(keyword=t)[0]
        wish.tags.add(candidate)
        wish.save()

    return redirect( display )

@csrf_protect
def display( request ):

    # fetch data from the database
    wishes = [w for w in Wish.objects.all()]

    return render_to_response( "display.html", {
            "title": "Test",
            "wishes": wishes
        },
        context_instance = RequestContext( request )
    );

@csrf_protect
def flush( request ):

    tables = [Tag, Student, Wish]

    # import mvp
    # from django.db import models
    # print [model for model in mvp.models.__dict__]

    map( lambda x: x.objects.all().delete(), tables )
    table_names = ", ".join([ table.__name__ for table in tables ])

    return render_to_response( "dialog.html", {
            "title": "Flush entries",
            "message": "The tables for %s has been flushed" % ( table_names )
        },
        context_instance = RequestContext( request )
    )