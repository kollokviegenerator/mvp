# Create your views here.
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
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

    # fetch tags
    tags = request.POST["tags"]
    tags = tags.split(",")

    # create student
    user = User.objects.get( username="ilyakh" )

    student = Student(
        user=user
    )
    student.save()

    # create wish
    wish = Wish( student=student )
    wish.save()

    for t in tags:
        tag = Tag( name=t )
        tag.save()
        wish.tags.add( tag )
        wish.save()

    tags = [(w.student, w.tags.all()) for w in Wish.objects.all()]

    return render_to_response( "main.html", {
            "title": "Test",
            "tags": tags
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