import pytest
from string_utils import StringUtils


class TestStringUtils:

    def setup_method(self):
        self.utils = StringUtils()

    # Тесты для capitalize

    def test_capitalize_normal(self):
        assert self.utils.capitalize("skypro") == "Skypro"

    def test_capitalize_empty_string(self):
        assert self.utils.capitalize("") == ""

    def test_capitalize_single_char(self):
        assert self.utils.capitalize("a") == "A"

    def test_capitalize_already_capitalized(self):
        assert self.utils.capitalize("Skypro") == "Skypro"

    @pytest.mark.xfail
    def test_capitalize_with_spaces(self):
        assert self.utils.capitalize("  skypro") == "  Skypro"

    def test_capitalize_numbers(self):
        assert self.utils.capitalize("123abc") == "123abc"

    def test_capitalize_mixed_case(self):
        assert self.utils.capitalize("sKyPrO") == "Skypro"

    # Тесты для trim

    def test_trim_leading_spaces(self):
        assert self.utils.trim("   skypro") == "skypro"

    def test_trim_no_spaces(self):
        assert self.utils.trim("skypro") == "skypro"

    def test_trim_empty_string(self):
        assert self.utils.trim("") == ""

    def test_trim_only_spaces(self):
        assert self.utils.trim("    ") == ""

    def test_trim_multiple_spaces(self):
        assert self.utils.trim("    sky    pro") == "sky    pro"

    def test_trim_single_space(self):
        assert self.utils.trim(" skypro") == "skypro"

    # Тесты для contains

    def test_contains_found(self):
        assert self.utils.contains("SkyPro", "S") is True

    def test_contains_not_found(self):
        assert self.utils.contains("SkyPro", "U") is False

    def test_contains_empty_symbol(self):
        assert self.utils.contains("SkyPro", "") is True

    def test_contains_empty_string(self):
        assert self.utils.contains("", "a") is False

    def test_contains_symbol_longer_than_string(self):
        assert self.utils.contains("ab", "abc") is False

    def test_contains_substring(self):
        assert self.utils.contains("Hello World", "World") is True

    def test_contains_case_sensitive(self):
        assert self.utils.contains("SkyPro", "s") is False

    # Тесты для delete_symbol

    def test_delete_symbol_single_char(self):
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_symbol_substring(self):
        assert self.utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_delete_symbol_not_found(self):
        assert self.utils.delete_symbol("SkyPro", "X") == "SkyPro"

    def test_delete_symbol_empty_symbol(self):
        assert self.utils.delete_symbol("SkyPro", "") == "SkyPro"

    def test_delete_symbol_empty_string(self):
        assert self.utils.delete_symbol("", "a") == ""

    def test_delete_symbol_all_chars(self):
        assert self.utils.delete_symbol("aaa", "a") == ""

    def test_delete_symbol_overlap(self):
        assert self.utils.delete_symbol("aaaa", "aa") == ""

    def test_delete_symbol_numbers(self):
        assert self.utils.delete_symbol("abc123def", "123") == "abcdef"
