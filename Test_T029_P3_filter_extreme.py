from Cimpl import *
from T029_P3_filter_extreme import extreme_contrast
from unit_testing import check_equal

def test_extreme_contrast() -> None:
    check_equal('extreme_contrast',extreme_contrast(0),new_low)
    check_equal('extreme_contrast',extreme_contrast(130),new_high)
    return pict.copy()
test_extreme_contrast()
