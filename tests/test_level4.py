import pytest

from phytoClassifier.level4 import getClassBySmiles


def test_getClassBySmiles():
    cls = "CC(=O)OCC[N+](C)(C)C"
    print(getClassBySmiles(cls))
    assert getClassBySmiles(cls) == "haha"
