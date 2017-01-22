#!/bin/bash
# -*- ENCODING: UTF-8 -*-
#echo " Linux es lo mejor"
#exit

echo "b)------------------------------------------------------"
##################################################################
#pushd linux/
#for f in *; do [ -d ./"$f" ] && find ./"$f" -maxdepth 1 -exec echo \; | wc -l && echo $f; done
#popd
find linux/ -maxdepth 1 -mindepth 1 -type d | while read dir; do
  printf "%-25.25s : " "$dir"
  find "$dir" -type f | wc -l
done
echo "c)------------------------------------------------------"
#################################################################

echo "Number of README:" $(find linux/ -name "README" | wc -l)
echo "Number of Kconfig files:" $(find linux/ -name "Kconfig" | wc -l)
echo "Number of Kbuild files:" $(find linux/ -name "Kbuild" | wc -l)
echo "Number of Makefiles files:" $(find linux/ -name "Makefile" | wc -l)
echo "Number of .c files:" $(find linux/ -name "*.c" | wc -l)
echo "Number of .h files:" $(find linux/ -name "*.h" | wc -l)
echo "Number of .pl files" $(find linux/ -name "*.pl" | wc -l)

echo "d)------------------------------------------------------"
################################################################
echo "Number of times the include <linux/module.h> appears =" $(grep -R '#include <linux/module.h>' linux/ | wc -l)

echo "e)------------------------------------------------------"
################################################################
$(mkdir -p 'C_FILES')
$(mkdir -p 'H_FILES')

find linux/ -name \*.c -exec cp {} C_FILES/ \;
find linux/ -name \*.h -exec cp {} H_FILES/ \;

echo "f)------------------------------------------------------"
################################################################
echo "Number of .c files in C_FILES:" $(find C_FILES/ -name "*.c*" | wc -l)
echo "Number of .h files in H_FILES:" $(find H_FILES/ -name "*.h*" | wc -l)
