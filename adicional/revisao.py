# imports
import falcon
import json

frases :list = []

# Carregar as frases
# https://github.com/devmatheusguerra/frasesJSON/blob/main/README.md
with open('frases.json', 'r') as file:
    frases = json.load(file)


class Frases(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200 # 200 OK e devolve conteudo
        resp.text = json.dumps(frases)

    def on_post(self, req, resp):
        frases.append(req.get_media())
        resp.status = falcon.HTTP_204 # 204 No Content que não devolve conteudo

    def on_delete(self, req, resp, frase_id):
        for frase in frases:
            if int(frase['id']) == int(frase_id):
                frases.remove(frase)
                continue
        resp.status = falcon.HTTP_204 # 204 No Content

    def on_put(self, req, resp, frase_id):
        self.on_delete(req, resp, frase_id)
        return self.on_post(req, resp)

# Criar uma instancia
app = falcon.App()

# Criar um instancia da classe Frases
index = Frases()

# Podemos testar a nossa API usando o app https://hoppscotch.io/
app.add_route('/{frase_id}', index)
app.add_route('/', index)
