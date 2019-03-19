#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 3/19/19 by Pat Blair
"""
.. currentmodule:: phrasebook.phrasebook
.. moduleauthor:: Pat Blair <pblair@geo-comm.com>

Store phrases (SQL, messages, what-have-you) alongside your modules.
"""
from pathlib import Path
from string import Template
from typing import Dict, Iterable, Tuple


PHRASES_SUFFIX = '.phr'  #: the standard suffix for phrasebook directories


# TODO: Read https://www.thoughtco.com/pythons-string-templates-2813675

class Phrasebook:

    def __init__(
            self,
            path: str or Path,
            suffixes: Iterable[str]
    ):
        """

        :param path: the path to the phrases directory, or a file that has an
            accompanying phrasebook directory
        :param suffixes: the suffixes of phrase files

        .. seealso::

            `Python's String Templates <https://bit.ly/2FdnQ61>`_
        """
        # Let's figure out where the phrases are kept.
        self._path: Path = (
            path if isinstance(dir, Path) else Path(path)
        ).expanduser().resolve()  #: the path to the phrases directory
        # If the path is the path to an existing file...
        if self._path.is_file():
            # ...assume we are actually looking for a directory in the same
            # location
            self._path = (
                    self._path.parent + self._path.stem
            ).with_suffix(PHRASES_SUFFIX)

        # We should also keep track of the file suffixes we expect to find.
        self._suffixes: Tuple[str] = tuple(
            s if s.startswith('.') else f".{s}"
            for s in (
                suffixes if suffixes else []
            ) if s
        )

        self._phrases: Dict[str, Template] = {}  #: the phrase templates

    @property
    def path(self) -> Path:
        """
        Get the path to the phrases directory.
        """
        return self._path

    @property
    def suffixes(self) -> Tuple[str]:
        """
        Get the recognized suffixes for phrase files.
        """
        return self._suffixes

    def _load(self, path: Path, prefix: str = ''):
        """
        Recursively load

        :param path: the directory path to load
        :param prefix: the prefix to prepend to all the phrase keys in the
            phrase dictionary
        """
        # Go through all the items in the path.
        for sub in path.iterdir():
            # If this item is a directory, append its name to the current
            # prefix and load it recursively.
            if sub.is_dir():
                self._load(sub, prefix=f"{prefix}{sub.name}.")
            elif (
                    sub.is_file()
                    and not self._suffixes or sub.suffix in self.suffixes
            ):
                # Otherwise, if it's a file and we either have no preference
                # for suffixes, or it's suffix is one we recognize, create a
                # template for it and place it into the dictionary of phrases.
                self._phrases[f"{prefix}sub.stem"] = Template(sub.read_text())

    def load(self) -> 'Phrasebook':
        """
        Load the phrases.

        :return: this instance
        """
        self._load(self._path)
        return self

    def substitute(
            self,
            phrase: str,
            default: str or Template = None,
            safe: bool = True,
            **kwargs
    ) -> str or None:
        """
        Perform substitutions on a phrase template and return the result.

        :param phrase: the phrase
        :param default: a default template
        :param safe: `True` (the default) to leave the original placeholder in
            the template in place if no matching keyword is found
        :param kwargs: the substitution arguments
        :return: the substitution result
        """
        template = self.get(
            phrase=phrase,
            default=default
        )
        if not template:
            return None
        return (
            template.safe_substitute(**kwargs) if safe
            else template.substitute(**kwargs)
        )

    def get(self, phrase: str, default: str or Template = None) -> Template:
        """
        Get a phrase template.

        :param phrase: the name of the phrase template
        :param default: a default template or string
        :return: the template (or the default)
        :raises KeyError: if the phrase does not exist and the caller does not
            provide a default

        .. seealso::

            :py:func:`gets`
        """
        try:
            return self._phrases[phrase]
        except KeyError:
            # If we were supplied with a default...
            if default:
                # ...return that.
                return (
                    default if isinstance(default, Template)
                    else Template(default)
                )
            else:
                raise  # Otherwise, we just pass along the exception.

    def gets(self, phrase: str, default: str or Template):
        """
        Get a phrase template string.

        :param phrase: the name of the phrase template
        :param default: a default template or string
        :return: the template (or the default)
        :raises KeyError: if the phrase does not exist and the caller does not
            provide a default
        """
        try:
            # See if the `get` method can give us a `Template` from which we
            # may derive a string.
            return self.get(phrase=phrase, default=default).template
        except KeyError:
            # If we got a `KeyError` (because the phrase wan't found) or an
            # `AttributeError` (likely because the phrase is found but it's
            # value is `None`), we may be able to revert to the default.
            if default is not None:
                return (
                    default.template if isinstance(default, Template)
                    else default
                )
            # Otherwise, raise the exception.
            raise
