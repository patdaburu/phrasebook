#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from .modules import module1, module2, module3


@pytest.mark.parametrize(
    'phrasebook, name, expectations',
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
    ]
)
def test_phrasebook_expect(phrasebook, name, expectations):
    """
    Arrange/Act: Retrieve a phrasebook from one of the test modules.
    Assert: The phrasebook contains the expected values.

    :param phrasebook:
    :param name:
    :param expectations:
    :return:
    """
    for k, v in expectations.items():
        assert phrasebook.gets(k) == v, (
            f"The value of {k} in '{name}' should be {v}."
        )
