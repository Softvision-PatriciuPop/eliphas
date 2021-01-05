import os
import os.path
import shutil
import glob
import sys
import getpass


class Remember:
    if os.path.isfile('eliphas.txt'):
        print("Config present")
    else:
        f = open("eliphas.txt", "a")
        f.write("0")
        f.close()

def profile_win():
    f = open("eliphas.txt", "r")
    n = int(f.readline())
    f.close()
    root = os.getcwd()
    file_to_copy = str(root) + "\\user.js"
    path = os.getenv('APPDATA') + "\Mozilla\Firefox\Profiles"
    full_path = path + "\Mozilla\Firefox\Profiles"
    nr = int(input("Number of profiles: "))
    for i in range(nr):
        create_build = 'cmd /c "firefox.exe -p -CreateProfile eliphas{}"'.format(n+1)
        os.system(create_build)
        os.chdir(path)
        profile_path = str(glob.glob('*eliphas{}'.format(n + 1)))
        profile_path = profile_path.replace("[", "\\")
        profile_path = profile_path.replace("]", "")
        profile_path = profile_path.replace("'", "")
        full_path = str(path) + str(profile_path)
        shutil.copy2(file_to_copy, full_path)
        os.chdir(root)
        open_build = 'cmd /c "set XPCSHELL_TEST_PROFILE_DIR=foo & firefox.exe -no-remote -p eliphas{}"'.format(n+1)
        os.system(open_build)
        n += 1
    os.chdir(root)
    g = open("eliphas.txt", "w")
    g.write(str(n))
    g.close()


def profile_linux():
    f = open("eliphas.txt", "r")
    n = int(f.readline())
    f.close()
    root = os.getcwd()
    file_to_copy = str(root) + "/user.js"
    username = str(getpass.getuser())
    path = "/home/{}/.mozilla/firefox/".format(username)
    nr = int(input("Number of profiles: "))
    for i in range(nr):
        create_build = 'firefox -p -CreateProfile eliphas{}'.format(n+1)
        os.system(create_build)
        os.chdir(path)
        profile_path = str(glob.glob('*eliphas{}'.format(n + 1)))
        profile_path = profile_path.replace("[", "")
        profile_path = profile_path.replace("]", "")
        profile_path = profile_path.replace("'", "")
        full_path = str(path) + str(profile_path)
        shutil.copy2(file_to_copy, full_path) + "/user.js"
        os.chdir(root)
        open_build = 'export XPCSHELL_TEST_PROFILE_DIR=foo ; {}/firefox -no-remote -p eliphas{}'.format((root), (n+1))
        os.system(open_build)
        n += 1
    os.chdir(root)
    g = open("eliphas.txt", "w")
    g.write(str(n))
    g.close()


class OScheck:
    if sys.platform == 'win32':
        profile_win()
    if sys.platform == 'darwin':
        print("mac")
        # profile_mac()
    else:
        profile_linux()
