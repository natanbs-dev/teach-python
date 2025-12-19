# metodos basicos

"""
GET = verificar um valor
PUT = editar um valor
POST = criar um valor
DELETE = deletar um valor
PATCH = editar partes do conteudo
"""

# imports
import falcon
import json
import os

if False:
    print("https://github.com/devmatheusguerra/frasesJSON/blob/main/README.md")
print("circulando")

frases :list = []

with open("frases.json", "r") as file:
    frases = json.loads(file.read())

class Frases(object):
    def on_get(self,req, resp):
        resp.status = falcon.HTTP_200 #ok e devolve o conteudo
        resp.text = json.dumps(frases)

    def on_post(self, req, resp):
        frases.append(req.get_media())
        resp.status = falcon.HTTP_204 # 204 No Content

    def on_delete(self, req, resp, frases_id):
        for frase in frases:
            if int(frase["id"]) == int(frases_id):
                frases.remove(frase)
                continue
        resp.status = falcon.HTTP_204

    def on_put(self, req, resp, frases_id):
        self.on_delete(req, resp, frases_id) # metodo do on_delete
        return self.on_post(req, resp)

# criando uma instancia
app = falcon.App()

#criando instancia da classe frases
frases1 = Frases()

#teste a ser feito no postman
app.add_route('/{frases_id}', frases1)
app.add_route('/', frases1)

