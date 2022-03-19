import requests

try:
    data = requests.get('http://192.168.12.104:7080/document/simbolo/api/v1.0/buscar?dni=99999999')
    codigo = data.status_code  # se almacena el codigo 200 (OK) en la variable CODIGO
    myData = data.json()  #aca se almacena la informacion si la API te devuelve algo

    if (myData is None): #si la API responde, pero no te devuelve datos (o sea que anda mal)
        print('No existe un CUD asociado al DNI 99999999')
    else: # si la API te devuelve datos
        print(myData)

# si la API no se encuentra disponible o no responde, lo captura el except
except:
    codigo = data.status_code   # se almacena el codigo 404 (ERROR) en la variable CODIGO
    print('la api no se encuentra disponible')