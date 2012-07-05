from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from mvp.models import Wish, Student, Tag

from util import *

def match( request ):

    wishes = Wish.objects.all()
    pool = Pool( wishes )
    result = sorted(
        [ (x.mountford_similarity(), x.wish_A, x.wish_B)
        for x in pool.pair()], key=lambda a: a[0]
    )

    return render_to_response( "dialog.html", {
            "title": "Test",
            "message": pool,
            "set": result
        },
        context_instance = RequestContext( request )
    )