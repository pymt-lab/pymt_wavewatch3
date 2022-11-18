from __future__ import absolute_import

import pkg_resources
from bmi_wavewatch3 import BmiWaveWatch3 as bmi_wavewatch3

bmi_wavewatch3.__name__ = "bmi_wavewatch3"
bmi_wavewatch3.METADATA = pkg_resources.resource_filename(
    __name__, "data/bmi_wavewatch3"
)

__all__ = [
    "bmi_wavewatch3",
]
