import pytest
from helixlang.types import DNA, RNA, Protein, BioTypeError
from helixlang.morphisms import transcribe, translate

def test_type_enforcement():
    with pytest.raises(BioTypeError):
        DNA("ATGZ")  # Z is invalid

def test_central_dogma():
    d = DNA("ATGTGATAA")
    r = transcribe(d)
    p = translate(r, table_id=1)
    assert p.seq == "MC*"
