# -*- coding: utf-8 -*-
from gluon.contrib.websocket_messaging import websocket_send
import logging
from datetime import  datetime, date, timedelta, time 
import time, requests
import random
import urllib.request
from sqlalchemy import create_engine
from cryptography.fernet import Fernet
import rsa
import json
import subprocess
from urllib.parse import urlencode
# import holidays

logger = logging.getLogger(" App_chatBot_Asesor ")
logger.setLevel(logging.DEBUG)

#  Available levels: DEBUG INFO WARNING ERROR CRITICAL
class DataGlobal:

    def __init__( self ):
        self.urlRt              = 'https://chatadvisers.intelibpo.com'
        self.urlRtIns           = 'chatadvisers.intelibpo.com'
        self.urlApiWh           = 'https://api.gupshup.io/sm/api/v1/msg'
        self.portRt             = '8282'
        self.acuerdoPago        = ['Acuerdo de pago']
        self.keyRt              = 'chatBotAsesores'
        self.errorUsuario       = "usuario"
        self.errorEstado        = "estado"
        self.StatBoolT          = True
        self.StatBoolF          = False
        self.estadoNoIniNum     = -1
        self.estadoIniNum       = 1
        self.estadoFalsNum      = 0
        self.estadoInicial      = "En-linea"
        self.estadoFin          = "Fuera-linea"
        self.estadoBack         = "Backoffice"
        self.errorUsuInvalido   = "invalido"
        self.plantillaNoF       = "templateNof.html"
        self.userBDChatbot      = 'root'
        self.dbDBChatbot        = 'chatbot'
        self.hostDBChatbot      = 'localhost'
        self.keyPrivate         = 'j7t05fLcn0'
        self.urlSubInteli       = '.intelibpo.com'
        self.portIntelibpo      = '54678'
        self.userIntelibpo      = 'gcp'
        self.keyIntelibpo       = '???Soporte*2017***'
        self.baseDatIntelibpo   = 'avi_reportes_'
        self.userBaseInte       = 'root'
        self.keyBaseIntelibpo   = 'j7t05fLcn0'
        self.portBaseIntelibpo  = '3360'
        self.tipoUsuAsesor      = 'Asesor'
        self.msmOriCliente      = 'cliente'
        self.msmOriasesor       = 'asesor'
        self.msmLectura         = 'Sin leer'
        self.msmLeido           = 'Leeido'
        self.msmLeido           = 'Leeido'
        self.formAcuerdos       = 'Compromiso pago'
        self.telefonoPD         = 'telefono'
        self.valor_acordadoPD   = 'valor_acordado'
        self.cuotas_acordadasPD = 'cuotas_acordadas'
        self.interes_acordadosPD = 'interes_acordados'
        self.fecha_pagoPD       = 'fecha_pago'
        self.punto_pagoPD       = 'punto_pago'
        self.numero_productoPD  = 'numero_producto'
        self.rutaDescarga       = '/var/www/web2py/applications/init/static/multimedia/'
        self.smsFinal           = 'En breve este chat finalizará. Si deseas ponerte en contacto con nosotros más adelante puedes hacerlo por este medio.'
        self.colorRgb           = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        self.fechaIntModels     = int(str(datetime.now())[:10].replace('-',''))
        self.horaIntTmp         = int(str(time.strftime("%H:%M:%S")).replace(':',''))
        self.horaSinSeg         = int(str(time.strftime("%H:%M")).replace(':',''))
        self.diaSemana          = datetime.today().strftime('%A')
        self.key                = Fernet.generate_key()
        self.fernet             = Fernet(self.key)
        self.fechaAMD           = str(datetime.now())[:10]
        self.dayGlb             = str(self.fechaAMD).split('-')[2]
        self.mesGlb             = str(self.fechaAMD).split('-')[1]
        self.anioGlb            = str(self.fechaAMD).split('-')[0]
        self.valorFecha         = ''
        self.opcFH              = 'fecha'
        self.pais               = 'Colombia'
        self.codPais            = 'CO'
        self.cantHorarioSeg     = 7
        if str(self.horaIntTmp)[:2] == '00':
            self.horaIntModels = self.horaIntTmp.replace('00','24')
        else:
            self.horaIntModels = self.horaIntTmp
            pass
    
    def emojis( self ):
        import emoji
        emoji_corazon = emoji.emojize(":heart:")
        print(emoji_corazon)  # Imprime ❤
        return emoji


    def descargarMultimedia( self ):
        fileMultimedia = ''
        try:
            fileMultimedia = subprocess.call(self.urlDescarga,shell = True)
        except Exception as e:
            logs = InfoLogs( 'error => descargarMultimedia', e )
            logs.logFile()
            pass
        return fileMultimedia


    def fechaFormato( self ):
        formato  = ''
        try:
            hora  = '00'
            minu  = '00'
            segun = '00'
            if self.opcFH == 'fecha':
                anio = str(self.valorFecha)[:4]
                mes  = str(self.valorFecha)[4:-2]
                dia  = str(self.valorFecha)[6:]
                formato = anio+'-'+str(mes)+'-'+str(dia)
            else:
                if len(str(self.valorFecha)) == 5:
                    hora  = str(self.valorFecha)[:1]
                    minu  = str(self.valorFecha)[1:3]
                    segun = str(self.valorFecha)[3:]
                elif len(str(self.valorFecha)) == 6:
                    hora  = str(self.valorFecha)[:2]
                    minu  = str(self.valorFecha)[2:4]
                    segun = str(self.valorFecha)[4:]
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


    def holidays_word( self ):
        # holidaysCod     = holidays.country_holidays(self.codPais)  # this is a dict
        # logsMostrar('info', 'horaInicialBase: '+str(horaInicialBase)+' ' )
        # logsMostrar('info', 'horaFinalBase: '+str(horaFinalBase)+' ' )
        # logsMostrar('info', 'horaActual: '+str(varData.horaSinSeg)+' ' )
        # logsMostrar('info', 'festivo: '+str(festivo)+' ' )
        # print('info', 'holidaysCod: '+str(holidaysCod)+' ' )
        # tmp = date(2022, 11, 14) in us_holidays  # True
        # print('info', 'tmp: '+str(tmp)+' ' )
        # resulDia  = tmp
        # return resulDia
        pass

