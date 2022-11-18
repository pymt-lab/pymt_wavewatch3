#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_wavewatch3").version


from .bmi import bmi_wavewatch3

__all__ = [
    "bmi_wavewatch3",
]
