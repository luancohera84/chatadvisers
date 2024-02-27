# -*- coding: utf-8 -*-
from empresas import Empresas, Clientes, Segmentos
from clientesUsers import ClientesUsers
from conversaCliAdv import ConversClientAdv
from usuariosAsignar import UsuariosAsig
from _clasFunt import DataGlobal
import json
import datetime

def setAtencionHorario( empresa, cliente, segmento ):
    from datetime import datetime
    company              = Empresas( db )
    customers            = Clientes( db )
    segment              = Segmentos( db )
    vardData             = DataGlobal()
    company.define_table()
    customers.define_table()
    segment.define_table()
    idEmpresa            = empresaConsulting( empresa )
    idCliente            = clienteConsulting( cliente, idEmpresa )
    segment.idSegmento   = segmentoConsulting( segmento, idCliente )
    horarioHabil         = vardData.StatBoolT
    sms                  = ''
    segment.diaBuscarSem = diaSemana(datetime.today().isoweekday())
    segment.tipoSmsPr    = 'Horario'
    # logsMostrar('info', 'segment.diaBuscarSem: '+str(segment.diaBuscarSem)+' ' )
    listHorarios         =  segment.setHorariosSegId()
    if listHorarios:
        # logsMostrar('info', 'listHorarios: '+str(listHorarios)+' ' )
        if int(listHorarios.dia_laborable) == vardData.estadoIniNum:
            horarioHabil   = validateHoraAtencion(listHorarios.hora_inicio,listHorarios.hora_fin,listHorarios.dias_festivos)
        else:
            horarioHabil = vardData.StatBoolF
            pass
        listadoSmsSeg  = segment.setSmsPrebSegId()
        if listadoSmsSeg:
            sms  = listadoSmsSeg.sms
            pass
        pass
    return horarioHabil, sms

def consultingInfoSinSeg ( telefonoCliente, identificaCliente, companyCliente, customersCliente ):
    segmentoStrauss          = ''
    if empresaConsulting( companyCliente ) > 0:
        clienteInfoT                  = ClientesUsers( db )
        clienteInfoT.telfonoCliente   = telefonoCliente
        clienteInfoT.idetficCliente   = identificaCliente
        clienteInfoT.empresa_strauss  = companyCliente
        clienteInfoT.cliente_strauss  = customersCliente
        clienteInfoT.define_table()
        infoClienteInfo               = clienteInfoT.consultingClieApiSinSeg()
        if infoClienteInfo:
            segmentoStrauss            = infoClienteInfo.segmento_strauss
            pass
        pass
    return segmentoStrauss




def setClienteInConversaAsesor( companyCliente, customersCliente, segmentCliente, telefono, identificacion ):
    # logsMostrar( 'info', 'setClienteInConversaAsesor => companyCliente '+str(companyCliente)+'' )
    # logsMostrar( 'info', 'setClienteInConversaAsesor => customersCliente '+str(customersCliente)+'' )
    # logsMostrar( 'info', 'setClienteInConversaAsesor => segmentCliente '+str(segmentCliente)+'' )
    # logsMostrar( 'info', 'setClienteInConversaAsesor => telefono '+str(telefono)+'' )
    # logsMostrar( 'info', 'setClienteInConversaAsesor => identificacion '+str(identificacion)+'' )
    vardData               = DataGlobal()
    coversaOnLine          = vardData.estadoFalsNum
    idClientePlf,idClientePlfHist  = consultingInfoClTrue ( telefono, identificacion, companyCliente, customersCliente, segmentCliente, False )
    # logsMostrar( 'info', 'setClienteInConversaAsesor API => idClientePlf 58 '+str(idClientePlf)+'' )
    # logsMostrar( 'info', 'setClienteInConversaAsesor API => idClientePlfHist 59 '+str(idClientePlfHist)+'' )
    if idClientePlf > vardData.estadoFalsNum:
        convCliAs              = ConversClientAdv( db )
        convCliAs.idCliPlaf    = idClientePlf
        convCliAs.define_table()
        aseCliente,idAdviser   = convCliAs.getClienteInConversaAsesor()
        # logsMostrar( 'info', 'setClienteInConversaAsesor API => aseCliente 65 '+str(aseCliente)+'' )
        # logsMostrar( 'info', 'setClienteInConversaAsesor API => idAdviser 66 '+str(idAdviser)+'' )
        if idAdviser > 0:
            statusAdviser,statusColor = statusActAdviser( idAdviser )
            # logsMostrar( 'info', 'setClienteInConversaAsesor API => statusAdviser 71 '+str(statusAdviser)+'' )
            if statusAdviser == vardData.estadoBack:
                coversaOnLine = aseCliente
                pass
            pass
        pass
    # logsMostrar( 'info', 'setClienteInConversaAsesor => coversaOnLine '+str(coversaOnLine)+'' )
    return coversaOnLine