class EncryDesCry:
    def __init__( self, text ):
        self.text = text

    
    def generate_key( self ):
        """
        Generates a key and save it into a file
        """
        key = Fernet.generate_key()
        with open("/var/www/web2py/applications/init/private/secret.key", "wb") as key_file:
            key_file.write(key)


    def load_key( self ):
        """
        Load the previously generated key
        """
        return open("/var/www/web2py/applications/init/private/secret.key", "rb").read()

    def EnCry( self ):
        textRet = ''
        try:
            key             = self.load_key()
            encoded_message = str(self.text).encode()
            f               = Fernet(key)
            textRet         = f.encrypt(encoded_message)
        except Exception as e:
            logs = InfoLogs( 'error', 'EnCry =>  '+str(e)+'')
            logs.logFile()
            pass
        return textRet


    def desCry( self ):
        textRet = ''
        try:
            print('self.text', self.text)
            print('self.type', type(self.text))
            key      = self.load_key()
            f        = Fernet(key)
            encoded_message = self.text.decode()
            textRet  = f.decrypt(encoded_message)
        except Exception as e:
            logs = InfoLogs( 'error', 'desCry =>  '+str(e)+'')
            logs.logFile()
            pass
        print('textRet', textRet)
        return textRet
    

class InfoLogs:
    
    def __init__( self, tipo, sms ):
        self.tipo = tipo
        self.sms = sms

    def logFile( self ):

        if self.sms:
            if self.tipo == 'error':
                logger.error(self.sms)
            elif self.tipo == 'info':
                logger.info(self.sms)
            elif self.tipo == 'warning':
                logger.warning(self.sms)
            else:
                logger.critical(self.sms)
                pass
        else:
            if self.sms:
                logger.info(self.sms)
            else:
                logger.critical('Informacion sin sms')
                pass
            pass



class RtTonadoWeb:

    def __init__( self, people, mensaje ):
        self.people = people
        self.mensaje = mensaje

    
    def rtInfo( self ):
        varGl  = DataGlobal()
        try:
            tmpRul = varGl.urlRt+':'+str(varGl.portRt)
            tmp = websocket_send(tmpRul, self.mensaje, varGl.keyRt,self.people)
            # logs = InfoLogs( 'info', 'Pasa por el RT' )
            # logs.logFile()
        except Exception as e:
            logs = InfoLogs( 'error', e )
            logs.logFile()
            pass
            


