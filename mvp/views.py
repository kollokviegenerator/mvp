# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.core.context_processors import csrf;
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect;
from mvp.models import Wish, Student, Tag

@csrf_protect
def main( request ):
    return render_to_response( "main.html", {
            "title": "Test",
        },
        context_instance = RequestContext( request )
    )

@csrf_protect
def display( request ):

    username = "ilyakh"

    tags = request.POST["tags"]
    tags = tags.split(",")

    # creates a wish object
    wish = Wish( username=username )
    wish.save()

    # add each tag to a ManyToMany field
    for t in tags:
        if not None:
            wish.tags.add( Tag(name=t) )

    wish.save()

    tags = Wish.objects.all()

    return render_to_response( "main.html", {
            "title": "Test",
            "tags": tags
        },
        context_instance = RequestContext( request )
    );