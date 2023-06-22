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

	def menor_de_edad(self):
		persona = Persona(nombre="Adolfo", edad=47)
		assert persona.edad() > 18

	def mayor_de_edad(self):
		persona = Persona(nombre="Adolfo", edad=15)
		assert persona.edad