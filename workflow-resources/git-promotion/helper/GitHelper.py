import os

from git import Repo


class GitHelper(object):
    """
    Helper around Git repository operations
    """

    def __init__(self, git_repo_url) -> None:
        self.url = git_repo_url

    @classmethod
    def from_settings(cls, git_repo: str):
        end_prefix_index = git_repo.index("//") + 2
        git_repo = (
            git_repo[:end_prefix_index] + "%s:%s@" + git_repo[end_prefix_index:]
        )
        url = f"{git_repo}"
        return cls(url)

    def clone_and_setup_repo(self) -> Repo:
        username = os.environ["GIT_USER"]
        password = os.environ["GIT_PASSWORD"]
        git_mail = os.environ["GIT_EMAIL"]
        git_repo_url = self.url % (username, password)

        repo = Repo.clone_from(git_repo_url, "clone", config="http.sslVerify=false")
        repo.config_writer().set_value("user", "name", username).release()
        repo.config_writer().set_value("user", "email", git_mail).release()
        repo.git.fetch("--all")

        print("Git repository cloned and set up")

        return repo