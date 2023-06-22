import pytest
import datetime
from persona import Persona

class TestPersona:

	def test_prueba(self):
		assert 0 == 0

	def test_constructor(self):
		persona = Persona(nombre="Diego", edad=25)
		assert persona.nombre() == "Diego"
		assert persona.edad() == 25

	def test_asingacion(self):
		persona = Persona(nombre="Diego", edad=25)
		persona.asignar_edad(28)
		persona.asignar_nombre("Adriana")
		assert persona.nombre() != "Diego"
		assert persona.edad() != 25
		assert persona.nombre() == "Adriana"
		assert persona.edad() == 28

	def test_contiene_texto(self):
		persona = Persona(nombre="María Alejandra", edad=22)
		assert "Alejandra" in persona.nombre()

	def test_anio_nacimiento(self):
		persona = Persona(nombre="María Alejandra", edad=22)
		assert persona.calcular_anio_nacimiento(True) == datetime.datetime.now().year - 22
		assert persona.calcular_anio_nacimiento(False) == datetime.datetime.now().year - 22 + 1

	def test_rfc(self):
		casos_prueba = {
			"RFC valido": {
				"rfc": "GODJ980101H31",
				"resultado": True
			},
			"RFC invalido": {
				"rfc": "GODJ980101H3",
				"resultado": False
			},
			"RFC vacio": {
				"rfc": "",
				"resultado": False
			},
			"RFC con más carácteres": {
				"rfc": "GODJ980101H312",
				"resultado": False
			},
		}

		for caso in casos_prueba:
			resultado_esperado = casos_prueba[caso]["resultado"]
			rfc = casos_prueba[caso]["rfc"]
			persona = Persona(nombre="María Alejandra", edad=22)

			persona.asignar_rfc(rfc)
			print("Caso de prueba: " + caso)

			assert persona.validar_rfc() == resultado_esperado
