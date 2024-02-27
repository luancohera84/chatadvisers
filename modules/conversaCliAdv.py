# -*- coding: utf-8 -*-

from turtle import left
from gluon import *
from _clasFunt import InfoLogs, DataGlobal,ConexionStrauss
from clientesUsers import ClientesUsers
from empresas import Empresas


class ConversClientAdv:

    def __init__( self, db ):

        self.db                     = db
        self.sms                    = ''
        self.tipo                   = ''
        self.origen                 = ''
        self.destino                = ''
        self.telfonoCliente         = ''
        self.idetficCliente         = ''
        self.descripcion_resultado  = ''
        self.tipoSms                = ''
        self.extension              = ''
        self.idCliPlaf              = 0
        self.idCliPlafHist          = 0
        self.idAdvisers             = 0
        self.idEmpresa              = 0
        self.idCliente              = 0
        self.idSegmento             = 0
        self.idInsertCov            = 0
        self.idInsertCovHist        = 0
        self.id_resultado           = 0
        self.idIdentiMultimadia     = 0
        self.idCliPlafs             = []

    
    def define_table( self ):
        try:
            cliOfertas = ClientesUsers( self.db )
            cliOfertas.define_table()
            varGl     = DataGlobal()
            db = self.db

            db.define_table('asesor_cliente',
                Field('id_cliente','reference info_cliente'),
                Field('id_asesor','reference auth_user'),
                Field('estado_asesor_cliente',default=True),
                Field('fecha_creacion',default = varGl.fechaIntModels),
                Field('hora_creacion',default  = varGl.horaIntModels)
            )

            db.define_table('asesor_cliente_historica',
                Field('id_cliente','reference info_cliente_historica'),
                Field('id_asesor','reference auth_user'),
                Field('estado_asesor_cliente',default=True),
                Field('fecha_creacion',default = varGl.fechaIntModels),
                Field('hora_creacion',default  = varGl.horaIntModels)
            )

            db.define_table('asesor_atencion_cliente',
                Field('id_cliente','reference info_cliente'),
                Field('id_cliente_histori','reference info_cliente_historica'),
                Field('id_asesor','reference auth_user'),
                Field('fecha_creacion',default = varGl.fechaIntModels),
                Field('hora_creacion',default  = varGl.horaIntModels)
            )

            db.define_table('conversaciones',
                Field('id_cliente','reference info_cliente'),
                Field('id_asesor','reference auth_user'),
                Field('id_conversacion_historica','integer'),
                Field('estado_conversacion',default=True),
                Field('fecha_creacion',default = varGl.fechaIntModels),
                Field('hora_creacion',default  = varGl.horaIntModels)
            )
            db.define_table('conversaciones_historica',
                Field('id_cliente','reference info_cliente_historica'),
                Field('id_asesor','reference auth_user'),
                Field('estado_conversacion',default=True),
                Field('anio_creacion',default = varGl.anioGlb),
                Field('mes_creacion',default = varGl.mesGlb),
                Field('dia_creacion',default = varGl.dayGlb),
                Field('fecha_creacion',default = varGl.fechaIntModels),
                Field('hora_creacion',default  = varGl.horaIntModels)
            )

            db.define_table('mensajes_conversacion',
                Field('id_conversacion','reference conversaciones'),
                Field('origen_mensaje','string'),
                Field('destino_mensaje','string'),
                Field('mensage', 'text', requires=IS_NOT_EMPTY()),
                Field('tipo_mensaje'),
                Field('id_mensaje_conversacion_historica','integer'),
                Field('estado_lectura',default=varGl.msmLectura),
                Field('orden_llegada','integer', default=varGl.estadoIniNum),
                Field('fecha_creacion',default = varGl.fechaIntModels),
                Field('hora_creacion',default  = varGl.horaIntModels)
            )
            db.define_table('mensajes_conversacion_historica',
                Field('id_conversacion','reference conversaciones_historica'),
                Field('origen_mensaje','string'),
                Field('destino_mensaje','string'),
                Field('mensage', 'text', requires=IS_NOT_EMPTY()),
                Field('tipo_mensaje'),
                Field('estado_lectura',default=varGl.msmLectura),
                Field('orden_llegada','integer', default=varGl.estadoIniNum),
                Field('fecha_creacion',default = varGl.fechaIntModels),
                Field('hora_creacion',default  = varGl.horaIntModels)
            )

            db.define_table('identificador_multimedia',
                Field('id_conversacion'),
                Field('id_cliente'),
                Field('id_asesor'),
                Field('tipo'),
                Field('multimedia'),
                Field('fecha_creacion',default = varGl.fechaIntModels),
                Field('hora_creacion',default  = varGl.horaIntModels)
            )
            return True
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: define_table asesor_cliente asesor_cliente_historica interacciones_asesor interacciones_asesor_historica => '+str(e)+'' )
            #logs.logFile()
            return False
            pass


    def getClienteInConversaAsesor( self ):
        try:
            varGl                = DataGlobal()
            resulCoversaOnLine   = varGl.estadoFalsNum
            adviserResul         = varGl.estadoFalsNum
            db                   = self.db
            adv_dbStaPlaf        = db.asesor_cliente
            resulCovTmp          = db( ( adv_dbStaPlaf.id_cliente == self.idCliPlaf ) & ( adv_dbStaPlaf.estado_asesor_cliente == True ) ).select( adv_dbStaPlaf.id,adv_dbStaPlaf.id_asesor ).last()
            if resulCovTmp:
                resulCoversaOnLine = resulCovTmp.id
                adviserResul       = resulCovTmp.id_asesor
                pass
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: getClienteInConversaAsesor => '+str(e)+'' )
            logs.logFile()
            pass
        return resulCoversaOnLine,adviserResul

   
    def getCreateClienteAdvisers( self ):
        idClAdvisers  = 0
        idClAdvisersHist = 0
        try:
            db = self.db
            cantAsClit       = db( ( db.asesor_cliente.id_cliente == self.idCliPlaf ) & ( db.asesor_cliente.id_asesor == self.idAdvisers ) & ( db.asesor_cliente.estado_asesor_cliente == True ) ).count()
            if cantAsClit == 0:
                idClAdvisers = db.asesor_cliente.insert(
                    id_cliente      = self.idCliPlaf,
                    id_asesor       = self.idAdvisers
                )
                idClAdvisersHist = db.asesor_cliente_historica.insert(
                    id_cliente      = self.idCliPlafHist,
                    id_asesor       = self.idAdvisers
                )
            else:
                idClAdvisersTmp        = db( ( db.asesor_cliente.id_cliente == self.idCliPlaf ) & ( db.asesor_cliente.id_asesor == self.idAdvisers ) & ( db.asesor_cliente.estado_asesor_cliente == True ) ).select( db.asesor_cliente.id ).last()
                if idClAdvisersTmp:
                    idClAdvisers           = idClAdvisersTmp.id
                    pass

                idClAdvisersHistTmp    = db( ( db.asesor_cliente_historica.id_cliente == self.idCliPlafHist ) & ( db.asesor_cliente_historica.id_asesor == self.idAdvisers ) & ( db.asesor_cliente_historica.estado_asesor_cliente == True ) ).select( db.asesor_cliente_historica.id ).last()
                if idClAdvisersHistTmp:
                    idClAdvisersHist       = idClAdvisersHistTmp.id
                    pass
                pass
        except Exception as e:  
            logs = InfoLogs( 'error', 'Error en: getCreateClienteAdvisers => '+str(e)+'' )
            logs.logFile()
            pass
        return idClAdvisers,idClAdvisersHist
    
    
    def getCreateClienteAdvisersAtencion( self ):
        try:
            db = self.db
            if db( db.asesor_atencion_cliente.id_asesor == self.idAdvisers ).count() > 0:
                db( db.asesor_atencion_cliente.id_asesor == self.idAdvisers ).delete()
                pass

            idClAdvisersAtencion = db.asesor_atencion_cliente.insert(
                id_cliente         = self.idCliPlaf,
                id_cliente_histori = self.idCliPlafHist,
                id_asesor          = self.idAdvisers
            )
        except Exception as e:
            idClAdvisersAtencion  = 0
            logs = InfoLogs( 'error', 'Error en: getCreateClienteAdvisersAtencion => '+str(e)+'' )
            logs.logFile()
            pass
        return idClAdvisersAtencion

    def getNewSms( self ):
        idInsertConSms = 0
        try:
            db     = self.db
            varGl  = DataGlobal()
            if self.origen == varGl.msmOriasesor:
                db( ( db.mensajes_conversacion.id_conversacion == self.idInsertCov ) & ( db.mensajes_conversacion.estado_lectura == varGl.msmLectura ) ).update( estado_lectura = varGl.msmLeido )
                db( ( db.mensajes_conversacion_historica.id_conversacion == self.idInsertCovHist ) & ( db.mensajes_conversacion_historica.estado_lectura == varGl.msmLectura ) ).update( estado_lectura = varGl.msmLeido )
                pass
            
            self.tipoSms    = self.tipo

            # print('self.sms', self.sms)
            
            if self.tipo == 'audio':
                self.idIdentiMultimadia = db.identificador_multimedia.insert(
                    id_conversacion = self.idInsertCovHist,
                    id_cliente      = self.idCliPlafHist,
                    id_asesor       = self.idAdvisers,
                    tipo            = self.tipo,
                    multimedia      = self.sms
                )
                self.extension  = 'mp3'
                multiMediFile = self.nombreMultimedia()
                rutaTmp  = varGl.rutaDescarga+str(self.tipo)+'/'+str(multiMediFile)
                smsFinal = multiMediFile
                varGl.urlDescarga = "wget -O "+str(rutaTmp)+" "+str(self.sms)+""
                varGl.descargarMultimedia()
            elif self.tipo == 'image':
                self.idIdentiMultimadia = db.identificador_multimedia.insert(
                    id_conversacion = self.idInsertCovHist,
                    id_cliente      = self.idCliPlafHist,
                    id_asesor       = self.idAdvisers,
                    tipo            = self.tipo,
                    multimedia      = self.sms
                )
                self.extension  = 'png'
                multiMediFile = self.nombreMultimedia()
                rutaTmp  = varGl.rutaDescarga+str(self.tipo)+'/'+str(multiMediFile)
                smsFinal = multiMediFile
                varGl.urlDescarga = "wget -O "+str(rutaTmp)+" "+str(self.sms)+""
                varGl.descargarMultimedia()
            else:
                smsFinal = self.sms
                pass
            
            idInsertConSmsHist =  db.mensajes_conversacion_historica.insert(
                id_conversacion    = self.idInsertCovHist,
                origen_mensaje     = self.origen,
                destino_mensaje    = self.destino,
                mensage            = smsFinal,
                tipo_mensaje       = self.tipo,
            ) 
            idInsertConSms                        = db.mensajes_conversacion.insert(
                id_conversacion                   = self.idInsertCov,
                origen_mensaje                    = self.origen,
                destino_mensaje                   = self.destino,
                mensage                           = smsFinal,
                tipo_mensaje                      = self.tipo,
                id_mensaje_conversacion_historica = idInsertConSmsHist
            )
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: getNewSms => '+str(e)+'' )
            logs.logFile()
            pass
        return idInsertConSms

    def getNewconversacion( self ):
        idInsertCov     = 0
        idInsertCovHist = 0
        try:
            db = self.db
            idInsertCovHist = db.conversaciones_historica.insert(
                id_cliente = self.idCliPlafHist,
                id_asesor  = self.idAdvisers
            )
            idInsertCov                   = db.conversaciones.insert(
                id_cliente                = self.idCliPlaf,
                id_asesor                 = self.idAdvisers,
                id_conversacion_historica = idInsertCovHist
            )
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: getNewconversacion => '+str(e)+'' )
            logs.logFile()
            pass
        return idInsertCov,idInsertCovHist


    def consultinIdConvCli( self ):
        idConver     = 0
        idConverHist = 0
        try:
            db = self.db
            # print('self.idCliPlaf consultinIdConvClinUser', self.idCliPlaf)
            # print('self.idCliPlafHist consultinIdConvClinUser', self.idCliPlafHist)
            idConver  = db( ( db.conversaciones.id_cliente == self.idCliPlaf )  & ( db.conversaciones.estado_conversacion == True ) ).select( db.conversaciones.id, db.conversaciones.id_asesor ).last()
            idConverHist  = db( ( db.conversaciones_historica.id_cliente == self.idCliPlafHist )  & ( db.conversaciones_historica.estado_conversacion == True ) ).select( db.conversaciones_historica.id ).last()
            # print('self.idConverHist consultinIdConvClinUser', idConverHist)
            return idConver,idConverHist
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: consultinIdConvClinUser => '+str(e)+'' )
            logs.logFile()
            return idConver,idConverHist
            pass

    def consultinIdConvClinUser( self ):
        idConver     = 0
        idConverHist = 0
        try:
            db = self.db
            # print('self.idCliPlaf consultinIdConvClinUser', self.idCliPlaf)
            # print('self.idAdvisers consultinIdConvClinUser', self.idAdvisers)
            # print('self.idCliPlafHist consultinIdConvClinUser', self.idCliPlafHist)
            idConver  = db( ( db.conversaciones.id_cliente == self.idCliPlaf ) & ( db.conversaciones.id_asesor == self.idAdvisers ) & ( db.conversaciones.estado_conversacion == True ) ).select( db.conversaciones.id ).last()
            # print('self.idConver consultinIdConvClinUser', idConver)
            idConverHist  = db( ( db.conversaciones_historica.id_cliente == self.idCliPlafHist ) & ( db.conversaciones_historica.id_asesor == self.idAdvisers ) & ( db.conversaciones_historica.estado_conversacion == True ) ).select( db.conversaciones_historica.id ).last()
            # print('self.idConverHist consultinIdConvClinUser', idConverHist)
            return idConver,idConverHist
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: consultinIdConvClinUser => '+str(e)+'' )
            logs.logFile()
            return idConver,idConverHist
            pass

    def consultingAsigClinUser( self ):
        db = self.db
        idClientAsig  = db( (db.asesor_cliente.id_cliente == self.idCliPlaf ) & ( db.asesor_cliente.estado_asesor_cliente == True )  ).select( db.asesor_cliente.ALL ).last()
        return idClientAsig

    def consultingAtencionClinAsesor( self ):
        db = self.db
        infoClientAtencion  = db( db.asesor_atencion_cliente.id_asesor == self.idAdvisers  ).select( db.asesor_atencion_cliente.id_cliente,db.asesor_atencion_cliente.id_cliente_histori ).last()
        # infoClientAtencion    = None
        return infoClientAtencion


    def consultingAtencionAsesorCliente( self ):
        db = self.db
        infoClientAtencion  = db( db.asesor_atencion_cliente.id_cliente == self.idCliPlaf  ).select( db.asesor_atencion_cliente.ALL ).last()
        return infoClientAtencion

    
    def infoClienteSmsAsesor( self ):
        db = self.db
        infoClientSms   = db( ( db.conversaciones.id_asesor == self.idAdvisers ) & ( db.conversaciones.id_cliente == self.idCliPlaf ) & ( db.conversaciones.estado_conversacion == True ) ).select( db.mensajes_conversacion.ALL, db.conversaciones.id_cliente,db.conversaciones.id_asesor,left = ( db.conversaciones.on ( db.conversaciones.id == db.mensajes_conversacion.id_conversacion ) ), orderby = db.mensajes_conversacion.id )
        return infoClientSms


    def infoClienteSmsIdCov( self ):
        db = self.db
        infoClientSms   = db( db.conversaciones.id == self.idInsertCov  ).select( db.mensajes_conversacion.ALL, db.conversaciones.id_cliente,db.conversaciones.id_asesor,left = ( db.conversaciones.on ( db.conversaciones.id == db.mensajes_conversacion.id_conversacion ) ), orderby = db.mensajes_conversacion.id )
        return infoClientSms


    def infoClienteSmsIdCovHist( self ):
        db = self.db
        infoClientSms   = db( db.conversaciones_historica.id == self.idInsertCovHist  ).select( db.mensajes_conversacion_historica.ALL, db.conversaciones_historica.id_cliente,db.conversaciones_historica.id_asesor,left = ( db.conversaciones_historica.on ( db.conversaciones_historica.id == db.mensajes_conversacion_historica.id_conversacion ) ), orderby = db.mensajes_conversacion_historica.id )
        return infoClientSms


    def infoClienteSmsHistory( self ):
        dataClienteSmsHistory   = []
        varGl     = DataGlobal()
        try:
            db = self.db
            sqlHistory = """
                SELECT
                    mch.id,
                    mch.origen_mensaje,
                    mch.mensage,
                    mch.estado_lectura,
                    mch.id_conversacion,
                    mch.hora_creacion,
                    mch.fecha_creacion,
                    mch.tipo_mensaje,
                    CONCAT(au.first_name,' ',au.last_name) as asesor,
                    CONCAT(ich.name,' ',ich.surname) as cliente,
                    ich.Nombre  
                FROM
                    mensajes_conversacion_historica mch
                INNER JOIN 
                    conversaciones_historica ch 
                ON
                    ch.id = mch.id_conversacion
                INNER JOIN 
                    info_cliente_historica ich 
                ON
                    ich.id = ch.id_cliente 
                INNER JOIN 
                    auth_user au 
                ON
                    au.id = ch.id_asesor 
                WHERE 
                    ch.id_cliente  in """+str(self.idCliPlafs)+"""
            """
            # print('sqlHistory', sqlHistory)
            dataClienteSTmp    = db.executesql(sqlHistory)
            if dataClienteSTmp:
                for item in dataClienteSTmp:
                    nameClienteTmp = str(item[9]).capitalize()
                    if nameClienteTmp != " ":
                        nameCliente = nameClienteTmp
                    else:
                        nameCliente = str(item[10]).capitalize()
                        pass
                    dataClienteSmsHistory.append(
                        dict(
                            idSms       = item[0],
                            tipoUsuario = item[1],
                            sms         = item[2],
                            estLect     = item[3],
                            idConv      = item[4],
                            horaSms     = str(self.fechaFormato(item[5],'hora')),
                            fechaSms    = str(self.fechaFormato(item[6],'fecha')),
                            textFecSms  = str(self.textFechaDia(item[6])),
                            tipoSms     = item[7],
                            cliente     = nameCliente,
                            asesor      = str(item[8]).capitalize()
                        )
                    )
                    pass
                pass
            return dataClienteSmsHistory
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: infoClienteSmsHistory => '+str(e)+'' )
            logs.logFile()
            pass

    def fechaFormato(self, valor, opc):
        formato  = ''
        try:
            hora  = '00'
            minu  = '00'
            segun = '00'
            if opc == 'fecha':
                anio = str(valor)[:4]
                mes  = str(valor)[4:-2]
                dia  = str(valor)[6:]
                formato = anio+'-'+str(mes)+'-'+str(dia)
            else:
                if len(str(valor)) == 5:
                    hora  = str(valor)[:1]
                    minu  = str(valor)[1:3]
                    segun = str(valor)[3:]
                elif len(str(valor)) == 6:
                    hora  = str(valor)[:2]
                    minu  = str(valor)[2:4]
                    segun = str(valor)[4:]
                    pass
                if hora == '24':
                    hora = hora.replace('24','00')
                    pass
                formato = hora+':'+str(minu)+':'+str(segun)
                pass
            return formato
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: fechaFormato => '+str(e)+'' )
            logs.logFile()
            pass
        
    def textFechaDia( self, fechaSms ):
        textFecha = ''
        try:
            from _clasFunt import DataGlobal
            varGl        = DataGlobal()
            fechaActual  = varGl.fechaIntModels
            operacion    = int(fechaActual) - int(fechaSms)
            if operacion ==  varGl.estadoFalsNum:
                textFecha   = 'Hoy'
            elif operacion ==  varGl.estadoIniNum:
                textFecha   = 'Ayer'
            else:
                if str(fechaActual)[-2:] == '01':
                    textFecha   = 'Ayer'
                else:
                    textFecha   = str(self.fechaFormato(fechaSms,'fecha'))
                    pass
                pass
            return textFecha
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: textFechaDia => '+str(e)+'' )
            logs.logFile()
            pass

    def countSmsSinLectura( self ):
        db     = self.db
        varGl  = DataGlobal()
        infoClientSms   = db( ( db.mensajes_conversacion.estado_lectura == varGl.msmLectura ) & ( db.mensajes_conversacion.destino_mensaje == varGl.msmOriasesor ) & ( db.conversaciones.id_cliente == self.idCliPlaf ) & ( db.conversaciones.estado_conversacion == True ) ).select( db.mensajes_conversacion.ALL, left = ( db.conversaciones.on ( db.conversaciones.id == db.mensajes_conversacion.id_conversacion ) ), orderby = db.mensajes_conversacion.id )
        return infoClientSms

    def consultingAsigClinUserHist( self ):
        db = self.db
        idClientAsigHist  = db( db.asesor_cliente_historica.id_cliente == self.idCliPlafHist  ).select( db.asesor_cliente_historica.ALL ).last()
        return idClientAsigHist


    def deleteAsigClinUser( self ):
        db = self.db
        idClientAsig  = db( db.asesor_cliente.id_cliente == self.idCliPlaf  ).delete()
        return idClientAsig


    def empresasClietAsesor( self ):
        db = self.db
        clientes = ClientesUsers( db )
        clientes.define_table
        listaEmpresasAsesorAsiCl = []
        # print('self.idAdvisers', self.idAdvisers)
        listaEmpresasAsesorAsiClTmp  = db( ( db.asesor_cliente.id_asesor == self.idAdvisers ) & ( db.asesor_cliente.estado_asesor_cliente == True ) ).select( db.info_cliente.empresa, left = ( db.info_cliente.on( db.info_cliente.id == db.asesor_cliente.id_cliente ) ), groupby = db.info_cliente.empresa )
        # print('listaEmpresasAsesorAsiClTmp', listaEmpresasAsesorAsiClTmp)
        if listaEmpresasAsesorAsiClTmp:
            company    = Empresas( db )
            company.define_table()
            for item in listaEmpresasAsesorAsiClTmp:
                company.idEmpresa = item.empresa
                empresaTpm        = company.getListarIdEmpresa()
                if empresaTpm:
                    listaEmpresasAsesorAsiCl.append(
                        dict(
                            idEmpresa     = empresaTpm.id,
                            nombreEmpresa = empresaTpm.nombre_empresa,
                            colorFondo    = empresaTpm.empresas_color 
                        )
                    )
                    pass
                pass
            pass
        return listaEmpresasAsesorAsiCl


    def clientesAsigEmpresaAsesor( self ):
        db         = self.db
        clientes   = ClientesUsers( db )
        company    = Empresas( db )
        company.define_table()
        clientes.define_table()
        listaClientesAsiEmprAsesor     = db( ( db.asesor_cliente.id_asesor == self.idAdvisers ) & ( db.asesor_cliente.estado_asesor_cliente == True ) & ( db.info_cliente.empresa == self.idEmpresa ) ).select( db.info_cliente.id,db.info_cliente.Nombre, db.info_cliente.telefono,db.info_cliente.surname,db.info_cliente.name,db.info_cliente.id_info_cliente_historica, left = ( db.info_cliente.on( db.info_cliente.id == db.asesor_cliente.id_cliente ) ), groupby = ( db.info_cliente.identificacion, db.info_cliente.telefono,  db.info_cliente.segmento ) )
        return listaClientesAsiEmprAsesor

    def nombreMultimedia( self ):
        db              = self.db
        nameMultimeda   = ''
        idCliTmp            = db( db.conversaciones.id == self.idInsertCov ).select( db.conversaciones.id_cliente ).last()
        if idCliTmp:
            self.idCliPlaf  = idCliTmp.id_cliente
            infoClienteData = self.infoClienteConversa()
            if infoClienteData:
                nameMultimeda = self.tipoSms+'_'+str(infoClienteData.identificacion)+'_'+str(infoClienteData.telefono)+'_'+str(infoClienteData.empresa)+'_'+str(infoClienteData.cliente)+'_'+str(infoClienteData.cliente)+'_'+str(infoClienteData.segmento)+'_'+str(self.idIdentiMultimadia)+'.'+str(self.extension)
                pass
            pass
        return nameMultimeda

    def infoClienteConversa( self ):
        db                 = self.db
        clientes           = ClientesUsers( db )
        clientes.define_table()
        infoClienteData    = db( ( db.info_cliente.id == self.idCliPlaf ) & ( db.info_cliente.estado == True ) ).select( db.info_cliente.empresa,db.info_cliente.cliente, db.info_cliente.telefono,db.info_cliente.identificacion,db.info_cliente.segmento ).last()
        return infoClienteData


    def infoSmsConversaciones( self ):
        listSmsConversaciones = []
        try:
            db = self.db
            infoSmsConvers   = db( db.mensajes_conversacion.id_conversacion == self.idInsertCov  ).select( db.mensajes_conversacion.ALL, orderby = db.mensajes_conversacion.id )
            if infoSmsConvers:
                for item in infoSmsConvers:
                    listSmsConversaciones.append(
                        dict(
                            origen_mensaje   = item.origen_mensaje,
                            destino_mensaje  = item.destino_mensaje,
                            mensage          = item.mensage,
                            tipo_mensaje     = item.tipo_mensaje,
                            fecha_creacion   = item.fecha_creacion,
                            hora_creacion    = item.hora_creacion
                        )
                    )
                    pass
                pass
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: infoSmsConversaciones => '+str(e)+'' )
            logs.logFile()
            pass
        return listSmsConversaciones