#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a test module that loads a phrasebook from a `.sql` file.
"""
from phrasebook import Phrasebook

phrasebook = Phrasebook(suffixes=['.sql']).load()
