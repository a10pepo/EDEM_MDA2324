""" Reto 1
Una tienda vende Discos de música (unos muñecos muy graciosos). Con la idea de vender un stock
almacenado durante meses, se decide que discos de género "Black Metal" y "Electro" tienen 
un descuento del 30%.

Cada disco (usa un diccionario para esto) tendrá:

Nombre
Artista
Año
Precio
Género (solo pueden ser de los siguientes)
Pop
Electro
Reggaeton
Rock
Metal
Death Metal
Black Metal
Escribe un programa que, disponiendo de una lista de discos
disponibles en la tienda el usuario pueda elegir el disco a comprar.

Al acabar la compra (pulsando la tecla 0) se deberá mostrar el ticket de compra indicando
la fecha de compra (puedes coger la fecha actual a través de datetime), el dinero que se 
ahorra el usuario y el coste final de la compra."""


from tienda import listaDiscos

from funcionlistarDiscosTienda import listarDiscosTienda

from funcionpedidoCompra import pedidoCompra

from funcionTicketCompra import ticketCompra

miCompra=ticketCompra()
