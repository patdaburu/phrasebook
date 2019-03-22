#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from .modules import (
    module1,
    module2,
    module3,
    module4,
    module5,
    module6
)


@pytest.mark.parametrize(
    'phrasebook,name,expectations',
    [
        (
            module1.phrasebook,
            'module 1 phrasebook',
            {
                'txt1': 'Hello, $NAME.'
            }
        ),
        (
            module2.phrasebook,
            'module 2 phrasebook',
            {
                'txt1': 'Hello, $NAME.'
            }
        ),
        (
            module3.phrasebook,
            'module 3 phrasebook',
            {
                'txt1': 'Hello, $NAME.',
                'txt2': None
            }
        ),
        (
            module4.phrasebook,
            "module 4 ('.sql' suffix) phrasebook",
            {
                'query1': 'SELECT $COLUMN_1 FROM $TABLE'
            }
        ),
        (
            module5.phrasebook,
            "module 5 ('.sql' suffix) phrasebook",
            {
                'query1': 'SELECT $COLUMN_1 FROM $TABLE'
            }
        ),
        (
            module6.phrasebook,
            'module 6 (SqlPhrasebook) phrasebook',
            {
                'query1': 'SELECT $COLUMN_1 FROM $TABLE',
                'query2': 'SELECT $COLUMN_1 FROM $TABLE WHERE $COLUMN_1 = $VALUE'
            }
        )
    ]
)
def test_phrasebook_expect(phrasebook, name, expectations):
    """
    Arrange/Act: Retrieve a phrasebook from one of the test modules.
    Assert: The phrasebook contains the expected values.

    :param phrasebook: the phrasebook instance
    :param name: a name for the phrasebook (to include in `assert` messages)
    :param expectations: a dictionary of values we expect to find in the
        phrasebook
    """
    for k, v in expectations.items():
        assert phrasebook.gets(k) == v, (
            f"The value of {k} in '{name}' should be {v}."
        )
