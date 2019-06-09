#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pathlib import Path

import click

karabiner_config_file = f'{Path.home()}/.config/karabiner/karabiner.json'


@click.command()
@click.option('--name', help='complex rule title', required=True)
def main(name):
    config = json.load(open(karabiner_config_file))

    complex_config = json.load(open(f'{name}.json'))
    target_profile = next((profile for profile in config['profiles'] if profile['name'] == name))
    target_profile['rules'] = complex_config['rules']

    json.dump(config, open(karabiner_config_file, 'w'), indent=2)


if __name__ == '__main__':
    main()
