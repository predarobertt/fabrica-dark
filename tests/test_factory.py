from fabrica_dark.factory import get_factory_info

def test_get_factory_info():
    """Check that factory indormation is returned correctly."""

    result = get_factory_info()

    assert "Fabrica Dark" in result
    assert "5 machines" in result
    assert "30 products" in result
    assert "50.0 seconds" in result