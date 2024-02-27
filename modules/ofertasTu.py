import logging
from datetime import  datetime, date, timedelta, time 
import time, requests
import random
from sqlalchemy import create_engine
import pandas as pd
import subprocess
from _clasFunt import DataGlobal, ConexionStrauss, InfoLogs


class ofertasTuacuerdo:
	
	def __init__(self, empresa, cliente, segmento, identificacion, token):

		self.empresa            = empresa
		self.cliente            = cliente
		self.segmento           = segmento
		self.identificacion     = identificacion
		self.token              = token
		self.tabla              = 'data_data_informacion_deudores'
		self.dataFrame          = ''
		self.tipo               = 'Dia'
		self.simbolo            = '$'
		self.dominoTu           = 'tuacuerdo.com'
		self.peru               = ['Banazteca','Falabella','AFP']


	def recordOfertas( self ):
		ofertas  = []
		if self.empresa in self.peru:
			self.simbolo  = 'S/'
		elif self.empresa == 'banguayaquil':
			self.simbolo = 'US'
		else:
			self.simbolo = '$'
			pass

		for index, row in self.dataFrame.iterrows():
			if row['nombreCodeudor']:
				tipo_cliente = 'Codeudor'
			else:
				tipo_cliente = 'Titular'
				pass
			ofertas.append(
				dict(
					idRegistro          = row['idRegistro'],
					Voferta             = row['valorOferta'],
					creacionF           = str(row['creacionFecha']),
					tipo                = self.tipo,
					nomPersona          = row['NomPersona'],
					vCapital            = row['vCapital'],
					vCorriente          = row['vCorriente'],
					vMora               = row['vMora'],
					ncuotas             = row['Ncuotas'],
					fPago               = str(row['fpago']),
					vTotalDeuda         = row['vTotalDeuda'],
					producto            = row['producto'],
					placa               = row['placa'],
					telefono            = row['telefono'],
					segmento            = row['segmento'],
					dMora               = row['dMora'],
					urlTu               = row['Url'],
					token               = row['token'],
					condonac            = row['condonacion'],
					vInCorrientes       = row['vInCorrientes'],
					vIntMora            = row['vIntMora'],
					vDescuMora          = row['vDescuMora'],
					vDescCorrientes     = row['vDescCorrientes'],
					pDescMora           = row['pDescMora'],
					pDescCorrientes     = row['pDescCorrientes'],
					pDescOtrosIntereses = row['pDescOtrosIntereses'],
					vDescOtrosIntereses = row['vDescOtrosIntereses'],
					idCodeudor          = row['idCodeudor'],
					nombreCodeudor      = row['nombreCodeudor'],
					canal               = 'tuacuerdo',
					tipo_cliente        = tipo_cliente,
					identiPersona       = row['identiPersona']
				)
			)
		pass
		return ofertas

	def activasOfertas( self ):
		ofertas  = []
		try:
			listSegmentos = ''
			conex                   = ConexionStrauss()
			conex.userStaruss       = 'tuacuerdo'
			conex.keyPrivateStrauss = 'r$L&gwM6zms7A'
			conex.hostStrauss       = self.dominoTu
			conex.bDStrauss         = 'tuacuerdo'
			self.dataFrame          = pd.DataFrame()
			if conex.conexionBdEmpStrauss():
				sqlOfertasDia = """
					SELECT
						d.id as idRegistro,
						d.valor_oferta as valorOferta,
						date(d.fecha_creacion) as creacionFecha,
						d.nombres_persona as NomPersona,
						d.valor_original_capital as vCapital,
						d.valor_original_corriente as vCorriente,
						d.valor_original_mora as vMora,
						d.numero_cuotas as Ncuotas,
						d.vencimiento as fpago,
						d.valor_original_saldo_total as vTotalDeuda,
						d.numero_producto as producto,
						d.placa as placa,
						d.telefono_persona as telefono,
						d.portafolio_cobranza as segmento,
						d.dias_mora as dMora,
						d.token as token,
						CONCAT('tuacuerdo.com/',dm.acortador,'/',d.token) as Url,
						d.condonacion as condonacion,
						d.valor_original_corriente as vInCorrientes,
						d.valor_original_mora as vIntMora,
						d.descuento_intereses_mora as vDescuMora,
						d.descuento_intereses_corrientes as vDescCorrientes,
						d.descuento_intereses_corrientes as vDescOtrosIntereses,
						d.porcentaje_descuento_intereses_mora as pDescMora,
						d.porcentaje_descuento_intereses_corrientes as pDescCorrientes,
						d.porcentaje_descuento_otros_intereses as pDescOtrosIntereses,
						d.identificacion_persona as identiPersona,
						d.prioridad as prioridad,
						d.idbase as idBase,
						d.idCodeudor as idCodeudor,
						d.nombreCodeudor as nombreCodeudor
					FROM
						"""+str(self.tabla)+""" as d
					INNER JOIN 
						data_mockupsdefinido dm 
					ON
						dm.id = d.mockupsDefinido 
					WHERE
						d.empresa_cobranza = '"""+str(self.empresa)+"""'
					AND 
						d.cliente_cobranza = '"""+str(self.cliente)+"""'
					AND
						d.portafolio_cobranza = '"""+str(self.segmento)+"""'
					AND
						(d.identificacion_persona = '"""+str(self.identificacion)+"""' OR d.token = '"""+str(self.token)+"""')
					ORDER BY
						date(fecha_creacion) DESC
				"""
				# print('sqlOfertasDia =>', sqlOfertasDia)
				self.dataFrame = self.dataFrame.append(pd.read_sql_query(sqlOfertasDia,conex.conexionBdEmpStrauss()))
				self.dataFrame.drop_duplicates(subset=['identiPersona', 'producto','Ncuotas','valorOferta'],inplace=True)
				# print('Columns 128', self.dataFrame.columns.values)
				# print('self.dataFrame 129', self.dataFrame[['identiPersona','creacionFecha','idRegistro','Ncuotas','valorOferta','prioridad','idBase','producto']])
				self.dataFrame = self.dataFrame.sort_values("creacionFecha",ascending=False)
				# print('self.dataFrame 131', self.dataFrame)
				#self.dataFrame = self.dataFrame.merge(self.dataFrame[["identiPersona","producto","creacionFecha"]].groupby(["identiPersona","producto"]).max(),how="inner",on=["identiPersona","producto","creacionFecha"])
				self.dataFrame.drop_duplicates(inplace=True)
				self.dataFrame = self.dataFrame.sort_values("prioridad",ascending=True)
				# print('self.dataFrame final',self.dataFrame)
				# print('self.dataFrame final', self.dataFrame[['idCodeudor','nombreCodeudor']])
				# ofertas       = self.dataFrame.to_dict('index')
				# .values.tolist()
				ofertas       =  self.recordOfertas()
				pass
		except Exception as e:
			logs = InfoLogs( 'error', 'Error en: activasOfertas => '+str(e)+'' )
			logs.logFile()
			pass
		return ofertas


	def contadorOfertas( self ):
		dfCtnOferta = pd.DataFrame()
		ofertCant   = 0
		conex                   = ConexionStrauss()
		conex.userStaruss       = 'tuacuerdo'
		conex.keyPrivateStrauss = 'r$L&gwM6zms7A'
		conex.hostStrauss       = self.dominoTu
		conex.bDStrauss         = 'tuacuerdo'
		if conex.conexionBdEmpStrauss():
			sqlCountOfertasDia = """
				SELECT 
					COUNT(1) as cantidad
				FROM
					"""+str(self.tabla)+"""
				WHERE
					empresa_cobranza = '"""+str(self.empresa)+"""'
				AND 
					cliente_cobranza = '"""+str(self.cliente)+"""'
				AND
					portafolio_cobranza = '"""+str(self.segmento)+"""'
				AND 
					(identificacion_persona = '"""+str(self.identificacion)+"""' OR token = '"""+str(self.token)+"""')
			"""
			# print('sqlCountOfertasDia', sqlCountOfertasDia)
			dfCtnOferta = dfCtnOferta.append(pd.read_sql_query(sqlCountOfertasDia,conex.conexionBdEmpStrauss()))
			pass
		return dfCtnOferta

	def ordenamiento( self ):
		ofertasList = []
		# print('self.empresa, self.identificacion', self.empresa, self.identificacion)
		cantOfertas = self.contadorOfertas()
		# print('cantOfertas', cantOfertas['cantidad'][0])
		if cantOfertas['cantidad'][0] > 0:
			ofertasList = self.activasOfertas()
			pass
		# print('ofertasList', ofertasList)
		return ofertasList