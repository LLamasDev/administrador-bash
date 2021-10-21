#!/bin/bash

primer_ag=$1 # Primer argumento

function funcion() {
  { # try
    ./stop.sh "$primer_ag"
    ./start.sh "$primer_ag"

    echo "Se ha reiniciado $primer_ag correctamente."
  } || { # catch
    echo "Error al reiniciar el proceso $primer_ag."
  }
}

funcion
