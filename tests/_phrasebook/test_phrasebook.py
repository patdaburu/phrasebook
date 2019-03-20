#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import module2

def test_module2():
    pb = module2.phrasebook
    print()
    print('-' * 20)
    for k, v in pb.items():
        print(f"{k} = {v.template}")