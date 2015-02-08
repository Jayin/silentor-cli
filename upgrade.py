#!usr/bin/env python
# -*- coding: utf-8 -*-

from silentorcli.github import GitHub
import os

clone_url = 'https://github.com/Jayin/silentor.git'


def main():
    print("Fetching .....")
    github = GitHub()
    releases = github.get_releases('Jayin', 'silentor')
    latest_release = releases[0]
    print("lasest version is %s" % latest_release['tag_name'])

    cmds = [
        'cd silentor',
        'git status',
        'git checkout --quiet gh-pages',
        'git pull',
        'git checkout --quiet {tag}'.format(tag=latest_release['tag_name']),
        'git status'
    ]
    os.system(' && '.join(cmds))
    print('upgrade to lasest version: {tag} '.format(tag=latest_release['tag_name']))


if __name__ == '__main__':
    main()
