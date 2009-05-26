#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
    return render_to_response('dpressblog/index.html',
        context_instance = RequestContext(request))
