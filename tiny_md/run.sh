#!/bin/bash

ROOT="${MESON_SOURCE_ROOT}"
cd "$ROOT"

LS=$(ls .)

MAIN=$1

for target in $LS
do
  if [ -d "$target" ] && [[  "$target" == t_*  ]];
  then
    echo "@ Compiling $target"
    cd "$target"
    meson compile > /dev/null 2>&1
    if [ "$?" -ne 0 ];
      then 
        echo "@ Compilation failed"
        exit 1
      else
        echo "@ Compilated succesfully"
    fi
    cd ..
  fi
done

for target in $LS
do
  if [ -d "$target" ] && [[  "$target" == t_*  ]];
  then
    echo "@ Running $target"
    echo ""
    cd "$target"
    if [ -z "$MAIN" ];
      then
        echo "Empty."
        ./tiny_md
      else
        echo "Not empty."
        $MAIN
    fi
    if [ "$?" -ne 0 ];
      then 
        echo "@ Program exited with result not 0."
        exit 1
    fi
    cd ..
  fi
done