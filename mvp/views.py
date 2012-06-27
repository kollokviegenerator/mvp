# Create your views here.
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render_to_response
from django.core.context_processors import csrf;
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect;
from mvp.models import Wish, Student, Tag

from controls import *

@csrf_protect
def main( request ):

    return render_to_response( "main.html", {
            "title": "Test",
        },
        context_instance = RequestContext( request )
    )

@csrf_protect
def display( request ):

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

    # generate tag objects

    for t in tags:
        candidate = Tag.objects.get_or_create(keyword=t)[0]
        wish.tags.add(candidate)
        wish.save()

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

    Tag.objects.all().delete()
    Student.objects.all().delete()
    Wish.objects.all().delete()

    return render_to_response( "main.html", {
            "title": "Flush entries"
        },
        context_instance = RequestContext( request )
    )