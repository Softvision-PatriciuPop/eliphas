import os
import os.path
import shutil
import glob


class Remember:
    if os.path.isfile('eliphas.txt'):
        print("Config present")
    else:
        f = open("eliphas.txt", "a")
        f.write("0")
        f.close()


class Profile:
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
        n +=1
    os.chdir(root)
    g = open("eliphas.txt", "w")
    g.write(str(n))
    g.close()
