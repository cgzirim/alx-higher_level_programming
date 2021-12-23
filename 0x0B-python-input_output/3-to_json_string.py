#!/usr/bin/python3
"""Defines a function that returns an object represented in JSON string."""
import json


def to_json_string(my_obj):
    """Returns an object represented by a JSON string."""

    return (json.dumps(my_obj))
