
import unittest
from tests.test_individual.test_cart import TestCart
from tests.test_individual.test_compare import TestCompare
from tests.test_individual.test_sort_by import TestSortBy
from tests.test_individual.test_verify_price_different_view import TestVerifyPriceDifferentView
from tests.test_individual.test_registration import TestRegistration

tc1 = unittest.TestLoader().loadTestsFromModule(TestCart)
tc2 = unittest.TestLoader().loadTestsFromModule(TestCompare)
tc3 = unittest.TestLoader().loadTestsFromModule(TestSortBy)
tc4 = unittest.TestLoader().loadTestsFromModule(TestVerifyPriceDifferentView)
tc5 = unittest.TestLoader().loadTestsFromModule(TestRegistration)


smoke_test = unittest.TestSuite([tc1,tc2,tc3,tc4,tc5])
unittest.TextTestRunner(verbosity=2).run(smoke_test)