def advisersOnLine( companyCliente, customersCliente, segmentCliente ):
    # logsMostrar( 'info', 'advisersOnLine => companyCliente '+str(companyCliente)+'' )
    # logsMostrar( 'info', 'advisersOnLine => customersCliente '+str(customersCliente)+'' )
    # logsMostrar( 'info', 'advisersOnLine => segmentCliente '+str(segmentCliente)+'' )
    usuAsing                  = UsuariosAsig( db )
    usuAsing.idEmpresa        = empresaConsulting( companyCliente )
    usuAsing.idCliente        = clienteConsulting( customersCliente, usuAsing.idEmpresa )
    usuAsing.idSegmento       = segmentoConsulting( segmentCliente, usuAsing.idCliente )
    usuAsing.define_table()
    cantAdviserOnLine         = usuAsing.listAsesorOneline()
    # logsMostrar( 'info', 'advisersOnLine => cantAdviserOnLine '+str(cantAdviserOnLine)+'' )
    return cantAdviserOnLine

def setInfoAtencionCliente( idCliente ):
    convCliAs            = ConversClientAdv( db )
    convCliAs.idCliPlaf  = idCliente
    convCliAs.define_table()
    idClAtencion         = 0
    dataClientAten       = convCliAs.consultingAtencionAsesorCliente()
    if dataClientAten:
        idClAtencion     = dataClientAten.id
        pass
    return idClAtencion

def setCantidadClienteSms( idClientePlf ):
    convCliAs               = ConversClientAdv( db )
    convCliAs.idCliPlaf     = idClientePlf
    dataClienteSms          = 0
    tiempoEspera            = 0 
    convCliAs.define_table()
    dataClienteSTmp         = convCliAs.countSmsSinLectura()
    if dataClienteSTmp:
        dataClienteSms      = len(dataClienteSTmp)
        for item in dataClienteSTmp:
            tiempoEspera    = str(fechaFormato(item.hora_creacion,'hora'))
            pass
        pass
    return dataClienteSms,tiempoEspera

