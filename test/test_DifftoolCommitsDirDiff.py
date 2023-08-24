import unittest
from unittest.mock import MagicMock
from gitgud.Fzf import Fzf
from gitgud.GitDataGetter import GitDataGetter
from gitgud.CommandRunner import CommandRunner
from gitgud.DifftoolCommitsDirDiff import DifftoolCommitsDirDiff

class TestDifftoolCommitsDirDiff(unittest.TestCase):

    def test_run(self):
        hash = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_commit_hash = MagicMock(return_value=hash)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run_foreground = MagicMock()
        difftool_commits = DifftoolCommitsDirDiff(command_runner, git_data_getter)
        difftool_commits.run()

        command_runner.run_foreground.assert_called_once_with(['git', 'difftool', hash, hash, '--dir-diff'])

if __name__ == '__main__':
    unittest.main()
