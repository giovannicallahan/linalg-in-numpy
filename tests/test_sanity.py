import numpy as np

def test_identity_leaves_vector_unchanged():
    v = np.array([1.0, 2.0, 3.0])
    assert np.allclose(np.eye(3) @ v, v)