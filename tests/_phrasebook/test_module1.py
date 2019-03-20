#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import module1

def test_module():
    pb = module1.phrasebook
    print()
    print('-' * 20)
    for k, v in pb.items():
        print(f"{k} = {v.template}")