class PlantillaUser:

    def __init__( self, tipeUser ):
        self.tipeUser = tipeUser

    def rederPalntilla( self ):
        varGl  = DataGlobal()
        if self.tipeUser == 'Gerente':
            plantillaRender = 'templateGer.html'
        elif self.tipeUser == 'Asesor':
            plantillaRender = 'templateAds.html'
        elif self.tipeUser == 'Developer':
            plantillaRender = 'templateAdmin.html'
        elif self.tipeUser == 'Director':
            plantillaRender = 'templateAdmin.html'
        else:
            plantillaRender = varGl.plantillaNoF
            pass
        return plantillaRender


class ConexionStrauss:

    def __init__(self):
        self.keyPrivateStrauss  = ''
        self.hostStrauss        = ''
        self.bDStrauss          = ''
        self.userStaruss        = ''
        self.nomEmpresa         = ''
        self.nomCliente         = ''
        self.nomSegmento        = ''
        self.userLocal          = 'root'
        self.keyPrivateLocal    = 'j7t05fLcn0'
        self.hostLocal          = 'localhost'
        self.bDLocal            = 'chatbot_asesor'

    def conexionBdEmpStrauss( self ):
        engineStrauss  = False
        try:
            varGl  = DataGlobal()
            engineStrauss  = create_engine(
                "mysql+pymysql://"+str(self.userStaruss)+":"+str(self.keyPrivateStrauss)+"@"+str(self.hostStrauss)+"/"+str(self.bDStrauss)+""
            )
        except Exception as e:
            logs = InfoLogs( 'error => conexionBdEmpStrauss', e )
            logs.logFile()
            pass
        return engineStrauss


    def conexionBdLocal( self ):
        engineLocal  = False
        try:
            varGl  = DataGlobal()
            engineLocal  = create_engine(
                "mysql+pymysql://"+str(self.userLocal)+":"+str(self.keyPrivateLocal)+"@"+str(self.hostLocal)+"/"+str(self.bDLocal)+""
            )
        except Exception as e:
            logs = InfoLogs( 'error => conexionBdLocal', e )
            logs.logFile()
            pass
        return engineLocal

    def datosDBHomologa( self ):
        datosHomologa = []
        try:
            conex = self.conexionBdEmpStrauss()
            # print('conex', conex)
            if conex:
                sqlDatos = """
                    SELECT
                        idresultado_intelibpo as idResultado,
                        resultado_cliente as resultado
                    FROM
                        homologaciones
                    WHERE 
                        canal_intelibpo = 'CHATBOT'
                    AND
                        cliente = '"""+str(self.nomCliente)+"""'
                    AND
                        segmento  = '"""+str(self.nomSegmento)+"""'
                    GROUP BY resultado_cliente
                """
                # print('sqlDatos', sqlDatos)
                with conex.connect() as connection:
                    countData = connection.execute(sqlDatos)
                countDataInfo = countData.fetchall()
                if len(countDataInfo) > 0:
                    for item in countDataInfo:
                        datosHomologa.append(
                            dict(
                               descripcion = item['resultado'],
                               idResultado = item['idResultado']
                            )
                        )
                        pass
                    pass
                # print('datosHomologa', datosHomologa)
        except Exception as e:
            logs = InfoLogs( 'error => datosDBHomologa', e )
            logs.logFile()
            pass
        return datosHomologa


    

