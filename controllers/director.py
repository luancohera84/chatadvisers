# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
import gluon.contrib.simplejson

@auth.requires_login()
def dashboard():
    response.title    = T("Dashboard")
    return locals()


