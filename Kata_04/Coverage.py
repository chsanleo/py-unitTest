import coverage
import unittest
import TestCalcular

suite = unittest.TestLoader().loadTestsFromModule(TestCalcular)

cov = coverage.Coverage()
cov.start()

unittest.TextTestRunner().run(suite)

cov.stop()
cov.save()

cov.html_report(directory='covhtml')
