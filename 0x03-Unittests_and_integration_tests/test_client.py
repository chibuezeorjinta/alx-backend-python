#!/usr/bin/env python3
"""GitHub class testing"""
import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Class to test GitHub org json retrival"""
    @parameterized.expand([
        "google",
        "abc"
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_str: str, mock_get):
        """Test the org method of the GitHub org class"""
        test_call = GithubOrgClient(org_str)
        result = test_call.org
        self.assertEqual(result, mock_get.return_value)
        mock_get.assert_called_once_with(test_call.ORG_URL.format(org=org_str))

    def test_public_repos_url(self):
        """ to unit-test GithubOrgClient._public_repos_url """
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value={"repos_url": "holberton"}) as mock_get:
            test_json = {"repos_url": "holberton"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            mock_get.assert_called_once()
            self.assertEqual(test_return,
                             mock_get.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get):
        """ to unit-test GithubOrgClient.public_repos """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            test_client = GithubOrgClient("hoberton")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["holberton"])
            mock_get.assert_called_once()
            mock_pub.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_return):
        """ to unit-test GithubOrgClient.has_license """
        test_client = GithubOrgClient("holberton")
        test_return = test_client.has_license(repo, license_key)
        self.assertEqual(expected_return, test_return)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Implement integration across fixtures"""
    @classmethod
    def setUpClass(cls):
        """Set up class"""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class setup"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """configure request call"""
        self.mock_get.return_value.json.side_effect = [
            self.org_payload, self.repos_payload]
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Configure requests to note a license key"""
        self.mock_get.return_value.json.side_effect = [
            self.org_payload, self.repos_payload]
        client = GithubOrgClient("google")
        check_license = client.public_repos(license="apache-2.0")
        self.assertEqual(check_license, self.apache2_repos)
