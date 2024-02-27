# -*- coding: utf-8 -*-

from usuariosAsignar import UsuariosAsig


def createUsersApi( idCompany,idCustomers,idSegment,nombreEmpresa  ):
    try:
        adv_dbUsuarios     = db.auth_user
        contadorUsers      = 0
        # emailCreateGer = 'gerente_'+str(nombreEmpresa).replace(' ','_').lower()+'@intelibpo.com'
        genero  = 'Femenino'
        for item in range(1,6):
            emailCreateGer     =  'gerente_'+str(item)+'_chatbot@intelibpo.com'
            if db( adv_dbUsuarios.email == emailCreateGer ).count() == 0:
                if item > 3:
                    genero = 'Masculino'
                    pass
                idUsuarioGer       =  adv_dbUsuarios.insert(
                    first_name     =  'Gerente '+str(item)+'',
                    last_name      =  'ChatBot',
                    email          =  emailCreateGer,
                    password       =  db.auth_user.password.validate('G3r3nT3'+str(request.now)[:4]+'')[0],
                    tipo           = 'Gerente',
                    genero         = genero,
                    id_empresa     = idCompany
                )
                contadorUsers     = 1
            else:
                contadorUsers     = 1
                pass
            pass

        
        asesorSeg            = UsuariosAsig( db )
        asesorSeg.idEmpresa  = idCompany
        asesorSeg.idCliente  = idCustomers
        asesorSeg.idSegmento = idSegment
        asesorSeg.define_table()
        genero  = 'Femenino'
        for item in range(1,6):
            # emailCreateAsesor     = 'asesor_'+str(item)+'_'+str(nombreEmpresa).replace(' ','_').lower()+'@intelibpo.com'
            emailCreateAsesor     = 'asesor_'+str(item)+'_chatbot@intelibpo.com'
            if db( adv_dbUsuarios.email == emailCreateAsesor ).count() == 0:

                if item > 3:
                    genero = 'Masculino'
                    pass
                idUsuarioAsesor    =  adv_dbUsuarios.insert(
                    first_name     =  'Asesor '+str(item)+'',
                    last_name      =  'ChatBot',
                    email          =  emailCreateAsesor,
                    password       =  db.auth_user.password.validate('A535or'+str(item)+''+str(request.now)[:4]+'')[0],
                    tipo           = 'Asesor',
                    genero         = genero,
                    id_empresa     = 0
                )
                contadorUsers        = contadorUsers + 1
            else:
                contadorUsers     = contadorUsers + 1
                pass
            pass
    except Exception as e:
        contadorUsers  = 0
        logsMostrar('error', 'Error en: getCreateCliente => '+str(e)+''  )
        pass
    return contadorUsers