import pytest
from definition_a4c7590aa503431fb719269077118ded import add_category


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup: Clear or reset internal category list before each test if needed
    # Assuming there's a way to clear categories, e.g., a function or attribute
    # This is a placeholder; user must implement reset functionality in definition_a4c7590aa503431fb719269077118ded
    try:
        from definition_a4c7590aa503431fb719269077118ded import reset_categories
        reset_categories()
    except ImportError:
        pass
    yield
    # Teardown: same as setup for idempotence
    try:
        from definition_a4c7590aa503431fb719269077118ded import reset_categories
        reset_categories()
    except ImportError:
        pass


@pytest.mark.parametrize("input_category", [
    "Groceries",
    "Rent",
    "Entertainment",
    "Utilities",
    "Education",
    # Edge cases:
    "",                        # Empty string may be invalid input
    "  ",                      # Whitespace only
    "Travel & Leisure",         # String with special chars
    "LongCategoryName" * 50,   # Very long string
    "123",                     # Numeric string
    "Budget_Category_1",       # Alphanumeric with underscore
    "Café",                    # Unicode characters
    "\nNewline",               # Contains newline
    "Tab\tCategory",           # Contains tab
    None,                      # NoneType input
    12345,                     # Numeric input
    [],                        # List input
    {},                        # Dict input
    True,                      # Boolean input
])
def test_add_category(input_category):
    if isinstance(input_category, str) and input_category.strip():
        # Valid category names (non-empty after stripping)
        try:
            result = add_category(input_category)
            # Function returns None on success
            assert result is None
        except Exception as e:
            pytest.fail(f"Unexpected exception raised for valid input '{input_category}': {e}")
    else:
        # Invalid inputs expected to raise an Exception
        with pytest.raises(Exception):
            add_category(input_category)


def test_duplicate_category_handling():
    # Assuming duplicate categories are not allowed and raises an exception
    category = "Health"
    # First addition should succeed
    add_category(category)
    # Adding the same category again - behavior depends on implementation
    # It may raise an exception or silently ignore
    try:
        add_category(category)
    except Exception:
        pass  # Acceptable behavior if duplicates raise exception
    else:
        # If no exception, test that duplicates are not added twice if possible to check
        pass  # Cannot assert internal state due to no access


def test_whitespace_category():
    # Categories with only whitespace should be rejected
    with pytest.raises(Exception):
        add_category("    ")


def test_category_with_leading_trailing_spaces():
    # Should either trim and add or raise exception
    input_cat = "  Travel  "
    try:
        result = add_category(input_cat)
        assert result is None
    except Exception:
        pass


def test_category_none_input():
    with pytest.raises(Exception):
        add_category(None)


def test_category_numeric_input():
    with pytest.raises(Exception):
        add_category(123)


def test_category_empty_string():
    with pytest.raises(Exception):
        add_category("")


def test_category_special_characters():
    special_cats = ["!@#$%", "^&*()_+", "`~", "cat@123"]
    for cat in special_cats:
        try:
            result = add_category(cat)
            assert result is None
        except Exception:
            pytest.fail(f"Unexpected exception raised for input '{cat}'")


def test_category_unicode_characters():
    unicode_cats = ["Café", "北京", "naïve", "😀category"]
    for cat in unicode_cats:
        try:
            result = add_category(cat)
            assert result is None
        except Exception:
            pytest.fail(f"Unexpected exception raised for unicode input '{cat}'")

