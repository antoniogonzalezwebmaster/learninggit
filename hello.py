clase={
	"nombre":"Tópicos Selectos de T.I.",
	"participantes":[
		{
			"rol":"catedrático",
			"nombre":"Antonio González",
			"email":"antoniogonzalezwebmaster@gmail.com"
		}

		{
			"rol":"estudiante",
			"nombre":"Adolfo Romero",
			"email":"adolfo.romero.escalona@gmail.com"
		}
	]	
}




print("Clase de GIT para la clase de {}".format(clase["nombre"]))

for persona in clase["participantes"]:
	print("Nombre:{}\t Correo:{}".format(persona["nombre"],persona["email"]))
