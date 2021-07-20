#!/usr/bin/env python3
"""Module that contains the function safely_get_value"""


from typing import Mapping, Any, TypeVar, Union


def safely_get_value(
    dct: Mapping, key: Any, default: Union[TypeVar("T"), None] = None
                    ) -> Union[Any, TypeVar("T")]:

    """Funtion to get a safely value

    Returns:
        [Union]: [Any or TypeVar]
    """
    if key in dct:
        return dct[key]
    else:
        return default
