import json
from pathlib import Path
import unittest

class Evidence(unittest.TestCase):
    def test_promoted_claims_need_sources(self):
        ledger=json.loads((Path(__file__).parents[1]/'evidence/claims.json').read_text())
        for claim in ledger['claims']:
            self.assertIn(claim['status'], ['proposed','supported','rejected'])
            if claim['status']=='supported':
                self.assertTrue(claim.get('run_manifest'))
                self.assertTrue(claim.get('figure_or_table'))
                self.assertTrue(claim.get('limitations'))
