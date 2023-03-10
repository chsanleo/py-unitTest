import unittest

from distutils.version import StrictVersion
from pint.compat import HAS_NUMPY, HAS_UNCERTAINTIES, NUMPY_VER


class TestSkip(unittest.TestCase):
    def requires_numpy18(self):
        if not HAS_NUMPY:
            return unittest.skip("Requires NumPy")
        return unittest.skipUnless(StrictVersion(NUMPY_VER) >= StrictVersion("1.8"), "Requires NumPy >= 1.8")

    def requires_numpy_previous_than(version):
        if not HAS_NUMPY:
            return unittest.skip("Requires NumPy")
        return unittest.skipUnless(StrictVersion(NUMPY_VER) >= StrictVersion(version), "Requires NumPy < %s" % version)

    def requires_numpy(self):
        return unittest.skipUnless(HAS_NUMPY, "Requires NumPy")

    def requires_not_numpy(self):
        return unittest.skipIf(HAS_NUMPY, "Requires Numpy is not installed")

    def requires_uncertainties(self):
        return unittest.skipUnless(HAS_UNCERTAINTIES, "Requires uncertainties")

    def requires_not_uncertainties(self):
        return unittest.skipIf(HAS_UNCERTAINTIES, "Requires uncertainties is not installed")


if __name__ == '__main__':
    unittest.main()
