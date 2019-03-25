#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a test module that loads a phrasebook from `.txt` files in a directory.
"""
from phrasebook import Phrasebook

phrasebook = Phrasebook(suffixes=('.txt',)).load()
