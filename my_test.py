from my_code import sleep_in


def test_sleep_in():
    assert True == sleep_in(False, False)
    assert False == sleep_in(True, False)
    assert True == sleep_in(False, True)
    assert True == sleep_in(True, True)