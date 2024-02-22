ESTUDIO JUGADORES CALL OF DUTY: MULTIPLAYER
Vamos a centrar nuestro análisis en el videojuego Call of Duty y en su modo de juego: multiplayer.

El objetivo de este estudio es conocer los mejores jugadores en función de una puntuación que dependa de kills y asistencias.
Además conocer la relación entre las muertes y las wins.

En este caso hacemos una serie de ejercicios previos para poner en práctica lo aprendido:
- Leer dos csv diferentes.
- Crear y visualizar DF a partir de los csv.
- Seleccionar columnas.
- Combinar campos y sumarlos en un nuevo campo 'total'.
- Ordenar en función del campo combinado.
- Cambiar el formato de los campos.
- Obtener totales y medias.
- Calcular la correlación entre campos determinados.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

Documentación

Disponemos de un CSV original en el que conocemos la información de los jugadores siguiente:

name: nombre del jugador
wins : número de victorias en todas sus partidas
kills : número de muertes en todas sus partidas
kdRatio : kill/deaths ratio
killstreak : racha de muertes
level : nivel
losses : número total de derrotas
prestige: modo especial que los jugadores pueden decidir si activar o no
hits : número de veces que un jugador ha alcanzado a otro
timePlayed : tiempo de juego en horas
headshots : número de tiros en la cabeza
averageTime : tiempo de juego medio
gamesPlayed : número de partidas jugadas por jugador
assists : asistencias
misses : número de veces que un jugador falla un disparo
xp : puntos de experiencia
scorePerMinute : puntos conseguidos por minuto
shots : número de disparos de cada jugador
deaths : número de veces que ha muerto un jugador
Tenemos un CSV original con 1558 jugadores:

Como los nombres de usuario son un poco extraños,
le hemos cambiado el nombre de usuario para que cada jugador tenga el nombre Jugador_XX donde 'XX' es el número jugador.
Por ejemplo, Jugador_01
Dos archivos .csv

Hemos separado el CSV en dos csv independientes para poder poner en práctica lo aprendido
y "jugar" con dos fuentes de datos diferentes pero la información 'name' en común.

COD1.csv con la siguiente información:
name: nombre del jugador
wins : número de victorias en todas sus partidas
kills : número de muertes en todas sus partidas
kdRatio : kill/deaths ratio
killstreak : racha de muertes
level : nivel
losses : número total de derrotas
prestige: modo especial que los jugadores pueden decidir si activar o no

COD2.csv con la siguiente información:
name: nombre del jugador
hits : número de veces que un jugador ha alcanzado a otro
timePlayed : tiempo de juego en horas
headshots : número de tiros en la cabeza
averageTime : tiempo de juego medio
gamesPlayed : número de partidas jugadas por jugador
assists : asistencias
misses : número de veces que un jugador falla un disparo
xp : puntos de experiencia
scorePerMinute : puntos conseguidos por minuto
shots : número de disparos de cada jugador
deaths : número de veces que ha muerto un jugador

