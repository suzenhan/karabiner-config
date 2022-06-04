#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pathlib import Path

from mando import command, main

karabiner_config_file = f'{Path.home()}/.config/karabiner/karabiner.json'


@command
def main(name, map_name):
    config = json.load(open(karabiner_config_file))

    complex_config = json.load(open(f'{name}.json'))
    target_profile = next((profile for profile in config['profiles'] if profile['name'] == name))
    map_config = json.load(open(f'{map_name}.json'))
    target_profile['rules'] = map_config['rules'] + complex_config['rules']
    json.dump(config, open(karabiner_config_file, 'w'), indent=2)


