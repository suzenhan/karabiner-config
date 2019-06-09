#!/usr/bin/env bash

cat two_fn.yml | yaml2json | jq . > two_fn.json
cat two_fn_map.yml | yaml2json | jq . > two_fn_map.json
./update_karabiner.py --name two_fn --map-name two_fn_map
mv two_fn.json ~/.config/karabiner/assets/complex_modifications
mv two_fn_map.json ~/.config/karabiner/assets/complex_modifications

