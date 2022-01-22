import os
import sys


if __name__ == "__main__"
    parser = argparse.ArgumentParser()
    parser.add_argument('binary')
    parser.add_argument('-g', '--grease-with')
    parser.add_argument('-d', '--driller_workers')
    parser.add_argument('-f', '--force_interval')
    parser.add_argument('-w', '--work-dir', default="/dev/shm/work/")
    parser.add_argument('-c', '--afl-cores', help="Number of AFL workers to spin up.", default=1, type=int)
    parser.add_argument('-C', '--first-crash', help="Stop on the first crash.", action='store_true', default=False)
    parser.add_argument('-t', '--timeout', help="Timeout (in seconds).", type=float)
    parser.add_argument('-i', '--ipython', help="Drop into ipython after starting the fuzzer.", action='store_true')
    parser.add_argument('-T', '--tarball', help="Tarball the resulting AFL workdir for further analysis to this file -- '{}' is replaced with the hostname.")
    parser.add_argument('-m', '--helper-module', help="A module that includes some helper scripts for seed selection and such.")
    parser.add_argument('--memory', help="Memory limit to pass to AFL (MB, or use k, M, G, T suffixes)", default="8G")
    parser.add_argument('--no-dictionary', help="Do not create a dictionary before fuzzing.", action='store_true', default=False)
    parser.add_argument('--logcfg', help="The logging configuration file.", default=".shellphuzz.ini")
    parser.add_argument('-s', '--seed-dir', action="append", help="Directory of files to seed fuzzer with")
    parser.add_argument('--run-timeout', help="Number of seconds permitted for each run of binary", type=int)
    parser.add_argument('--driller-timeout', help="Number of seconds to allow driller to run", type=int, default=10*60)
    parser.add_argument('--length-extension', help="Try extending inputs to driller by this many bytes", type=int)
    args = parser.parse_args()

    if os.path.isfile(os.path