class ConexionWhast:

    def __init__(self, sms, empresaNombre, clienteNombre, segmentoNombre, numberCliente):
        self.sms            = sms
        self.empresaNombre  = empresaNombre
        self.clienteNombre  = clienteNombre
        self.segmentoNombre = segmentoNombre
        self.numberCliente  = numberCliente
        self.nameContex     = ''
        self.bodyText       = ''
        self.varContexto    = ''
        self.tipoSmsSend    = 'text'
        self.source         = ''
        self.number         = '3015237437' 
        self.idtemp         = ''
        self.params         = ''
        self.appid          = ''
        self.token          = ''
        self.APIKey         = ''
        self.idInstance     = 0
        self.fechaIntModels = int(str(datetime.now())[:10].replace('-',''))
        self.horaIntTmp     = int(str(time.strftime("%H:%M:%S")).replace(':',''))
    def conexionBdExt( self ):
        engineStrauss  = False
        try:
            varGl  = DataGlobal()
            engineStrauss  = create_engine(
                "mysql+pymysql://"+str(varGl.userBDChatbot)+":"+str(varGl.keyPrivate)+"@"+str(varGl.hostDBChatbot)+"/"+str(varGl.dbDBChatbot)+""
            )
        except Exception as e:
            logs = InfoLogs( 'error => conexionBdExt', e )
            logs.logFile()
            pass
        return engineStrauss



    def datosBDInstanceId( self ):
        datosInstance = []
        try:
            conex = self.conexionBdExt()
            if conex:
                sqlDatos = """
                    SELECT
                        num_instance as num_instance,
                        instance_id as instance_id,
                        token as token,
                        tokenApp as APIKey,
                        appId as appid,
                        status_send as status_send,
                        intensidad as intensidad,
                        prioridad as prioridad,
                        id_instancias as id_instancias,
                        estado as estado
                    FROM
                        chatbot.instancias_chatapi
                    WHERE
                        id_instancias = {0}
                """.format(self.idInstance)
                with conex.connect() as connection:
                    countData = connection.execute(sqlDatos)
                countDataInfo = countData.fetchall()
                if len(countDataInfo) > 0:
                    for item in countDataInfo:
                        datosInstance.append(
                            dict(
                               num_instance = item['num_instance'],
                               instance     = item['instance_id'], 
                               token        = item['token'],
                               APIKey       = item['APIKey'],
                               appid        = item['appid'],
                               status_send  = item['status_send'],
                               intensidad   = item['intensidad'],
                               prioridad    = item['prioridad'],
                               idInstance   = item['id_instancias'],
                               estado       = item['estado']
                            )
                        )
                        pass
                pass
        except Exception as e:
            logs = InfoLogs( 'error => datosBDInstanceId', e )
            logs.logFile()
            pass
        return datosInstance


    def datosBDInstance( self ):
        datosInstance = []
        try:
            conex = self.conexionBdExt()
            if conex:
                sqlDatos = """
                    SELECT
                        num_instance as num_instance,
                        instance_id as instance_id,
                        token as token,
                        tokenApp as APIKey,
                        appId as appid,
                        status_send as status_send,
                        intensidad as intensidad,
                        prioridad as prioridad,
                        id_instancias as id_instancias,
                        estado as estado
                    FROM
                        chatbot.instancias_chatapi
                    WHERE
                        empresa = '"""+str(self.empresaNombre)+"""'
                    AND 
                        cliente = '"""+str(self.clienteNombre)+"""'
                    AND 
                        segmento = '"""+str(self.segmentoNombre)+"""'
                """
                # print('sqlDatos =>', sqlDatos)
                with conex.connect() as connection:
                    countData = connection.execute(sqlDatos)
                countDataInfo = countData.fetchall()
                # print('countDataInfo =>', countDataInfo)
                if len(countDataInfo) > 0:
                    for item in countDataInfo:
                        datosInstance.append(
                            dict(
                               num_instance = item['num_instance'],
                               instance     = item['instance_id'], 
                               token        = item['token'],
                               APIKey       = item['APIKey'],
                               appid        = item['appid'],
                               status_send  = item['status_send'],
                               intensidad   = item['intensidad'],
                               prioridad    = item['prioridad'],
                               idInstance   = item['id_instancias'],
                               estado       = item['estado']
                            )
                        )
                        pass
                pass
        except Exception as e:
            logs = InfoLogs( 'error => datosBDInstance', e )
            logs.logFile()
            pass
        return datosInstance


    def insertUpdateContex( self ):
        cantidadCont   = 0
        cantidadContTE = 0
        datosInstance  = 1
        try:
            conex = self.conexionBdExt()
            if conex:
                # Eliminamos el template si ya esta creado en la tabla los contextos de esta ECS
                sqlUpdatECS = """
                    DELETE
                    FROM
                        chatbot.contextos
                    WHERE
                        empresa = '{0}'
                    AND 
                        cliente  = '{1}'
                    AND 
                        segmento  = '{2}'
                    AND
                        id_template = '{3}'
                """.format(self.empresaNombre,self.clienteNombre,self.segmentoNombre,self.idtemp)
                
                with conex.connect() as connection:
                    connection.execute(sqlUpdatECS)

                # Creamos un contexto ya creado
                sqlInsertECST = """
                    INSERT
                        INTO
                        chatbot.contextos (
                            nombre_contexto,
                            texto_contexto,
                            variables_contexto,
                            fecha_registro,
                            empresa,
                            cliente,
                            segmento,
                            fecha_creacion,
                            hora_creacion,
                            estado,
                            id_template
                        )
                        VALUES(
                            '{0}',
                            '{1}',
                            '{2}',
                            '{9}',
                            '{3}',
                            '{4}',
                            '{5}',
                            {6},
                            {7},
                            1,
                            '{8}'
                        );
                """.format(self.nameContex,self.bodyText,self.varContexto,self.empresaNombre,self.clienteNombre,self.segmentoNombre,self.fechaIntModels,self.horaIntTmp,self.idtemp,datetime.now())
                with conex.connect() as connection:
                    connection.execute(sqlInsertECST)
                pass
        except Exception as e:
            logs = InfoLogs( 'error => datosBDInstance', e )
            logs.logFile()
            datosInstance  = 0
            pass
        return datosInstance


    def conexionSend( self ):
        resApi     = 0
        try:
            varGl  = DataGlobal()
            
            if len(self.datosBDInstance()) > 0:
                for item in self.datosBDInstance():
                    payload = {
                        "channel" : "whatsapp",
                        "source" : str(item['num_instance']),
                        "destination" : str(self.numberCliente),
                        "src.name": str(item['instance']),
                        "message" : {
                            "type": self.tipoSmsSend,
                            "text": str(self.sms).replace(u'\xa0', u' ')
                        }
                    }
                    headers = {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'apikey': ''+str(item['token'])
                    }
                    pass
                resApi = requests.request("POST", varGl.urlApiWh, headers=headers, data=urllib.parse.urlencode(payload))
                pass
        except Exception as e:
            resApi = 0
            logs = InfoLogs( 'error => conexionSend', e )
            logs.logFile()
            pass
        print('resApi =>', resApi)
        return resApi

    def get_template(self):
        """Permite consultar los templates que se encuentran registrados en gupshup independientemente el estado del mismo, de aqui se consulta para saber cuales Templates se pueden usar y cuales no, solo los de status APPROVED pueden ser utilizados"""
        
        url = "http://partner.gupshup.io/partner/app/{0}/templates".format(self.appid)

        payload={}
        headers = {
          'token': self.token,
          'Connection': 'keep-alive'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return json.loads(response.text)
    

    def get_templateId(self):
        """Permite consultar un templates que se encuentran registrados en gupshup independientemente el estado del mismo, de aqui se consulta para saber cuales Templates se pueden usar y cuales no, solo los de status APPROVED pueden ser utilizados"""
        
        url = "http://partner.gupshup.io/partner/app/{0}/templates/{1}".format(self.appid,self.idtemp)
        print('Url template => ', url)
        payload={}
        headers = {
          'token': self.token,
          'Connection': 'keep-alive'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return json.loads(response.text)
    
    
    def enable_optin(self):
        """Funci n para habilitar el n mero para recepci n de WhatsApps"""

        print("habilitando n mero optin")
        url = "http://partner.gupshup.io/partner/app/{0}/optin".format(self.appid)

        payload='phone='+str(self.number)
        headers = {
          'Connection': 'keep-alive',
          'Authorization': self.token,
          'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        # print('response.text =>', response.text)
        # print('response.status_code =>', response.status_code)
        return response.status_code
    

    def send_message_test(self):
        """Funcion para env o de mensajes individuales"""
        # print("Enviando mensaje al n mero "+self.number)
        url = "http://partner.gupshup.io/partner/app/{0}/template/msg".format(self.appid)

        payload={'source':self.source,
                 'sandbox':'false',
                 'destination':self.number,
                 'template':'{"id":"'+self.idtemp+'","params":'+str(self.params).replace("'",'"')+'}',
                 'src.name':'InteliBPO'}
        print('payload =>', payload)
        headers = {
          'Connection': 'keep-alive',
          'Authorization': self.token,
          'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data=urlencode(payload))
        # print(response.text)
        # print(response.status_code)
        return response.status_code


