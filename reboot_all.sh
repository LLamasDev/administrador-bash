#!/bin/bash

function funcion() {
  { # try
    ./reboot.sh 'supercell'
    echo''
    ./reboot.sh 'clashroyale'
    echo''
    ./reboot.sh 'clashofclans'
    echo''

    proceso=$(ps -ef | grep -i "supercell\|clashroyale\|clashofclans" | grep -iv "screen\|grep\|networkd" | wc -l)

    if [ $proceso -eq 3 ]; then # Si el contador del proceso es 3 significa que estan corriendo los procesos
      echo 'Reiniciado todos los procesos correctamente.'
    else # El contador de procesos no es 3 significa que no esta corriendo
      echo "No se han reiniciado todos los procesos correctamente."
    fi
  } || { # catch
    echo 'Error al reiniciar los procesos.'
  }
}

funcion
