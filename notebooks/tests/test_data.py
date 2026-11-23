"""Tests for the data module."""

from animal_shelter import data


def test_convert_camel_case() -> None:
    """Tests for convert_camel_case function."""
    assert data.convert_camel_case("CamelCase") == "camel_case"
    assert data.convert_camel_case("CamelCASE") == "camel_case"
    assert data.convert_camel_case("camel-case") != "camel_case"
    assert data.convert_camel_case("camel case") == "camel case"
    assert data.convert_camel_case("camel_case") == "camel_case"
    assert data.convert_camel_case("Camel_Case") == "camel__case"
    assert data.convert_camel_case("camelCase") == "camel_case"
