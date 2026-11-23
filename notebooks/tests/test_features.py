from pandas.testing import assert_series_equal

from animal_shelter.features import (
    _check_has_name,
    _check_is_dog,
    _compute_days_upon_outcome,
    _get_hair_type,
    _get_neutered,
    _get_sex,
)


def test_check_has_name() -> None:
    import pandas as pd

    s = pd.Series(["Ivo", "Henk", "unknown"])
    result = _check_has_name(s)
    expected = [True, True, False]
    assert_series_equal(result, pd.Series(expected))


def test_check_is_dog() -> None:
    import pandas as pd

    s = pd.Series(["dog", "cat"])
    result = _check_is_dog(s)
    expected = [True, False]
    assert_series_equal(result, pd.Series(expected))


def test_get_sex() -> None:
    import pandas as pd

    s = pd.Series(["Neutered Male", "Spayed Female", "Unknown"])
    result = _get_sex(s)
    expected = ["male", "female", "unknown"]
    assert_series_equal(result, pd.Series(expected))


def test_get_neutered() -> None:
    import pandas as pd

    s = pd.Series(["Neutered Male", "Spayed Female", "Intact Male", "Unknown"])
    result = _get_neutered(s)
    expected = ["fixed", "fixed", "intact", "unknown"]
    assert_series_equal(result, pd.Series(expected))


def test_get_hair_type() -> None:
    import pandas as pd

    s = pd.Series(["Shorthair", "Medium Hair", "Longhair", "Unknown"])
    result = _get_hair_type(s)
    expected = ["shorthair", "medium hair", "longhair", "unknown"]
    assert_series_equal(result, pd.Series(expected))


def test_compute_days_upon_outcome() -> None:
    import pandas as pd

    s = pd.Series(["2 days", "3 weeks", "1 month", "1 year", "Unknown"])
    result = _compute_days_upon_outcome(s)
    expected = [2, 21, 30, 365, None]
    assert_series_equal(result, pd.Series(expected))
