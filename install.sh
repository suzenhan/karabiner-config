#!/usr/bin/env bash

cat ee6c.yml | yaml2json | jq . > ee6c.json
./update_karabiner.py --name ee6c
mv ee6c.json ~/.config/karabiner/assets/complex_modifications