def consultingClAdvCov ( telefonoCliente, identificaCliente, companyCliente, customersCliente, segmentCliente, idClientePlf, idClientePlfHist ):
    clienteUsers                  = ConversClientAdv( db )
    clienteUsers.telfonoCliente   = telefonoCliente
    clienteUsers.telfonoCliente   = identificaCliente
    clienteUsers.idEmpresa        = empresaConsulting( companyCliente )
    clienteUsers.idCliente        = clienteConsulting( customersCliente, clienteUsers.idEmpresa  )
    clienteUsers.idSegmento       = segmentoConsulting( segmentCliente, clienteUsers.idCliente  )
    clienteUsers.idCliPlaf        = idClientePlf
    clienteUsers.idCliPlafHist    = idClientePlfHist
    idAsigCli                     = 0
    idAsigCliHist                 = 0
    asesorAsig                    = 0
    # logsMostrar( 'info', 'consultingClAdvCov => idClientePlf  144 '+str(idClientePlf)+'' )
    if idClientePlf > 0:
        clienteUsers.define_table()
        infoIdCliAsig             = clienteUsers.consultingAsigClinUser()
        # logsMostrar( 'info', 'consultingClAdvCov => infoIdCliAsig  147 '+str(infoIdCliAsig)+'' )
        infoIdCliAsigHist         = clienteUsers.consultingAsigClinUserHist()
        if infoIdCliAsig:
            idAsigCli             = infoIdCliAsig.id
            idAsigCliHist         = infoIdCliAsigHist.id
            usuAsing              = UsuariosAsig( db )
            usuAsing.idEmpresa    = clienteUsers.idEmpresa
            usuAsing.idCliente    = clienteUsers.idCliente
            usuAsing.idSegmento   = clienteUsers.idSegmento
            usuAsing.define_table()
            asesorDipon          = usuAsing.listAsesorDisponible()
            # logsMostrar( 'info', 'consultingClAdvCov => asesorDipon 108 '+str(asesorDipon)+'' )
            if asesorDipon > 0:
                clienteUsers.idAdvisers   = asesorDipon
                idAsigCli,idAsigCliHist   = clienteUsers.getCreateClienteAdvisers()
                asesorAsig                = clienteUsers.idAdvisers #infoUsuarioId( clienteUsers.idAdvisers )
                # smsRt = """
                #     rTime.newAsignacionClienteAsesor("""+str(clienteUsers.idCliPlaf)+""","""+str(clienteUsers.idAdvisers)+""");
                # """
                # enviarSmsRT( clienteUsers.idAdvisers, smsRt )
                pass
        else:
            # Buscar asesores disponibles
            usuAsing              = UsuariosAsig( db )
            usuAsing.idEmpresa    = clienteUsers.idEmpresa
            usuAsing.idCliente    = clienteUsers.idCliente
            usuAsing.idSegmento   = clienteUsers.idSegmento
            usuAsing.define_table()
            asesorDipon          = usuAsing.listAsesorDisponible()
            # logsMostrar( 'info', 'consultingClAdvCov => asesorDipon cliente new 108 '+str(asesorDipon)+'' )
            if asesorDipon > 0:
                clienteUsers.idAdvisers   = asesorDipon
                idAsigCli,idAsigCliHist   = clienteUsers.getCreateClienteAdvisers()
                # logsMostrar( 'info', 'consultingClAdvCov => idAsigCli cliente new 112 '+str(idAsigCli)+'' )
                # logsMostrar( 'info', 'consultingClAdvCov => idAsigCliHist cliente new 113 '+str(idAsigCliHist)+'' )
                asesorAsig                = asesorDipon #infoUsuarioId( asesorDipon )
                # logsMostrar( 'info', 'consultingClAdvCov => asesorAsig cliente new 115 '+str(asesorAsig)+'' )
                smsRt = """
                    rTime.newAsignacionClienteAsesor("""+str(clienteUsers.idCliPlaf)+""","""+str(asesorDipon)+""");
                """
                # logsMostrar( 'info', 'consultingClAdvCov => smsRt cliente new 119 '+str(smsRt)+'' )
                enviarSmsRT( asesorDipon, smsRt )
                pass
            
            pass
        pass
    return asesorAsig,idAsigCli,idAsigCliHist


