import os
import sys
import tempfile
import argparse
import subprocess
import json
import shutil
import glob

import cassette


def run_cmd(cmd):
    with tempfile.TemporaryDirectory() as tmpdir:
        cwd = os.getcwd()
        os.chdir(tmpdir)

        p = subprocess.run(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            cwd=tmpdir
        )

        if p.stderr:
            sys.stderr.write(str(p.stderr))
            err_msg = "Error output from youtube command: {}".format(cmd)
            raise Exception(err_msg)

        for f in glob.glob("*.mp3"):
            shutil.copy(f, cwd)

        os.chdir(cwd)
        return p.stdout


def get_url_song(url):
    """Extract the best available audio to an mp3 file named
    "(youtube post title).mp3" and use post thumbnail for album art
    """
    cmd_get_audio = 'youtube-dl ' \
        '-x -f bestaudio ' \
        '--audio-format mp3 ' \
        '-o \"%(title)s.%(ext)s\" ' \
        '--embed-thumbnail ' \
        '\"{}\"'

    run_cmd(cmd_get_audio.format(url))


def main():
    parser = argparse.ArgumentParser(
        description=cassette.__description__
    )
    parser.add_argument(
        'url', nargs="+", help='Extract audio from one or more URLs'
    )
    args = parser.parse_args()

    for url in args.url:
        get_url_song(url)
