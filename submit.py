import os
import argparse
import subprocess
import glob
from nelson.gtomscs import submit
# see https://github.com/udacity/nelson for nelson information (OMSCS specific)

DEVNULL = open("/dev/null", "wb")
md5_file_name = "md5sum.txt"

def cleanup_md5sum():
    try:
        os.remove(md5_file_name)
    except OSError:
        pass


def compute_md5sum():
    cleanup_md5sum()
    sum_command = ["md5sum"] + glob.glob("*")
    subprocess.call(sum_command, stdout=open(md5_file_name, "w"), stderr=DEVNULL)

def compute_readme_list():
    readme_list = []
    readme_candidates = ['readme-student.md', 'readme-student.pdf', 'student-readme.md', 'student-readme.pdf']
    for candidate in readme_candidates:
        if os.path.isfile(candidate):
            readme_list.append(candidate)
    if len(readme_list) is 0:
        raise Exception("There is no valid student readme file to submit")
    return readme_list

def main():
    parser = argparse.ArgumentParser(description='Submits code to the Udacity site.')
    parser.add_argument('quiz', choices=['echo', 'transfer', 'gfclient', 'gfserver', 'gfclient_mt', 'gfserver_mt', 'readme'])

    args = parser.parse_args()

    path_map = {'echo': 'echo',
                'transfer': 'transfer',
                'gfclient': 'gflib',
                'gfserver': 'gflib',
                'gfclient_mt': 'mtgf',
                'gfserver_mt': 'mtgf',
                'readme': '.'}

    quiz_map = {'echo': 'pr1_echo_client_server',
                'transfer': 'pr1_transfer',
                'gfclient': 'pr1_gfclient',
                'gfserver': 'pr1_gfserver',
                'gfclient_mt': 'pr1_gfclient_mt',
                'gfserver_mt': 'pr1_gfserver_mt',
                'readme': 'pr1_readme'}

    files_map = {'pr1_echo_client_server': ['echoclient.c', 'echoserver.c'],
                 'pr1_transfer': ['transferclient.c', 'transferserver.c'],
                 'pr1_gfclient': ['gfclient.c', 'gfclient-student.h', 'gf-student.h'],
                 'pr1_gfserver': ['gfserver.c', 'gfserver-student.h', 'gf-student.h'],
                 'pr1_gfclient_mt': ['gfclient_download.c', 'gfclient-student.h', 'gf-student.h'],
                 'pr1_gfserver_mt': ['gfserver_main.c', 'handler.c', 'gfserver-student.h', 'gf-student.h'],
                 'pr1_readme': compute_readme_list()}

    quiz = quiz_map[args.quiz]

    os.chdir(path_map[args.quiz])
    compute_md5sum()
    if (os.path.exists(md5_file_name)): files_map[quiz].append(md5_file_name)

    submit('cs6200', quiz, files_map[quiz])
    cleanup_md5sum()

if __name__ == '__main__':
    main()
