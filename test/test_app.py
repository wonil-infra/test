from app import msg

def test_msg_contains_jenkins():
    assert "Jenkins" in msg()

