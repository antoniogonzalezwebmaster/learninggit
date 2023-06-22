import datetime
import re

class Persona:

	def __init__(self, nombre, edad):
		self.__nombre = nombre
		self.__edad = edad

	def asignar_edad(self, edad):
		self.__edad = edad

	def asignar_nombre(self, nombre):
		self.__nombre = nombre

	def edad(self):
		return(self.__edad)

	def nombre(self):
		return(self.__nombre)

	def asignar_rfc(self, rfc):
		self.__rfc = rfc

	def rfc(self):
		return(self.__rfc)

	def calcular_anio_nacimiento(self, ya_cumplio_anios):
		anio_actual = datetime.datetime.now().year
		if ya_cumplio_anios:
			return (anio_actual - self.__edad)
		else:
			return (anio_actual - self.__edad + 1)

	def validar_rfc(self):
		regex = r"^(((?!(([CcKk][Aa][CcKkGg][AaOo])|([Bb][Uu][Ee][YyIi])|([Kk][Oo](([Gg][Ee])|([Jj][Oo])))|([Cc][Oo](([Gg][Ee])|([Jj][AaEeIiOo])))|([QqCcKk][Uu][Ll][Oo])|((([Ff][Ee])|([Jj][Oo])|([Pp][Uu]))[Tt][Oo])|([Rr][Uu][Ii][Nn])|([Gg][Uu][Ee][Yy])|((([Pp][Uu])|([Rr][Aa]))[Tt][Aa])|([Pp][Ee](([Dd][Oo])|([Dd][Aa])|([Nn][Ee])))|([Mm](([Aa][Mm][OoEe])|([Ee][Aa][SsRr])|([Ii][Oo][Nn])|([Uu][Ll][Aa])|([Ee][Oo][Nn])|([Oo][Cc][Oo])))))[A-Za-zñÑ&][aeiouAEIOUxX]?[A-Za-zñÑ&]{2}(((([02468][048])|([13579][26]))0229)|(\d{2})((02((0[1-9])|1\d|2[0-8]))|((((0[13456789])|1[012]))((0[1-9])|((1|2)\d)|30))|(((0[13578])|(1[02]))31)))[a-zA-Z1-9]{2}[\dAa])|([Xx][AaEe][Xx]{2}010101000))$"

		if re.search(regex, self.__rfc):
			return True
		else:
			return False

