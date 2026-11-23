"""Tests for the features module."""

import pandas as pd
import pytest
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
    """Tests for _check_has_name function."""
    s = pd.Series(["Ivo", "Henk", "unknown"])
    result = _check_has_name(s)
    expected = [True, True, False]
    assert_series_equal(result, pd.Series(expected))


def test_check_is_dog() -> None:
    """Tests for _check_is_dog function."""
    import pandas as pd

    s = pd.Series(["dog", "cat"])
    result = _check_is_dog(s)
    expected = [True, False]
    assert_series_equal(result, pd.Series(expected))


def test_check_is_dog_rejects_invalid_animal_type() -> None:
    """Tests that _check_is_dog raises an error for invalid animal types."""
    import pandas as pd

    animal_types = pd.Series(["eagle", "rabbit"])

    with pytest.raises(
        RuntimeError,
        match="Found pets that are not dogs or cats",
    ):
        _check_is_dog(animal_types)


@pytest.fixture(scope="class")
def list_of_sex() -> pd.Series[str]:
    """Fixture providing a list of sex strings."""
    return pd.Series(["Neutered Male", "Spayed Female", "Intact Male", "Unknown"])


class TestSexBasedFeatures:
    """Tests for sex-based feature functions."""

    def test_get_sex(self, list_of_sex) -> None:
        """Tests for _get_sex function."""
        result = _get_sex(list_of_sex)
        expected = ["male", "female", "male", "unknown"]
        assert_series_equal(result, pd.Series(expected))

    def test_get_neutered(self, list_of_sex) -> None:
        """Tests for _get_neutered function."""
        result = _get_neutered(list_of_sex)
        expected = ["fixed", "fixed", "intact", "unknown"]
        assert_series_equal(result, pd.Series(expected))


def test_get_hair_type() -> None:
    """Tests for _get_hair_type function."""
    s = pd.Series(["Shorthair", "Medium Hair", "Longhair", "Unknown"])
    result = _get_hair_type(s)
    expected = ["shorthair", "medium hair", "longhair", "unknown"]
    assert_series_equal(result, pd.Series(expected))


def test_compute_days_upon_outcome() -> None:
    """Tests for _compute_days_upon_outcome function."""
    s = pd.Series(["2 days", "3 weeks", "1 month", "1 year", "Unknown"])
    result = _compute_days_upon_outcome(s)
    expected = [2, 21, 30, 365, None]
    assert_series_equal(result, pd.Series(expected))
