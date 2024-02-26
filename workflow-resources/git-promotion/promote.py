#!/usr/bin/python3

import argparse
import functools
import copy
import shutil

from helper.GitHelper import GitHelper
from helper.FileHelper import FileHelper

def main():
    """
    Main function of this script. Promotes app version changes from one repository folder to another, given a source commit.
    """
    # Parses input arguments, initializes various local variables and perform basic checks on input parameters
    arguments = parse_arguments()

    git_repo = arguments.git_repo
    source_commit = arguments.source_commit
    source_phase = arguments.source_phase
    target_phase = arguments.target_phase

    if arguments.dry_run:
        print("Dry run enabled, no changes will be made")

    try:
        if target_phase:
            print("Running promotion from repo %s commit %s to phase %s" % (
                git_repo, source_commit, target_phase))

            repo = GitHelper.from_settings(git_repo).clone_and_setup_repo()

            source_version = FileHelper().get_app_version_for_phase(source_commit, source_phase, repo.git)
            target_version = FileHelper().get_app_version_for_phase(None, target_phase, repo.git)

            if source_version != target_version:
                print("Changes detected")
                FileHelper().update_app_version(source_version, target_phase)
                
                if not arguments.dry_run:
                    print("Commit and Push Changes")
                    repo.git.commit('-am', "(chore) - Automated app promotion")
                    repo.git.push()

            else:
                print("No change detected")
        else:
            print("No target folder provided")
    #except Exception as ex:
    #    print(ex)
    finally:
        # Remove the repository
        try:
            shutil.rmtree("clone")
        except OSError as e:
            print(f"Error: {e.filename} - {e.strerror}.")

def parse_arguments():
    """
    Parses input arguments of the current python script
    """
    parser = argparse.ArgumentParser(
        description='Promotes chart changes from one repository branch to another, given a source commit')
    required_args = parser.add_argument_group('required arguments')

    required_args.add_argument('-g', '--git-repo', type=str, help='The Git repository',
                                required=True)
    required_args.add_argument('-c', '--source-commit', type=str, help='The source commit id to promote', required=True)
    required_args.add_argument('-s', '--source-phase', type=str,
                               help='The source phase to promote the source commit content from', required=True)
    required_args.add_argument('-t', '--target-phase', type=str,
                               help='The target phase to promote the source commit content to', required=True)

    optional_args = parser.add_argument_group('optional arguments')
    optional_args.add_argument(
        '--dry-run', action='store_true', help='Optional, to run tests without doing a real commit for promotion')

    return parser.parse_args()


# -------------------------------------------------------------------------------------------
# Main
# -------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()