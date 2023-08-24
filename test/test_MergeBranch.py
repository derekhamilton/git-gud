import unittest
from unittest.mock import MagicMock
from gitgud.Fzf import Fzf
from gitgud.GitDataGetter import GitDataGetter
from gitgud.CommandRunner import CommandRunner
from gitgud.MergeBranch import MergeBranch

class TestMergeBranch(unittest.TestCase):

    def test_run(self):
        branch = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_branch_name = MagicMock(return_value=branch)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run = MagicMock()
        merge_branch = MergeBranch(command_runner, git_data_getter)
        merge_branch.run()

        command_runner.run.assert_called_once_with(['git', 'merge', branch])

if __name__ == '__main__':
    unittest.main()
