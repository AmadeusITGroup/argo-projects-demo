import os
import yaml
from yaml.loader import SafeLoader


class FileHelper(object):
    """
    Helper class for files
    """

    APP_FILE_PATH = './clone/argo-projects/app/manifests/overlays/'

    def get_app_version_for_phase(self, commit, phase, git_repo):
        """
        Get the app version from the values in the phase provided
        :param commit: GIT commit from which to retrieve the app version
        :param phase: the application phase for which to retrieve the app version
        :param git_repo: the GIT repository from which to app version
        :return: the app version
        """
        print("Getting app version for phase %s, commit %s" % (phase,commit))

        if commit is not None:
            git_repo.checkout(commit)
        else:
            git_repo.checkout()

        if os.path.isfile(FileHelper.APP_FILE_PATH + phase + "/values-" + phase + ".yaml"):
            with open(FileHelper.APP_FILE_PATH + phase + "/values-" + phase + ".yaml") as f:
                values = yaml.load(f, Loader=SafeLoader)
                if values is not None and 'image' in values and version in values['image']:
                    return values['image']['version']
                else:
                    print("No version found in values file for phase: %s" % phase)
        else:
            print("Could not find values file for phase: %s" % phase)
    
    def update_app_version(self, version, phase):

        print("Updating app version for phase %s" % phase)

        # Update to latest
        git_repo.checkout("main")
        git_repo.pull()

        if os.path.isfile(FileHelper.APP_FILE_PATH + phase + "/values-" + phase + ".yaml"):
            with open(FileHelper.APP_FILE_PATH + phase + "/values-" + phase + ".yaml") as f:
                values = yaml.load(f, Loader=SafeLoader)
                if values is not None and 'image' in values and version in values['image']:
                    values['image']['version'] = version
                    with open(APP_FILE_PATH + phase + "/values-" + phase + ".yaml", 'w') as f:
                        yaml.dump(values, f)
                else:
                    print("No version found in values file for phase: %s" % phase)
        else:
            print("Could not find values file for phase: %s" % phase)