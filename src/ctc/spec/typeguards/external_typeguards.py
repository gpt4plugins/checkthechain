from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    import pandas

    from typing_extensions import TypeGuard

    from .. import typedefs


def is_dataframe(
    candidate: typing.Any,
) -> TypeGuard['pandas.core.frame.DataFrame']:
    import pandas as pd

    return isinstance(candidate, pd.DataFrame)


def is_int(value: typing.Any) -> TypeGuard['typedefs.Integer']:
    return isinstance(value, int) or type(value).__name__ in (
        'int8',
        'int16',
        'int32',
        'int64',
    )


def is_float(value: typing.Any) -> TypeGuard['typedefs.Float']:
    return isinstance(value, float) or type(value).__name__ in (
        'float16',
        'float32',
        'float64',
        'float128',
    )


def is_number(value: typing.Any) -> TypeGuard['typedefs.Number']:
    return is_int(value) or is_float(value)
