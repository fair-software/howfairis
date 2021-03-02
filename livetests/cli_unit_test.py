import unittest 
from click.testing import CliRunner, Result
from howfairis import cli

class CliTest(unittest.TestCase): 
  
    def test_valid_url(self):
        runner = CliRunner()
        result = runner.invoke(cli.cli, ["https://github.com/fair-software/howfairis"])
        self.assertEqual(result.exit_code, 0) 

    def test_invalid_url(self):
        runner = CliRunner()
        result = runner.invoke(cli.cli, ["howfairis"])
        self.assertEqual(str(result.exception), "url should start with https://")

    def test_no_github(self):
        runner = CliRunner()
        result = runner.invoke(cli.cli, ["https://www.esciencecenter.nl"])
        self.assertEqual(str(result.exception), "Repository should be on github.com or on gitlab.com")

    def test_no_repository(self):
        runner = CliRunner()
        result = runner.invoke(cli.cli, ["https://github.com/fair-software"])
        self.assertEqual(str(result.exception), "url is not a repository")

  
if __name__ == '__main__': 
    unittest.main() 
