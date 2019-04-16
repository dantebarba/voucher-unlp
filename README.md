# Voucher UNLP [![Build Status](https://travis-ci.org/dantebarba/voucher-unlp.svg?branch=master)](https://travis-ci.org/dantebarba/voucher-unlp)

Este módulo en Python permite recuperar un Voucher válido para la conexión Wifi de la Facultad de Informática, UNLP. Esta compuesto de un html-parser que recupera el voucher de la página web de La Fuente (actualmente el único proveedor disponible) y de una API que expone el voucher. 

## Instalacion

1. Requiere Python 2.7. 
2. Instalamos el archivo `requirements.txt` utilizando pip:

```bash
$ pip install -r requierements.txt
$ python src/voucher_api.py
```

## Api endpoints

```http
- GET /voucher?url={url} url: Url de la pagina de La Fuente 
  Response: 200 OK 
  Content: voucher
```

## Docker

```bash
docker run -p 5000:5000 dantebarba/voucher-unlp:latest
```