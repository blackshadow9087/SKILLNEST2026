# Crea un archivo de Python llamado suscripcion_streaming.py.

#  Define la clase SuscripcionStreaming, que debe incluir:

# Atributos:
# usuario (nombre del usuario asociado a la suscripción)
# tipo_suscripcion (Gratis, Estándar, Premium)
# costo_mensual (según el tipo de suscripción)
# saldo_pendiente (monto acumulado que debe pagar el usuario)
# Métodos:
# realizar_pago(self, monto) reduce el saldo pendiente según el monto pagado.
# cambiar_suscripcion(self, nuevo_tipo) cambia el tipo de suscripción y ajusta el costo mensual.
# ver_contenido_exclusivo(self) permite el acceso a contenido según el tipo de suscripción. La suscripción “Gratis” no tiene acceso a contenido exclusivo.
# mostrar_info_suscripcion(self) muestra el estado actual de la suscripción del usuario.
#  Realizar las siguientes pruebas con instancias:

# Crea 3 usuarios con diferentes tipos de suscripción.
# Haz que el primer usuario intente ver contenido exclusivo, mejore su suscripción y pague su saldo.
# Haz que el segundo usuario vea contenido exclusivo, cambie su suscripción a Premium y pague dos veces.
# Haz que el tercer usuario intente pagar una cantidad menor a su saldo pendiente y vea contenido exclusivo.


class SuscripcionStreaming:
   costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

   def __init__(self, usuario, tipo_suscripcion="Gratis"):
       self.usuario = usuario #Nombre del usuario
       self.tipo_suscripcion = tipo_suscripcion #El tipo de suscripcion
       self.costo_mensual = SuscripcionStreaming.costos_suscripcion[tipo_suscripcion] #Gratis por defecto
       self.saldo_pendiente = self.costo_mensual

   def realizar_pago(self, monto):
       """Reduce el saldo pendiente según el monto pagado."""
       if monto < self.saldo_pendiente:
           print(f"El usuario {self.usuario} no tiene suficiente monto para pagar tu saldo (jaja pobre)")
       else:
           print(f"El usuario {self.usuario} ha pagado su saldo con exito")
           self.saldo_pendiente -=  monto

       
   def cambiar_suscripcion(self, nuevo_tipo):
       """Cambia el tipo de suscripción y actualiza el costo mensual."""
       self.tipo_suscripcion = nuevo_tipo
       self.nuevo_costo = self.costo_mensual = SuscripcionStreaming.costos_suscripcion[self.tipo_suscripcion]
       print(f"El usuario {self.usuario} ha cambiado su suscripcion a {self.tipo_suscripcion}")

   def ver_contenido_exclusivo(self):
       """Permite ver contenido exclusivo según el tipo de suscripción."""
       if self.tipo_suscripcion == "Premium":
           print(f"El usuario {self.usuario} puede ver contenido {self.tipo_suscripcion}")

       elif self.tipo_suscripcion == "Estándar":
           print(f"El usuario {self.usuario} puede ver contenido {self.tipo_suscripcion}")

       elif self.tipo_suscripcion == "Gratis":
           print(f"El ususario {self.usuario} no puede ver ningun contenido exclusivo")

   def mostrar_info_suscripcion(self):
       """Muestra la información de la suscripción del usuario."""
       print(f"Usuario: {self.usuario}, Tipo de Suscripcion: {self.tipo_suscripcion}, Saldo pendiente: {self.saldo_pendiente}")

u1 = SuscripcionStreaming("Juan Perez")

u2 = SuscripcionStreaming("Pablo Fernandez", "Estándar")

u3 = SuscripcionStreaming("Julian Lomanco", "Estándar")

u1.ver_contenido_exclusivo()
u1.cambiar_suscripcion("Estándar")
u1.realizar_pago(100)

u2.ver_contenido_exclusivo()
u2.cambiar_suscripcion("Premium")
u2.realizar_pago(100)
u2.realizar_pago(100)

u3.realizar_pago(4)
u3.ver_contenido_exclusivo()