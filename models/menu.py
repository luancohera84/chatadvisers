# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------
from _clasFunt import DataGlobal
varGl       = DataGlobal()

response.menu  = []
textNoPicture  = ["id","estado","producto","telefono","empresa","cliente","segmento", "Nombre","name", "surname","id_asignacion","fecha_fin_asignacion","hora_creacion", "id_info_cliente_historica",]
tiposDatosHtml = ['date','text','number','tel','texarea','punto_pago']

if not configuration.get('app.production'):
    _app = request.application
    response.menu += []


def is_session():
    return True if auth.is_logged_in() else False

if is_session():
    idUser               = auth.user.id
    nameUser             = "%s %s" %(auth.user.first_name,auth.user.last_name)
    emailUser            = auth.user.email
    userType             = auth.user.tipo
    estado               = auth.user.registration_key
    empresaSesion        = auth.user.id_empresa
    proVClRt             = 'wss://'+str(varGl.urlRtIns)+':8282/realtime/'


def createUsers( nombre, apellidos, email, password, tipoUsuario, genero ):
    adv_dbUsuarios     = db.auth_user
    idUsuarioDeveloper = adv_dbUsuarios.insert(
        first_name     = nombre,
        last_name      = apellidos,
        email          = email,
        password       = db.auth_user.password.validate(password)[0],
        tipo           = tipoUsuario,
        genero         = genero,
    )
    return idUsuarioDeveloper



def changeStatusAdviser( idAdviser, estado ):
    adv_dbStaPlaf     = db.estados_plataforma
    adv_dbStAdv       = db.estado_asesor
    adv_dbStAdvHist   = db.estado_asesor_historica
    idEstadoAdv       = 0
    idEstadoPlaf      = db( adv_dbStaPlaf.estado_plataforma_nombre == estado ).select( adv_dbStaPlaf.id ).last()
    if idEstadoPlaf:
        db( adv_dbStAdv.estado_asesor_asesor == idAdviser ).delete()
        idEstadoAdv   = adv_dbStAdv.insert(
            estado_asesor_estado_plataforma     = idEstadoPlaf.id,
            estado_asesor_asesor                = idAdviser
        )
        adv_dbStAdvHist.insert(
            estado_asesor_estado_plataforma     = idEstadoPlaf.id,
            estado_asesor_asesor                = idAdviser
        )
        pass
    return idEstadoAdv


def statusActAdviser( idAdviser ):
    from _clasFunt import DataGlobal
    varGl        = DataGlobal()
    adv_dbStaPlaf     = db.estados_plataforma
    adv_dbStAdv       = db.estado_asesor
    statusAdviser     = 'Sin status' 
    statusColor       = 'text-secondary'
    idEstadoPlaf      = db( adv_dbStAdv.estado_asesor_asesor == idAdviser ).select( adv_dbStaPlaf.estado_plataforma_nombre, left = ( adv_dbStaPlaf.on( adv_dbStaPlaf.id == adv_dbStAdv.estado_asesor_estado_plataforma) ), groupby = adv_dbStAdv.estado_asesor_asesor ).last()
    if idEstadoPlaf:
        if idEstadoPlaf.estado_plataforma_nombre == varGl.estadoInicial:
            statusColor    = 'text-success'
        elif idEstadoPlaf.estado_plataforma_nombre == varGl.estadoFin:
            statusColor    = 'text-danger'
        else:
            statusColor    = 'text-primary'
            pass
        statusAdviser  = idEstadoPlaf.estado_plataforma_nombre
        pass
    return statusAdviser,statusColor


def tiposUsuarios():
    if userType[0] ==  'Gerente':
        tipoUsuarios     =  ['Asesor','Director']
    elif ( ( userType[0] ==  'Developer' ) | ( userType[0] ==  'Administrador' )):
        tipoUsuarios     = ['Developer','Administrador','Gerente','Asesor','Director']
    elif userType[0] ==  'Director':
        tipoUsuarios     =  ['Gerente','Asesor','Director']
    else:
        tipoUsuarios     =  []
        pass
    return tipoUsuarios



def tipoTipificaciones():
    tipTipificacion = db( db.tipo_interaccion.tipo_interaccion_estado == True ).select( db.tipo_interaccion.tipo_interaccion_id_resultado, db.tipo_interaccion.tipo_interaccion_descripcion )
    logsMostrar( 'info', 'tipoTipificaciones=> tipTipificacion '+str(tipTipificacion)+'' )
    return tipTipificacion


def statusAll():
    adv_dbStaPlaf  = db.estados_plataforma
    statusList     = db( adv_dbStaPlaf.estado_plataforma_estado == True ).select( adv_dbStaPlaf.estado_plataforma_nombre )
    return statusList


def diaSemana( diaNumb ):
    diaNumber = int(diaNumb)
    # logsMostrar('info', 'diaNumber: '+str(diaNumber)+' ' )
    if diaNumber == 1:
        diaSemanaReturn = 'Lunes'
    elif diaNumber == 2:
        diaSemanaReturn = 'Martes'
    elif diaNumber == 3:
        diaSemanaReturn = 'Miercoles'
    elif diaNumber == 4:
        diaSemanaReturn = 'Jueves'
    elif diaNumber == 5:
        diaSemanaReturn = 'Viernes'
    elif diaNumber == 6:
        diaSemanaReturn = 'Sabado'
    else:
        diaSemanaReturn = 'Domingo'
        pass
    return diaSemanaReturn


def mesCurso(mes):
    mesNumero = int(mes)
    if mesNumero == 1:
        mes = 'enero'
    elif mesNumero == 2:
        mes = 'febrero'
    elif mesNumero == 3:
        mes = 'marzo'
    elif mesNumero == 4:
        mes = 'abril'
    elif mesNumero == 5:
        mes = 'mayo'
    elif mesNumero == 6:
        mes = 'junio'
    elif mesNumero == 7:
        mes = 'julio'
    elif mesNumero == 8:
        mes = 'agosto'
    elif mesNumero == 9:
        mes = 'septiembre'
    elif mesNumero == 10:
        mes = 'octubre'
    elif mesNumero == 11:
        mes = 'noviembre'
    else:
        mes = 'diciembre'
        pass
    return str(mes).capitalize()

# ácóúñÑªáíóúñÑóƒ×á
def replaceAcentos( strs ):
    logsMostrar( 'info', 'replaceAcentos 165 => strs '+str(strs)+'')
    strSinAc   = str(strs).replace('á','a').replace('é','a').replace('í','i').replace('ó','o').replace('ú','u').replace('á','a').replace('ñ','n').replace('"\\n"','')
    logsMostrar( 'info', 'replaceAcentos 167 => strSinAc '+str(strSinAc)+'')
    return strSinAc