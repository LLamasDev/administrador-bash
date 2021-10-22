#!/bin/bash

function funcion() {
  { # try
    ./stop.sh 'supercell'
    echo ''
    ./stop.sh 'clashroyale'
    echo''
    ./stop.sh 'clashofclans'
    echo''
    sleep 10 # Paramos 10 segundos para esperar la parada del proceso

    proceso=$(ps -ef | grep -i "supercell\|clashroyale\|clashofclans" | grep -iv "screen\|grep\|networkd" | wc -l)

    if [ $proceso -eq 0 ]; then # Si el contador del proceso es 0 significa que no estan corriendo los procesos
      echo 'Parado todos los procesos correctamente.'
    else # El contador de procesos no es 0 significa que no han parado todos los procesos
      echo "No se ha parado todos los procesos correctamente."
    fi
  } || { # catch
    echo 'Error al arrancar los procesos.'
  }
}

funcion
