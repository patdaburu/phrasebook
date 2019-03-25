#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a test module that loads a phrasebook from a `SqlPhrasebook`.
"""
from phrasebook import SqlPhrasebook

phrasebook = SqlPhrasebook().load()
