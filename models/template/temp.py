# -*- coding: utf-8 -*-

#  Cambio estado empresa
def setUpEstadoCompany( idCompany, status ):
    from empresas import Empresas, Clientes, Segmentos
    from usuariosAsignar import UsuariosAsig
    idCompanyUp             = 0
    company                 = Empresas( db )
    customers               = Clientes( db )
    segment                 = Segmentos( db )
    asesorSeg               = UsuariosAsig( db )
    company.idEmpresa       = idCompany
    customers.idEmpresa     = idCompany
    segment.idEmpresa       = idCompany
    asesorSeg.idEmpresa     = idCompany
    company.estadoEmpresa   = int(status)
    customers.estadoCliente = int(status)
    segment.estadoSegmento  = int(status)
    company.define_table()
    customers.define_table()
    segment.define_table()
    idCompanyUp             = company.setCambioEstado()
    if idCompanyUp > 0:
        if int(status) == 1:
            customers.setCambioEstadoClientesEmpresa()
            segment.setCambioEstadoSegEmpresa()
            asesorSeg.define_table()
            idAseAsig            = asesorSeg.getEliminarEmpresaAs()
            pass
        pass
    return idCompanyUp

# Cambio de nombre empresa
def setUpNombreCompany( idCompany, nomEmpresa  ):
    from empresas import Empresas
    idCompanyUp           = False
    company               = Empresas( db )
    company.idEmpresa     = idCompany
    company.nomEmpresa    = nomEmpresa
    company.define_table()
    idCompanyUp            = company.setCambioNombre()
    return idCompanyUp

# Cambio estado cliente
def setUpEstadoCustomer( idCustomers, status ):
    from empresas import Empresas, Clientes, Segmentos
    idCustomerUp              = 0
    company                   = Empresas( db )
    customers                 = Clientes( db )
    segment                   = Segmentos( db )
    customers.idCliente       = idCustomers
    customers.estadoCliente   = int(status)
    segment.idCliente         = idCustomers
    segment.estadoSegmento    = int(status)
    company.define_table()
    customers.define_table()
    segment.define_table()
    idCustomerUp            = customers.setCambioEstadoClientes()
    if idCustomerUp > 0:
        segment.setCambioEstadoSegCliente()
        pass
    return idCustomerUp


# Cambio nombre cliente
def setUpNombreCustomer( idCustomers, nomCliente  ):
    from empresas import Empresas,Clientes
    company                   = Empresas( db )
    customers                 = Clientes( db )
    customers.idCliente       = idCustomers
    customers.nomCliente      = nomCliente
    company.define_table()
    customers.define_table()
    idCustomerUp            = customers.setCambioNombreClientes()
    return idCustomerUp


#  Cambio estado segmento
def setUpEstadoSegment( idSegment, status ):
    from empresas import Empresas, Clientes, Segmentos
    company                   = Empresas( db )
    customers                 = Clientes( db )
    segment                   = Segmentos( db )
    segment.idSegmnento     = idSegment
    segment.estadoSegmento    = int(status)
    company.define_table()
    customers.define_table()
    segment.define_table()
    idSegmentUp            = segment.setCambioEstadoSegmentos()
    return idSegmentUp


# Cambio nombre segmento
def setUpNombreSegment( idSegment, nomSegmento  ):
    from empresas import Empresas, Clientes, Segmentos
    company                   = Empresas( db )
    customers                 = Clientes( db )
    segment                   = Segmentos( db )
    segment.idSegmnento       = idSegment
    segment.nomSegmento       = nomSegmento
    company.define_table()
    customers.define_table()
    segment.define_table()
    idSegmentUp              = segment.setCambioNombreSegmentos()
    return idSegmentUp



#  Cambio estado usuarios
def setUpEstadoUsers( idUsers, status ):
    adv_dbUsuarios     = db.auth_user
    if int(status) == 1:
        estadoNew  =  status
    else:
        estadoNew  = ''
        pass
    idUserstUp = db( adv_dbUsuarios.id == idUsers ).update( registration_key = estadoNew )
    return idUserstUp


# Cambio email - password usuario
def setUpNombreUsers( idUsers, emailUsers, passwordUsers  ):
    adv_dbUsuarios     = db.auth_user
    if emailUsers:
        if db( adv_dbUsuarios.email == emailUsers ).count() == 0:
            idUserstUp    = db( adv_dbUsuarios.id == idUsers ).update( email = emailUsers )
            if passwordUsers:
                idUserstUp    = db( adv_dbUsuarios.id == idUsers ).update( password = db.auth_user.password.validate(passwordUsers)[0] )
                pass
        else:
            idUserstUp = 0
            pass
    else:
        if passwordUsers:
            idUserstUp    = db( adv_dbUsuarios.id == idUsers ).update( password = db.auth_user.password.validate(passwordUsers)[0] )
            pass
        pass
    return idUserstUp


#  Cambio estado horario
def setUpEstadoHorario( idHorario, status ):
    from empresas import Empresas, Clientes, Segmentos
    company                   = Empresas( db )
    customers                 = Clientes( db )
    segment                   = Segmentos( db )
    segment.idHorario         = idHorario
    segment.estadoHorario     = int(status)
    company.define_table()
    customers.define_table()
    segment.define_table()
    idHorarioUp            = segment.setCambioEstadoHorario()
    return idHorarioUp



#  Cambio estado SmsPrest
def setUpEstadoSmsPrest( idSmsPret, status ):
    from empresas import Empresas, Clientes, Segmentos
    company                   = Empresas( db )
    customers                 = Clientes( db )
    segment                   = Segmentos( db )
    segment.idSmsPret         = idSmsPret
    segment.estadoSmsPret     = int(status)
    company.define_table()
    customers.define_table()
    segment.define_table()
    idSmsPrestUp             = segment.setCambioEstadoSmsPrest()
    return idSmsPrestUp




def setChatServicio( idClienPlaf ):
    from clientesUsers import ClientesUsers
    cliInfo            = ClientesUsers( db )
    cliInfo.idCliPlaf  = idClienPlaf
    infoChatCliente    = []
    cliInfo.define_table()
    infoClienteSendSms  = cliInfo.consultingClieTrueId()
    if infoClienteSendSms:
        infoChatCliente.append(
            dict(
                empresa   = str(infoClienteSendSms.empresa_strauss).capitalize(),
                idUser    = idUser,
                idEmpresa = infoClienteSendSms.empresa
            )
        )
        pass
    return infoChatCliente

# def setChatServicio( idClienPlaf ):
#     from clientesUsers import ClientesUsers
#     from conversaCliAdv import ConversClientAdv
#     cliInfo                    = ClientesUsers( db )
#     clienteUsers               = ConversClientAdv( db )
#     clienteUsers.idAdvisers    = idUser
#     clienteUsers.idCliPlaf     = idClienPlaf
#     clienteUsers.idCliPlafHist = idClienPlaf
#     idAsigCli,idAsigCliHist    = clienteUsers.getCreateClienteAdvisers()
#     idClAdvisersAtencion       = clienteUsers.getCreateClienteAdvisersAtencion()
#     infoChatCliente    = []
#     cliInfo.define_table()
#     infoClienteSendSms  =  db( db.info_cliente.id == idClienPlaf ).select( db.info_cliente.ALL ).last()
#     if infoClienteSendSms:
#         infoChatCliente.append(
#             dict(
#                 empresa   = str(infoClienteSendSms.empresa_strauss).capitalize(),
#                 idUser    = idUser,
#                 idEmpresa = infoClienteSendSms.empresa
#             )
#         )
#         pass
#     return infoChatCliente