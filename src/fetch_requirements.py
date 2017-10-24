import os
import subprocess

REQUIREMENTS_DIR = "requirements"
if __name__ == '__main__':
    for dirname, dirnames, filenames in os.walk(REQUIREMENTS_DIR):
        for subdirname in dirnames:
            subdir_path = os.path.join(dirname, subdirname)

        for filename in filenames:
            filename_path =  os.path.join(dirname, filename)
            # check if requirements.txt has some information in it.
            if filename == 'requirements.txt':
                # read file contents.
                with open(filename_path) as requirementsfile:
                    requirements_content = requirementsfile.read()
                    if len(requirements_content):
                        print "Found content in {}".format(filename_path)
                        # since there exists a requirements.txt which has some libraries mentioned, download them in lib/ folder if it's empty
                        lib_dir_path = subdir_path+"/lib/"
                        pip_download_command = "pip download -r {} -d {}".format(filename_path, lib_dir_path)
                        subprocess.call(pip_download_command.split(" "))

