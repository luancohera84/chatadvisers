# -*- coding: utf-8 -*-

@auth.requires_login()
def pageNoPermitida():
    response.title    = T("Pagina no permitida")
    return locals()