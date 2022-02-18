from foo import foo


def test_foo():
    assert foo() == "foo"


def test_foo_uppercase():
    assert foo(True) == "FOO"
