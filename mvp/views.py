# Create your views here.
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from mvp.models import Wish, Student, Tag

from controls import *

@csrf_protect
def main( request ):

    return render_to_response( "add.html", {
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

    map( lambda x: x.objects.all().delete(), tables )
    table_names = ", ".join([ table.__name__ for table in tables ])

    return render_to_response( "dialog.html", {
            "title": "Flush entries",
            "message": "The tables for %s has been flushed" % ( table_names )
        },
        context_instance = RequestContext( request )
    )


# Temporary test-specific views
@csrf_protect
def intrude( request, username ):

    previous_username = request.user
    auth.logout( request )
    user = auth.authenticate( username=username, password="123" )

    if user != None:
        auth.login( request, user )

        out = render_to_response( "dialog.html", {
                "title": "Fast intrusion",
                "message": "You were logged in as: %s, and now you are logged in as %s" % (previous_username, username),
            },
            context_instance = RequestContext( request )
        )

    else:
        out = render_to_response( "dialog.html", {
                "title": "Fast intrusion failed",
                "message": "You are still logged in as: %s, user %s was not authenticated" % (previous_username, username)
            },
            context_instance = RequestContext( request )
        )

    return out;


# Testing

def display_students( request ):
    users = Student.objects.all()
    output = [u.username for u in users]

    return render_to_response( "dialog.html", {
            "title": "All registered students",
            "message": "Listing %d students" % (len(output)),
            "set": output
        },
        context_instance = RequestContext( request )
    )

def populate_students( request ):
    data = open( "./gen/test/users.dat", "r" ).readlines();

    from management.usermanagement import UserManagement
    manager = UserManagement()

    for line in data:
        manager.adduser( line )
        manager.updateuser( line, arg="s" )

    return redirect( "/test/students/" )


def populate_wishes( request ):
    SEPARATOR = " "
    data = open( "./gen/test/wishes.dat", "r" ).readlines();

    from management.wishmanagement import WishManagement
    manager = WishManagement()

    for line in data:
        candidate = line.split( SEPARATOR )
        manager.addwish( candidate[0], candidate[1:] )

    return redirect( "/test/wishes/" )

def display_wishes( request ):
    wishes = Wish.objects.all()

    output = []
    for w in wishes:
        output.append(
            (w.student.username, w.tags.all())
        )

    return render_to_response( "wishlist.html", {
            "title": "Wish register",
            "message": "Following wishes were captured in the database",
            "wishlist": output
        },
        context_instance = RequestContext( request )
    )

def flush_wishes( request ):
    Wish.objects.all().delete()

    return render_to_response( "dialog.html", {
            "title": "All wishes were deleted",
            "message": "All wishes were removed from the databased.",
        },
        context_instance = RequestContext( request )
    )