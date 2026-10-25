import numpy as np

def fused_distance(ld, rd, w_l=0.7, w_r=0.3):
    if np.isnan(ld) and np.isnan(rd): return np.nan
    if np.isnan(ld): return rd
    if np.isnan(rd): return ld
    return w_l * ld + w_r * rd

def test_fused_distance():
    assert fused_distance(10, 20) == 13.0
    assert fused_distance(np.nan, 20) == 20
    assert fused_distance(10, np.nan) == 10
    assert np.isnan(fused_distance(np.nan, np.nan))