def consultingInfoClTrue ( telefonoCliente, identificaCliente, companyCliente, customersCliente, segmentCliente, data ):
    idClientePlf                      = 0
    idClientePlfHist                  = 0
    if empresaConsulting( companyCliente ) > 0:
        clienteInfoT                  = ClientesUsers( db )
        clienteInfoT.telfonoCliente   = telefonoCliente
        clienteInfoT.idetficCliente   = identificaCliente
        clienteInfoT.idEmpresa        = empresaConsulting( companyCliente )
        clienteInfoT.idCliente        = clienteConsulting( customersCliente, clienteInfoT.idEmpresa )
        clienteInfoT.idSegmento       = segmentoConsulting( segmentCliente, clienteInfoT.idCliente )
        clienteInfoT.empresa_strauss  = companyCliente
        clienteInfoT.cliente_strauss  = customersCliente
        clienteInfoT.segmento_strauss = segmentCliente
        # logsMostrar( 'info', 'consultingInfoClTrue => clienteInfoT.telfonoCliente '+str(clienteInfoT.telfonoCliente)+'' )
        # logsMostrar( 'info', 'consultingInfoClTrue => clienteInfoT.idetficCliente '+str(clienteInfoT.idetficCliente)+'' )
        # logsMostrar( 'info', 'consultingInfoClTrue => clienteInfoT.empresa_strauss '+str(clienteInfoT.empresa_strauss)+'' )
        # logsMostrar( 'info', 'consultingInfoClTrue => clienteInfoT.cliente_strauss '+str(clienteInfoT.cliente_strauss)+'' )
        # logsMostrar( 'info', 'consultingInfoClTrue => clienteInfoT.segmento_strauss '+str(clienteInfoT.segmento_strauss)+'' )
        # logsMostrar( 'info', 'consultingInfoClTrue => clienteInfoT.idEmpresa '+str(clienteInfoT.idEmpresa)+'' )
        # logsMostrar( 'info', 'consultingInfoClTrue => clienteInfoT.idCliente '+str(clienteInfoT.idCliente)+'' )
        # logsMostrar( 'info', 'consultingInfoClTrue => clienteInfoT.idSegmento '+str(clienteInfoT.idSegmento)+'' )
        clienteInfoT.define_table()
        infoClienteInfo               = clienteInfoT.consultingClieTrueIdentEmClSeg()
        # logsMostrar( 'info', 'consultingInfoClTrue => infoClienteInfo '+str(infoClienteInfo)+'' )
        infoClienteInHist             = clienteInfoT.consultingClieTrueIdentEmClSegHist()
        # logsMostrar( 'info', 'consultingInfoClTrue => infoClienteInHist '+str(infoClienteInHist)+'' )
        if not infoClienteInfo:
            # Data que llega del chatBot
            if data:
                clienteInfoT.dataCliente  = data
                idClientePlf,idClientePlfHist = clienteInfoT.getCreateInfoCliente()
                pass
        else:
            idClientePlf               = infoClienteInfo.id
            idClientePlfHist           = infoClienteInHist.id
            pass
        pass
    return idClientePlf,idClientePlfHist



