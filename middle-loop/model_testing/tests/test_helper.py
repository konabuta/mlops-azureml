from src import helper


def test_mlops_hello_world():
    assert helper.mlops_hello_world(10) == 20
    assert helper.mlops_hello_world(15) == 24