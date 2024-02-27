# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
import gluon.contrib.simplejson

@auth.requires_login()
def index():
    if userType[0] ==  'Gerente':
        redirect( URL('reportes','empresas') )
    elif userType[0] ==  'Director':
        redirect( URL('director','dashboard') )
    elif userType[0] ==  'Asesor':
        redirect( URL('asesor','dashboard') )
    else:
        response.title    = T("Dashboard")
        # import emoji

        # # Imprimir un emoji específico
        # print(emoji.emojize(":smiley:"))

        # # Concatenar emojis con texto
        # mensaje = "¡Hola " + emoji.emojize(":wave:") + "!"
        # print(mensaje)

        # # Buscar emojis por nombre o descripción
        # resultado = emoji.demojize("🐶")
        # print(resultado)  # Imprime ":perro:"

        # # Obtener una lista de todos los emojis disponibles
        # lista_emojis = emoji.emoji_lis()
        # for e in lista_emojis:
        #     print(e['emoji'])

        pass
    return locals()



@auth.requires_login()
def emojis():
    return locals()



def ingresoUsuario():
    from _clasFunt import DataGlobal
    varGl  = DataGlobal()
    logsMostrar( 'info', 'Ingreso a la funcion => ingresoUsuario' )
    vars_emailIngreso    = request.vars.emailIngreso
    # logsMostrar( 'info', f'Ingreso a la funcion => vars_emailIngreso {vars_emailIngreso}' )
    logsMostrar( 'info', vars_emailIngreso )
    vars_passIngreso     = request.vars.passIngreso
    # logsMostrar( 'info', f'Ingreso a la funcion => vars_passIngreso {vars_passIngreso}' )
    logsMostrar( 'info', vars_passIngreso )
    vars_users           = db.auth_user
    vars_consul          = db( vars_users.email==vars_emailIngreso ).count()
    # logsMostrar( 'info', f'Ingreso a la funcion => vars_consul {vars_consul}' )
    logsMostrar( 'info', vars_consul )
    vars_consulEsta      = db( ( vars_users.registration_key ) & ( vars_users.email==vars_emailIngreso ) ).count()
    # logsMostrar( 'info', f'Ingreso a la funcion => vars_consulEsta {vars_consulEsta}' )
    logsMostrar( 'info', vars_consulEsta )
    if vars_consul       == 0:
        vars_valores     = dict(vars_valores=varGl.errorUsuario)
    elif vars_consulEsta == 1:
        vars_valores     = dict(vars_valores=varGl.errorEstado)
    else:
        multi_Autentic    = auth.login_bare(vars_emailIngreso,vars_passIngreso)
        if multi_Autentic:
            vars_valores = str(session.auth.user.first_name)+' '+str(session.auth.user.last_name)
            img           = ''
            vars_valores = dict(vars_valores=vars_valores,img=img)
            logsMostrar( 'info', session.auth.user.tipo )
            if session.auth.user.tipo == ['Asesor']:
                logsMostrar( 'info', 'Soy usuarios Asesor' )
                tmpCambioEstado = changeStatusAdviser( session.auth.user.id, varGl.estadoInicial )
                logsMostrar( 'info', tmpCambioEstado )
                if tmpCambioEstado > 0:
                    print('Ingreso asesor', tmpCambioEstado)
                    logsMostrar( 'info', tmpCambioEstado )
                    # datosAsesor = datosEmpleado( session.auth.user.id )
                    # # print('datosAsesor colaborador', datosAsesor)
                    # sms = "rTime.noti_ingresoAsesor('"+str(datosAsesor)+"');" 
                    # setRtime(sms,'gerente_'+str(session.auth.user.empresa)+'_'+str(session.auth.user.cliente)+'_'+str(session.auth.user.sucursal))
                    pass
                pass
        else:
            vars_valores = dict(vars_valores=varGl.errorUsuInvalido)
            pass
        pass
    logsMostrar( 'info', 'vars_valores => '+str(vars_valores)+' ' )
    return gluon.contrib.simplejson.dumps(vars_valores)

def start():
    #resulInsert = createUsers( 'Developer', 'FullStack', 'lcortes@intelibpo.com', 'Ab1g3l2@12', 'Developer', 'Masculino' )
    #resulInsert = createUsers( 'Director', 'Operacion', 'directaor@intelibpo.com', 'D1r4ct3r2@22', 'Director', 'Femenino' )
    # apt-get install python3-xlrd
    # apt-get install python-xlrd
    # python3 -m pip install xlrd
    # pip install xlrd
    # import pandas as pd
    # import numpy as np
    # from sqlalchemy import create_engine
    # import xlrd, os
    # prefijosPais   = db.prefijos_pais

    # df_info        = pd.read_excel('/var/www/web2py/applications/init/static/phone_code.xlsx')
    # logsMostrar( 'info', 'actualizacionAsigIdenti df_info.head() => '+str(df_info.head())+'')

    # if len(df_info) > 0:
    #     prefijosPais.bulk_insert(df_info.to_dict(orient='records'))
    #     pass
    pass
# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
