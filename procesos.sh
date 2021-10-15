#!/bin/bash

primer_ag=$1 # Primer argumento

function funcion() {
  { # try
    proceso=$(ps -ef | grep -i $primer_ag.py | grep -iv "screen\|grep\|networkd" | wc -l)

    if [ $proceso -eq 1 ]; then # Si el contador del proceso es 1 significa que esta corriendo
      echo 'El proceso esta corriendo'
    else # El proceso no es 1 significa que no esta corriendo, ya que solo puede estar arrancado una vez
      echo 'El proceso no esta corriendo'
    fi
  } || { # catch
    echo 'El proceso esta en estado anomalo'
  }
}

funcion
