from itertools import groupby
from gluon import *
from _clasFunt import InfoLogs, DataGlobal
from conversaCliAdv import ConversClientAdv
from clientesUsers import ClientesUsers
from interaccionesAsesor import InteraccionesAsesor


class Reportes:

    def __init__( self, db ):

        self.db                          = db
        self.idCliPlaf                   = 0
        self.idCliPlafHist               = 0
        self.idAdvisers                  = 0
        self.idInsertCov                 = 0
        self.idInsertCovHist             = 0
        self.id_resultado                = 0
        self.idEmpresa                   = 0
        self.descripcion_resultado       = ''
        self.nomEmpresa                  = ''


    def setCountClientAsigEmpresa( self ):
        varGl                  = DataGlobal()
        countInfoClientes      = varGl.estadoFalsNum
        try:
            db                 = self.db
            infoConver         = ConversClientAdv( db )
            infoCliet          = ClientesUsers( db )
            infoConver.define_table()
            infoCliet.define_table()
            dbConvHist         = db.conversaciones
            dbClietn           = db.info_cliente
            countInfoCliTmp   = db( dbClietn.empresa == self.idEmpresa ).select(dbConvHist.id,left=( dbClietn.on( dbClietn.id == dbConvHist.id_cliente ) ))
            if countInfoCliTmp:
                countInfoClientes = len(countInfoCliTmp)
                pass
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: setCountClientAsigEmpresa => '+str(e)+'' )
            logs.logFile()
            pass
        return countInfoClientes

    def setCountSmsAsigEmpresa( self ):
        varGl             = DataGlobal()
        countInfoCola     = varGl.estadoFalsNum
        try:
            db                 = self.db
            infoConver         = ConversClientAdv( db )
            infoCliet          = ClientesUsers( db )
            infoConver.define_table()
            infoCliet.define_table()
            dbConvHist         = db.conversaciones
            dbMsmHist          = db.mensajes_conversacion
            dbClietn           = db.info_cliente
            countInfoColaTmp   = db( ( dbClietn.empresa == self.idEmpresa ) & ( dbMsmHist.origen_mensaje == varGl.msmOriCliente ) ).select(dbMsmHist.id,left=( dbConvHist.on( dbConvHist.id == dbMsmHist.id_conversacion ), dbClietn.on( dbClietn.id == dbConvHist.id_cliente ) ))
            if countInfoColaTmp:
                countInfoCola = len(countInfoColaTmp)
                pass
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: setCountColaAsigEmpresa => '+str(e)+'' )
            logs.logFile()
            pass
        return countInfoCola
    
    def setCountGestionesAsigEmpresa( self ):
        varGl                  = DataGlobal()
        countInfoGestiones     = varGl.estadoFalsNum
        try:
            db                 = self.db
            infoIntera         = InteraccionesAsesor( db )
            infoIntera.define_table()
            dbIntAs            = db.interacciones_asesor
            countInfoGestiones = db( dbIntAs.id_empresa == self.idEmpresa ).count()
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: setCountGestionesAsigEmpresa => '+str(e)+'' )
            logs.logFile()
            pass
        return countInfoGestiones

    def setCountColaAsigEmpresa( self ):
        varGl             = DataGlobal()
        countInfoCola     = varGl.estadoFalsNum
        try:
            db                 = self.db
            infoConver         = ConversClientAdv( db )
            infoCliet          = ClientesUsers( db )
            infoConver.define_table()
            infoCliet.define_table()
            dbConvHist         = db.conversaciones
            dbMsmHist          = db.mensajes_conversacion
            dbClietn           = db.info_cliente
            countInfoColaTmp   = db( ( dbClietn.empresa == self.idEmpresa ) & ( dbMsmHist.origen_mensaje == varGl.msmOriCliente ) & ( dbMsmHist.estado_lectura == varGl.msmLectura ) ).select(dbMsmHist.id,left=( dbConvHist.on( dbConvHist.id == dbMsmHist.id_conversacion ), dbClietn.on( dbClietn.id == dbConvHist.id_cliente ) ))
            if countInfoColaTmp:
                countInfoCola = len(countInfoColaTmp)
                pass
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: setCountColaAsigEmpresa => '+str(e)+'' )
            logs.logFile()
            pass
        return countInfoCola
       

    def setGestionesAsigEmpresa( self ):
        dataInfoGestiones = []
        try:
            db            = self.db
            varGl         = DataGlobal()
            infoIntera    = InteraccionesAsesor( db )
            infoIntera.define_table()
            dbIntAs       = db.interacciones_asesor
            infoTmp       = db( dbIntAs.id_empresa == self.idEmpresa ).select( dbIntAs.ALL )
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: setGestionesAsigEmpresa => '+str(e)+'' )
            logs.logFile()
            pass
        return dataInfoGestiones

    def setAcuerdosDePago( self ):
        try:
            db            = self.db
            varGl         = DataGlobal()
            infoIntera    = InteraccionesAsesor( db )
            infoIntera.define_table()
            dbIntAs       = db.interacciones_asesor
            dataInfoAcuerdoPago  = db( ( dbIntAs.id_empresa == self.idEmpresa ) & ( dbIntAs.descripcion_resultado in varGl.acuerdoPago ) ).count()
        except Exception as e:
            dataInfoAcuerdoPago = 0
            logs = InfoLogs( 'error', 'Error en: setAcuerdosDePago => '+str(e)+'' )
            logs.logFile()
            pass
        return dataInfoAcuerdoPago


    def setPromedioAtencion( self ):
        try:
            db            = self.db
            sqlPromedio = """
                SELECT AVG(TIME_TO_SEC(TIMEDIFF(hor_fin,hor_ini)))/60 as prom from
                (
                select c.id, min(mc.hora_creacion) as hor_ini, ia.hora_interaccion as hor_fin
                from chatbot_asesor.conversaciones c 
                inner join chatbot_asesor.mensajes_conversacion mc 
                    on c.id = mc.id_conversacion
                inner join chatbot_asesor.interacciones_asesor ia
                    on c.id = ia.id_conversacion 
                where ia.id_empresa = """+str(self.idEmpresa)+"""
                group by c.id
                )a
            """
            # print('sqlPromedio', sqlPromedio)
            res           = db.executesql(sqlPromedio)
            if res:
                for item in res:
                    promedio   = int(item[0])
                    pass
                pass
        except Exception as e:
            promedio = 0
            logs = InfoLogs( 'error', 'Error en: setPromedioAtencion => '+str(e)+'' )
            logs.logFile()
            pass
        return promedio


    def setAtencionAsesor( self ):
        dataAtencionAsesores = []
        try:
            db            = self.db
            varGl         = DataGlobal()
            infoIntera    = InteraccionesAsesor( db )
            infoIntera.define_table()
            dbIntAs       = db.interacciones_asesor
            dbAses        = db.auth_user
            inteTmp       = db( dbIntAs.id_empresa == self.idEmpresa ).select( dbIntAs.id_asesor, groupby = dbIntAs.id_asesor  )
            if inteTmp:
                for items in inteTmp:
                    infoConver         = ConversClientAdv( db )
                    countInfoCola      = varGl.estadoFalsNum
                    fHOldGes           = ''
                    infoConver.define_table()
                    dbConvHist         = db.conversaciones
                    dbMsmHist          = db.mensajes_conversacion
                    
                    countInfoColaTmp   = db( ( dbConvHist.id_asesor == items.id_asesor ) & ( dbMsmHist.origen_mensaje == varGl.msmOriCliente ) & ( dbMsmHist.estado_lectura == varGl.msmLectura ) ).select(dbMsmHist.id,left=( dbConvHist.on( dbConvHist.id == dbMsmHist.id_conversacion ) ))
                    print('countInfoColaTmp', countInfoColaTmp)
                    if countInfoColaTmp:
                        countInfoCola = len(countInfoColaTmp)
                        pass

                    print('countInfoCola', countInfoCola)

                    fHOldGesTmp      = db( ( dbConvHist.id_asesor == items.id_asesor ) & ( dbMsmHist.origen_mensaje == varGl.msmOriasesor )  ).select(dbMsmHist.fecha_creacion,dbMsmHist.hora_creacion,left=( dbConvHist.on( dbConvHist.id == dbMsmHist.id_conversacion ) )).last()
                    print('fHOldGesTmp', fHOldGesTmp)
                    if fHOldGesTmp:
                        horaSms     = str(self.fechaFormato(fHOldGesTmp.hora_creacion,'hora'))
                        fechaSms    = str(self.fechaFormato(fHOldGesTmp.fecha_creacion,'fecha'))
                        fHOldGes    = fechaSms+' '+str(horaSms)
                        pass
                    
                    print('fHOldGes', fHOldGes)
                    dataAtencionAsesores.append(
                        dict(
                            asesor   = db.auth_user[items.id_asesor].first_name+' '+str(db.auth_user[items.id_asesor].last_name),
                            cerrados = db( dbIntAs.id_asesor == items.id_asesor ).count(),
                            acuerdos = db( ( dbIntAs.id_asesor == items.id_asesor ) & ( dbIntAs.descripcion_resultado in varGl.acuerdoPago ) ).count(),
                            inCola   = countInfoCola,
                            fHOldGes = fHOldGes 
                        )
                    )
                    pass
                pass
            print('dataAtencionAsesores', dataAtencionAsesores)
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: setAtencionAsesor => '+str(e)+'' )
            logs.logFile()
            pass
        return dataAtencionAsesores


    def gestionesAsignacion( self ):
        infoGestiones = []
        varGl     = DataGlobal()
        try:
            db = self.db
            sqlGestion = """
                SELECT
                    empresa,
                    cliente,
                    segmento,
                    nombre_cliente,
                    identificacion_cliente,
                    telefono_cliente,
                    descripcion_resultado,
                    fecha_interaccion,
                    hora_interaccion,
                    id_conversacion,
                    id_info_cliente,
                    id_empresa
                FROM
                    interacciones_asesor ia
                WHERE 
                    ia.id_empresa  = """+str(self.idEmpresa)+"""
                ORDER BY
                    ia.id
            """
            infoGestionesTmp    = db.executesql(sqlGestion)
            if infoGestionesTmp:
                for items in infoGestionesTmp:
                    infoGestiones.append(
                        dict(
                            empresa                = items[0],
                            cliente                = items[1],
                            segmento               = items[2],
                            nombre_cliente         = items[3],
                            identificacion_cliente = items[4],
                            telefono_cliente       = items[5],
                            descripcion_resultado  = items[6],
                            fecha_interaccion      = str(self.fechaFormato(items[7],'fecha')),
                            hora_interaccion       = str(self.fechaFormato(items[8],'hora')),
                            id_conversacion        = items[9],
                            id_info_cliente        = items[10],
                            id_empresa             = items[11]
                        )
                    )
                    pass
                pass
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: gestionesAsesor => '+str(e)+'' )
            logs.logFile()
            pass
        return infoGestiones


    def gestionesAsignacionFechas( self ):
        infoGestionesFechas = []
        varGl     = DataGlobal()
        try:
            db = self.db
            mesAntes = int(varGl.mesGlb) - int(varGl.estadoIniNum)
            sqlGestion = """
                SELECT
                    empresa,
                    cliente,
                    segmento,
                    nombre_cliente,
                    identificacion_cliente,
                    telefono_cliente,
                    descripcion_resultado,
                    fecha_interaccion,
                    hora_interaccion,
                    id_conversacion_historica,
                    id_info_cliente,
                    id_empresa
                FROM
                    interacciones_asesor_historica ia
                WHERE 
                    ia.id_empresa  = """+str(self.idEmpresa)+"""
                AND
                    ia.anio_creacion >= """+str(varGl.anioGlb)+"""
                AND
                    ia.mes_creacion <= """+str(mesAntes)+"""
                ORDER BY
                    ia.id
            """
            # print('sqlGestion', sqlGestion)
            infoGestionesTmp    = db.executesql(sqlGestion)
            if infoGestionesTmp:
                for items in infoGestionesTmp:
                    infoGestionesFechas.append(
                        dict(
                            empresa                = items[0],
                            cliente                = items[1],
                            segmento               = items[2],
                            nombre_cliente         = items[3],
                            identificacion_cliente = items[4],
                            telefono_cliente       = items[5],
                            descripcion_resultado  = items[6],
                            fecha_interaccion      = str(self.fechaFormato(items[7],'fecha')),
                            hora_interaccion       = str(self.fechaFormato(items[8],'hora')),
                            id_conversacion        = items[9],
                            id_info_cliente        = items[10],
                            id_empresa             = items[11]
                        )
                    )
                    pass
                pass
            # print('infoGestionesFechas', infoGestionesFechas)
        except Exception as e:
            logs = InfoLogs( 'error', 'Error en: gestionesAsesorFechas => '+str(e)+'' )
            logs.logFile()
            pass
        return infoGestionesFechas


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



