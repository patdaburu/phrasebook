#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 3/20/19 by Pat Blair
"""
.. currentmodule:: phrasebook.sql
.. moduleauthor:: Pat Blair <pblair@geo-comm.com>

SQL phrases (y'know... like queries and query fragments and such...)
"""
from pathlib import Path
from .phrasebook import Phrasebook

class SqlPhrasebook(Phrasebook):

    def __init__(self, path: str or Path):
        super().__init__(
            path=path,
            suffixes=['.sql']
        )