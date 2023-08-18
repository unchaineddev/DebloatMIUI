import subprocess

# Uninstalls packages
def uninstall_apk(package_name):
    subprocess.run(["adb", "shell", "pm", "uninstall", "--user", "0", package_name])

# Reads from file and uninstalls
with open("commands.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if line.strip():
            package_name = line.split("|")[0].strip()
            print(f"Uninstalling: {package_name}")
            uninstall_apk(package_name)

print("APK uninstallation completed.")
