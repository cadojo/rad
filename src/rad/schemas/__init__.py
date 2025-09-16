"""Schemas for resume data.

More documentation is en route!
"""

import jsonschema
import typing

Schema: typing.TypeAlias = dict[str, "str | list[str] | Schema"]


def experience() -> Schema:
    """Work experience.

    More documentation en route!
    """
    return {
        "type": "object",
        "properties": {
            "organization": {"type": "string"},
            "start": {"type": "date"},
            "stop": {"type": ["string", "null"], "format": "date", "default": "null"},
            "notes": {"type": "array", "items": {"type": "string"}},
            "title": {"type": "string"},
        },
    }


def project() -> Schema:
    """A project you made.

    More documentation en route!
    """
    return {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "description": {"type": "string"},
            "url": {"type": "string", "format": "uri", "pattern": "^(https?|http?)://"},
            "notes": {"type": "array", "items": {"type": "string"}},
        },
    }
