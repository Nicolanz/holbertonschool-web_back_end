#!/usr/bin/env python3
"""first element of a sequence annotated"""


from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first element of a list

    Args:
        lst (Sequence[Any]): [list]

    Returns:
        Union[Any, None]: [First element or None of not exits]
    """
    if lst:
        return lst[0]
    else:
        return None
