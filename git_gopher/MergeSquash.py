from git_gopher.CommandInterface import CommandInterface

class MergeSquash(CommandInterface):
    def __init__(self, hist_command_runer, git_data_getter):
        self._hist_command_runer = hist_command_runer
        self._git_data_getter = git_data_getter

    def run(self):
        branch = self._git_data_getter.get_branch_name(preview='echo "git merge --squash {2}"')

        if branch:
            self._hist_command_runer.run(['git', 'merge', '--squash', branch])
