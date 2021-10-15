#!/bin/bash

primer_ag=$1 # Primer argumento

function funcion() {
  { # try
    proceso=$(ps -ef | grep -i $primer_ag.py | grep -iv "screen\|grep\|networkd" | wc -l)

    if [ $proceso -eq 1 ]; then # Si el contador del proceso es 1 significa que esta corriendo
      echo 'Proceso ya estaba arrancado, saliendo del arranque'
    else # El proceso no es 1 significa que no esta corriendo, ya que solo puede estar arrancado una vez
      ruta=$(find /bot/ -type f -name "$primer_ag*" 2>/dev/null) # Saco la ruta del archivo que siempre estan en bot
      screen_proceso=$(screen -S $primer_ag -d -m bash -c "python3 $ruta") # Ejecuto el archivo Python en una screen

      echo 'Proceso arrancado'
    fi
  } || { # catch
    echo 'Error al arrancar el proceso'
  }
}

funcion
