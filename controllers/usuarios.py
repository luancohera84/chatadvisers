# -*- coding: utf-8 -*-


@auth.requires_login()
def listado():
    response.title     = T("Listado usuarios") 
    response.suBtitle  = T("Dashboard usuarios")
    adv_dbUsuarios     = db.auth_user
    listUsers          = []
    if userType[0] ==  'Gerente':
        listIsAsesors  = listUsersAsig()
        for item in listIsAsesors:
            tmpAser = db( ( adv_dbUsuarios.id == item ) & ( adv_dbUsuarios.tipo == 'Asesor' ) ).select( adv_dbUsuarios.ALL ).last()
            if tmpAser:
                listUsers.append(
                    dict(
                        id               = tmpAser.id,
                        first_name       = tmpAser.first_name,
                        last_name        = tmpAser.last_name,
                        tipo             = tmpAser.tipo,
                        registration_key = tmpAser.registration_key,
                        email            = tmpAser.email
                    )
                )
                pass
            pass
    elif ( ( userType[0] ==  'Developer' ) | ( userType[0] ==  'Administrador' )):
        listUsers      = db( adv_dbUsuarios.id > 0 ).select( adv_dbUsuarios.ALL )
    elif userType[0] ==  'Director':
        listUsers      = db( ( adv_dbUsuarios.tipo == 'Asesor' ) | ( adv_dbUsuarios.tipo == 'Gerente' ) ).select( adv_dbUsuarios.ALL )
    else:
        redirect(URL('error','pageNoPermitida'))
        pass
    logsMostrar( 'info', 'listado => listUsers '+str(listUsers)+'' )
    return locals()


@auth.requires_login()
def agrergarUsuario():
    varDatos       = request.vars
    resulInsert    = 0
    resulInsert    = createUsers( varDatos.nombreUusario, varDatos.apellidosUusario,varDatos.emailUsuario,varDatos.passwordUsuario,varDatos.tipoUsuario,varDatos.genero)
    return str(resulInsert)



def infoEmpresaUsuario():
    varDatos        = request.vars
    listadoEmpresas = infoEmpresaListAsigAs( varDatos.idUsers )
    return locals()



@auth.requires_login()
def getlistaEmpresas():
    varDatos        = request.vars
    infoCompany     = setListadoEmpresas()
    return locals()


@auth.requires_login()
def agregarUsuEmpresa():
    varDatos       = request.vars
    resulInsert    = 0
    if varDatos.idEmpresa:
        resulInsert    = setAsignarUsuEmpresa( varDatos.idEmpresa, varDatos.idUser, varDatos.tipo, varDatos.opc )
        pass
    return str(resulInsert)


@auth.requires_login()
def getlistaClientes():
    varDatos       = request.vars
    resulInsert    = 0
    infoCustomers  = setListadoClientesEmpresasUsu( varDatos.idEmpresa )
    return locals()


@auth.requires_login()
def asigSegmentoClienteUsuario():
    varDatos       = request.vars
    resulInsert    = 0
    logsMostrar( 'info', varDatos )
    resulInsert    = setAsigClientesSegmentoUsu( varDatos.idEmpresa, varDatos.idCliente, varDatos.idSegmento, varDatos.idUser, varDatos.parmOpc )
    return str(resulInsert)