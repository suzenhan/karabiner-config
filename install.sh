#!/usr/bin/env bash

yaml2json two_fn.yml | jq . > two_fn.json
yaml2json two_fn_map.yml| jq . > two_fn_map.json
./update_karabiner.py --name two_fn --map-name two_fn_map
mv two_fn.json ~/.config/karabiner/assets/complex_modifications
mv two_fn_map.json ~/.config/karabiner/assets/complex_modifications

