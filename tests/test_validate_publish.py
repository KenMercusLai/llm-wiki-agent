from __future__ import annotations

import unittest
from unittest import mock

from tools import validate_publish


class ValidatePublishTest(unittest.TestCase):
    @mock.patch("tools.validate_publish.synthesis.validate_repository")
    @mock.patch("tools.validate_publish.validate_identities.main", return_value=1)
    def test_stops_after_identity_failure(self, identity_main, synthesis_validate):
        self.assertEqual(1, validate_publish.main([]))
        synthesis_validate.assert_not_called()

    @mock.patch("tools.validate_publish.synthesis.validate_repository", return_value={"topic_count": 8})
    @mock.patch("tools.validate_publish.validate_identities.main", return_value=0)
    def test_runs_identity_and_synthesis_checks(self, identity_main, synthesis_validate):
        self.assertEqual(0, validate_publish.main([]))
        synthesis_validate.assert_called_once()

    @mock.patch("tools.validate_publish.synthesis.validate_repository", side_effect=ValueError("bad manifest"))
    @mock.patch("tools.validate_publish.validate_identities.main", return_value=0)
    def test_synthesis_failure_is_fail_closed(self, identity_main, synthesis_validate):
        self.assertEqual(1, validate_publish.main([]))


if __name__ == "__main__":
    unittest.main()
