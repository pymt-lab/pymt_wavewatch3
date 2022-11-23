from __future__ import absolute_import

import pkg_resources
from bmi_wavewatch3 import BmiWaveWatch3 as WaveWatch3

WaveWatch3.__name__ = "WaveWatch3"
WaveWatch3.METADATA = pkg_resources.resource_filename(__name__, "data/WaveWatch3")

__all__ = [
    "WaveWatch3",
]
