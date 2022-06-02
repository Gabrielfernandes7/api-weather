from requests import *
import json

url = 'http://api.weatherapi.com/v1/current.json?key=b88ef79595c940ccb1a155249220106&q=Fortaleza&aqi=no'

parametros = {}

resposta = request("GET", url, params=parametros)

objetos = json.loads(resposta.text)

dados = objetos['current']