import subprocess
import sys

class CommandLineOptions:
    command = None
    file = None

    def __init__(self,command ="-u",file="command.txt"):
        self.command = command
        self.file = file

# Uninstalls packages
def uninstall_apk(package_name):
    subprocess.run(["adb", "shell", "pm", "uninstall", "--user", "0", package_name])

#restores packages
def restore_apk(package_name):
    subprocess.run(["adb", "shell", "cmd","package", "install-existing", package_name])

# Reads from file and execute an install or unuinstall
def read_and_execute(file_name,command,command_str = ""):
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():
                package_name = line.split("|")[0].strip()
                if not package_name.startswith("#"):
                    print(f"{command_str} {package_name}")
                    command(package_name)

def read_cmd_line():
    options = CommandLineOptions()
    for flag in sys.argv:
        if flag == "-i" or flag == "-r":
            options.command = flag
        elif not (flag.find("=") == -1):
            print(flag.find("="))
            if flag.split("=")[0] == "file":
                options.file = flag.split("=")[1]
    return options

def main():
    options = read_cmd_line()
    if options.command == "-u":
        read_and_execute(options.file,uninstall_apk,"Uninstalling : ")
        print("\nAPK uninstallation completed.")
    elif options.command == "-r":
        read_and_execute(options.file,restore_apk,"Restoring : ")
        print("\nAPK restoration completed.")

main()