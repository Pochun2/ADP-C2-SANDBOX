import unittest
from sandboxlib import seed_contract as c


class SandboxBoundaryTests(unittest.TestCase):
    def test_project_id(self): self.assertEqual(c.PROJECT_ID, "ADP_C2_SANDBOX")
    def test_broker_denied(self): self.assertIs(c.BROKER_ACCESS, False)
    def test_order_denied(self): self.assertIs(c.ACCOUNT_ORDER_ACCESS, False)
    def test_scheduler_denied(self): self.assertIs(c.SCHEDULER_ACTIVE, False)
    def test_issuer_denied(self): self.assertIs(c.ISSUER_DEPLOYED, False)
