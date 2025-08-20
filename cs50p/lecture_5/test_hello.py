from hello import hello


def test_default_name():
    assert hello() == "Hello, World!"


def test_suguments():
    for name in ["Alice", "Bob", "Charlie"]:
        assert hello(name) == f"Hello, {name}!"
