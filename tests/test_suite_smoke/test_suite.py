
import unittest
from tests.test_individual.test_login import TestLogin


tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)


smoke_test = unittest.TestSuite([tc1])
unittest.TextTestRunner(verbosity=2).run(smoke_test)