def recepcionSms( telefonoCliente, identificaCliente, companyCliente, customersCliente, segmentCliente, sms, origen, destino, tipo, asesorLleg,infoIdCliAsigLleg,infoIdCliAsigHistLleg ):
    # logsMostrar('info','sms 237 => '+str((sms))+'')
    # logsMostrar('info','sms 237 => '+str(sms.encode('utf-8'))+'')
    # logsMostrar('info','sms 238 => '+str(sms.decode('utf-8'))+'')
    idConversacion                = 0
    clienteUsers                  = ConversClientAdv( db )
    clienteInfoT                  = ClientesUsers( db )
    clienteUsers.telfonoCliente   = telefonoCliente
    clienteUsers.idetficCliente   = identificaCliente
    clienteUsers.idEmpresa        = empresaConsulting( companyCliente )
    clienteUsers.idCliente        = clienteConsulting( customersCliente, clienteUsers.idEmpresa  )
    clienteUsers.idSegmento       = segmentoConsulting( segmentCliente, clienteUsers.idCliente  )
    clienteUsers.sms              = sms
    clienteUsers.tipo             = tipo
    clienteUsers.origen           = origen
    clienteUsers.destino          = destino
    if asesorLleg > 0:
        asesor                     = asesorLleg
        infoIdCliAsig              = infoIdCliAsigLleg
        infoIdCliAsigHist          = infoIdCliAsigHistLleg
        clienteUsers.idCliPlaf     = db.asesor_cliente[infoIdCliAsigLleg].id_cliente
        clienteUsers.idCliPlafHist = db.asesor_cliente_historica[infoIdCliAsigHistLleg].id_cliente
        if clienteUsers.idCliPlaf > 0:
            clienteUsers.define_table()
            clienteUsers.idAdvisers             = asesor
            idInsertCov,idInsertCovHist         = clienteUsers.consultinIdConvClinUser()
            if idInsertCov:
                clienteUsers.idInsertCov        = idInsertCov.id
                clienteUsers.idInsertCovHist    = idInsertCovHist.id
            else:
                idInsertCov,idInsertCovHist     = clienteUsers.getNewconversacion()
                clienteUsers.idInsertCov        = idInsertCov
                clienteUsers.idInsertCovHist    = idInsertCovHist
                pass
            idConversacionRet                   = clienteUsers.getNewSms()
            
            if idConversacionRet > 0:
                idConversacion = idConversacionRet
                clienteInfoT.define_table()
                cantSms, tiempoSms = setCantidadClienteSms( clienteUsers.idCliPlaf )
                smsRt = """
                    rTime.newSmsAsesor("""+str(setInfoAtencionCliente(clienteUsers.idCliPlaf))+""","""+str(clienteUsers.idCliPlaf)+""","""+str(clienteUsers.idAdvisers)+""",'"""+str(sms)+"""',"""+str(clienteUsers.idEmpresa)+""",'"""+str(tipo)+"""','"""+str(db.info_cliente[clienteUsers.idCliPlaf].Nombre)+"""',"""+str(cantSms)+""",'"""+str(tiempoSms)+"""');
                """
                enviarSmsRT( clienteUsers.idAdvisers, smsRt )
                pass
            pass
        return idConversacion
    else:
        # Sin asesor asignado
        infoClienteInfo ,infoClienteInHist = consultingInfoClTrue( telefonoCliente, identificaCliente, companyCliente, customersCliente, segmentCliente, [] )
        # logsMostrar('info','infoClienteInfo 288 => '+str(infoClienteInfo)+'')
        # logsMostrar('info','infoClienteInHist 289 => '+str(infoClienteInHist)+'')
        if infoClienteInfo:
            clienteUsers.idCliPlaf              = infoClienteInfo
            clienteUsers.idCliPlafHist          = infoClienteInHist
            if clienteUsers.idCliPlaf > 0:
                clienteUsers.define_table()
                # Consultar si el cliente tiene una conversacion con un asesor
                idInsertCov,idInsertCovHist      = clienteUsers.consultinIdConvCli()
                # logsMostrar('info','idInsertCov 297 => '+str(idInsertCov)+'')
                # logsMostrar('info','idInsertCovHist 298 => '+str(idInsertCovHist)+'')
                if idInsertCov:
                    clienteUsers.idInsertCov        = idInsertCov.id
                    clienteUsers.idAdvisers         = idInsertCov.id_asesor
                    clienteUsers.idInsertCovHist    = idInsertCovHist.id
                    idConversacionRet               = clienteUsers.getNewSms()
                    if idConversacionRet > 0:
                        idConversacion = idConversacionRet
                        clienteInfoT.define_table()
                        cantSms, tiempoSms = setCantidadClienteSms( clienteUsers.idCliPlaf )
                        smsRt = """
                            rTime.newSmsAsesor("""+str(setInfoAtencionCliente(clienteUsers.idCliPlaf))+""","""+str(clienteUsers.idCliPlaf)+""","""+str(clienteUsers.idAdvisers)+""",'"""+str(sms)+"""',"""+str(clienteUsers.idEmpresa)+""",'"""+str(tipo)+"""','"""+str(db.info_cliente[clienteUsers.idCliPlaf].Nombre)+"""',"""+str(cantSms)+""",'"""+str(tiempoSms)+"""');
                        """
                        enviarSmsRT( clienteUsers.idAdvisers, smsRt )
                        pass
                else:
                    asesor,infoIdCliAsig,infoIdCliAsigHist = consultingClAdvCov( telefonoCliente, identificaCliente, companyCliente, customersCliente, segmentCliente, clienteUsers.idCliPlaf, clienteUsers.idCliPlafHist )
                
                    if infoIdCliAsigHist:
                        idAsigCli         = infoIdCliAsig
                        idAsigCliHist     = infoIdCliAsigHist
                        # Construir una conversacion cliente & asesor
                        
                        # logsMostrar('info','recepcionSmsAPI idAsigCli 187 => '+str(idAsigCli)+'')
                        #idAsesorTmp                         = db( ( db.asesor_cliente.id_cliente == idAsigCli )  ).select( db.asesor_cliente.id_asesor ).last()
                        #logsMostrar('info','recepcionSmsAPI idAsesorTmp 188 => '+str(idAsesorTmp)+'')
                        clienteUsers.idAdvisers             = asesor #idAsesorTmp.id_asesor
                        idInsertCov,idInsertCovHist         = clienteUsers.consultinIdConvClinUser()
                        # logsMostrar('info','recepcionSmsAPI idInsertCov 191 => '+str(idInsertCov)+'')
                        # logsMostrar('info','recepcionSmsAPI idInsertCovHist 192 => '+str(idInsertCovHist)+'')
                        if idInsertCov:
                            clienteUsers.idInsertCov        = idInsertCov.id
                            clienteUsers.idInsertCovHist    = idInsertCovHist.id
                            # logsMostrar('info','recepcionSmsAPI clienteUsers.idInsertCov 1 186 => '+str(clienteUsers.idInsertCov)+'')
                            # logsMostrar('info','recepcionSmsAPI clienteUsers.idInsertCovHist 1 197 => '+str(clienteUsers.idInsertCovHist)+'')
                        else:
                            idInsertCov,idInsertCovHist     = clienteUsers.getNewconversacion()
                            clienteUsers.idInsertCov        = idInsertCov
                            clienteUsers.idInsertCovHist    = idInsertCovHist
                            # logsMostrar('info','recepcionSmsAPI idInsertCov 0 202 => '+str(idInsertCov)+'')
                            # logsMostrar('info','recepcionSmsAPI idInsertCovHist 0 203 => '+str(idInsertCovHist)+'')
                            pass
                        idConversacionRet                   = clienteUsers.getNewSms()
                        # logsMostrar('info','recepcionSmsAPI idConversacionRet 206 => '+str(idConversacionRet)+'')
                        if idConversacionRet > 0:
                            idConversacion = idConversacionRet
                            clienteInfoT.define_table()
                            cantSms, tiempoSms = setCantidadClienteSms( clienteUsers.idCliPlaf )
                            smsRt = """
                                rTime.newSmsAsesor("""+str(setInfoAtencionCliente(clienteUsers.idCliPlaf))+""","""+str(clienteUsers.idCliPlaf)+""","""+str(clienteUsers.idAdvisers)+""",'"""+str(sms)+"""',"""+str(clienteUsers.idEmpresa)+""",'"""+str(tipo)+"""','"""+str(db.info_cliente[clienteUsers.idCliPlaf].Nombre)+"""',"""+str(cantSms)+""",'"""+str(tiempoSms)+"""');
                            """
                            # logsMostrar('info','recepcionSmsAPI smsRt 214 => '+str(smsRt)+'')
                            enviarSmsRT( clienteUsers.idAdvisers, smsRt )
                            pass
                        pass
                    pass
                pass
            pass
        return idConversacion
        pass