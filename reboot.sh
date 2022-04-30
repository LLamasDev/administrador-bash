#!/bin/bash

primer_ag=$1 # Primer argumento

function funcion() {
    { # try
        limpiar_dead=$(screen -wipe) # Elimino los DEAD
        proceso_existe=$(ps -ef | grep -i $primer_ag.py | grep -iv "screen\|grep\|networkd" | wc -l) # Contador para saber si esta corriendo

        if [ $proceso_existe -eq 1 ]; then # Si el contador del proceso es 1 significa que existe
            ./stop.sh "$primer_ag"
            sleep 3
            ./start.sh "$primer_ag"
            echo ''
            sleep 5 # Paramos 5 segundos para esperar el arranque del proceso
            proceso_reinicio=$(ps -ef | grep -i $primer_ag.py | grep -iv "screen\|grep\|networkd" | wc -l) # Contador para saber si esta corriendo

            if [ $proceso_reinicio -eq 1 ]; then # Si el contador del proceso es 1 significa que se ha reiniciado
                echo "Se ha reiniciado $primer_ag correctamente."
            else # El contador de procesos no es 3 significa que no esta corriendo
                echo "No se ha reiniciado $primer_ag correctamente."
            fi
        else # El contador de procesos no es 3 significa que no esta corriendo
            echo "El proceso $primer_ag no esta corriendo, saliendo del reinicio."
        fi
    } || { # catch
        echo "Error al reiniciar el proceso $primer_ag."
    }
}

funcion