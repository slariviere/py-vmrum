#!/bin/bash

# Create symlinks in $HOME/bin to all python script in the current directory with the extention truncated

for file in $(ls -1 *.py); do
    dest_filename=$(echo $file | sed 's/.py$//')
    current_dir=$(pwd)
    # If the symlik exist, we rplace it
    if [ -h ${HOME}/bin/${dest_filename} ]; then
        $(rm ${HOME}/bin/${dest_filename})
    fi
    $(ln -s ${current_dir}/${file} ${HOME}/bin/${dest_filename});
done
