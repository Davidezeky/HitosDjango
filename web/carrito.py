class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        if 'carrito' not in self.session:
            self.session['carrito'] = {}
        self.carrito = self.session['carrito']

    def agregar(self, flan):
        flan_uuid = str(flan.flan_uuid)
        if flan_uuid not in self.carrito:
            self.carrito[flan_uuid] = {
                'flan_uuid': flan.flan_uuid,
                'name': flan.name,
                'acumulado': flan.precio,
                'cantidad': 1,
            }
        else:
            self.carrito[flan_uuid]['cantidad'] += 1
            self.carrito[flan_uuid]['acumulado'] += flan.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def eliminar(self, flan):
        flan_uuid = str(flan.flan_uuid)
        if flan_uuid in self.carrito:
            del self.carrito[flan_uuid]
            self.guardar_carrito()

    def restar(self, flan):
        flan_uuid = str(flan.flan_uuid)
        if flan_uuid in self.carrito:
            self.carrito[flan_uuid]['cantidad'] -= 1
            self.carrito[flan_uuid]['acumulado'] -= flan.precio
            if self.carrito[flan_uuid]['cantidad'] <= 0:
                self.eliminar(flan)
            self.guardar_carrito()

    def limpiar(self):
        self.session['carrito'] = {}
        self.session.modified = True
