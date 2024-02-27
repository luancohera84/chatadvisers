# -*- coding: utf-8 -*-
from _clasFunt import DataGlobal, ConexionWhast
import json
import datetime
import time

def lisTemplatesLast( empresa, cliente, segmento ):
    conexApiWhat    = ConexionWhast( '', empresa, cliente, segmento, '' )
    isinstans       = conexApiWhat.datosBDInstance()
    data            = []
    varTmp          = 'test_inteli'
    if len(isinstans) > 0:
        for item in isinstans:
            conexApiWhat.appid      = item['appid']
            conexApiWhat.token      = item['APIKey']
            if conexApiWhat.appid:
                templatesTmp        = conexApiWhat.get_template()
                if templatesTmp:
                    for itemTem in templatesTmp['templates']:
                        if itemTem['status'] == 'APPROVED':
                            tmpSplit  = str(itemTem['elementName']).split('_')
                            if str(tmpSplit[0]).lower() == str(empresa).lower():
                                data.append(
                                    dict(
                                        nameTemplate  = str(itemTem['elementName']).capitalize(),
                                        idTemplate    = itemTem['id'],
                                        status        = itemTem['status']
                                    )
                                )
                                pass
                            pass
                        pass
                    pass
                pass
            pass
        pass
    return data


def idTemplatesInsert( empresa, cliente, segmento, idTemplate ):
    conexApiWhat    = ConexionWhast( '', empresa, cliente, segmento, '' )
    isinstans       = conexApiWhat.datosBDInstance()
    data            = 0
    tmpVar          = []
    if len(isinstans) > 0:
        for item in isinstans:
            conexApiWhat.appid      = item['appid']
            conexApiWhat.token      = item['APIKey']
            conexApiWhat.idtemp     = idTemplate
            if conexApiWhat.appid:
                templatesTmp        = conexApiWhat.get_templateId()
                # logsMostrar( 'info', 'idTemplatesInsert ASESOR => templatesTmp '+str(templatesTmp)+'' )
                if templatesTmp:
                    if templatesTmp['status'] != 'error':
                        if templatesTmp['template']['status'] == 'APPROVED':
                            conexApiWhat.empresaNombre   = empresa
                            conexApiWhat.clienteNombre   = cliente
                            conexApiWhat.segmentoNombre  = segmento
                            conexApiWhat.nameContex      = templatesTmp['template']['elementName']
                            conexApiWhat.bodyText        = templatesTmp['template']['data']
                            import json
                            tmp          = json.loads(str(templatesTmp['template']['meta']).replace('!', '').replace('],', '] ,').replace('],[', '] , [') )
                            for item in tmp['example'].split():
                                if str(item)[0] == '[':
                                    tmpVar.append(str(item).replace('[','').replace(']','').replace('.','').replace(',',''))
                                    pass
                                pass
                            conexApiWhat.varContexto     = str(tmpVar).replace("'",'"')
                            conexApiWhat.idtemp          = idTemplate
                            data  = conexApiWhat.insertUpdateContex()
                            pass
                        pass
                    pass
                pass
            pass
        pass
    return data
# chatgushupapi@intelibpo.com
# *?Mko0*?Zaq1*?