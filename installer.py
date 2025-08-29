import shutil, subprocess, platform, os

# Installer class, checks for system, homebrew installation and chdman installation
# Installs homebrew and chdman if not present
class Installer:
    def __init__(self):
        self.os_name = platform.system()
        self.os_arch = platform.machine()
        # Early exit if not macOS
        if platform.system() != "Darwin":
            raise RuntimeError("Installer only supported on macOS")
    
    # --- Checks ---   
    # Checks if homebrew is installed
    def check_homebrew(self):
        path = shutil.which("brew")
        if path is None:
            print("Homebrew is not installed")
            return False
        else:
            print("Homebrew is installed")
            return True

    # Checks if chdman is installed
    def check_chdman(self):
        homebrew_installed = self.check_homebrew()
        if homebrew_installed:
            path = shutil.which("chdman")
            if path is None:
                print("chdman is not installed")
                return False
            else:
                print("chdman is installed")
                return True
        else:
            print("Homebrew is not installed")
            return False

    # --- Installers ---
    # Installs homebrew
    def install_homebrew(self):
        install_command = '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
        subprocess.run(install_command, shell=True, check=True)
        print("Homebrew installed successfully")
        self.homebrew_to_path()
        return True

    # Adds homebrew to path
    def homebrew_to_path(self):
        brew_prefix = "/opt/homebrew" if self.os_arch == "arm64" else "/usr/local"
        # Get the environment setup lines
        out = subprocess.check_output([f"{brew_prefix}/bin/brew", "shellenv"], text=True)
        for line in out.splitlines():
            if line.startswith("export "):
                key, val = line[len("export "):].split("=", 1)
                os.environ[key] = val.strip('"')
            # Prepend bin/sbin to PATH explicitly
            os.environ["PATH"] = f"{brew_prefix}/bin:{brew_prefix}/sbin:" + os.environ.get("PATH", "")
            print("Homebrew has been added to PATH for this process")
    
    # Installs chdman
    def install_chdman(self):
        if self.check_chdman() == False:
            command = "brew install rom-tools"
            subprocess.run(command, shell=True, check=True)
            print("chdman installed successfully")

if __name__ == "__main__":
    inst = Installer()
    has_homebrew = inst.check_homebrew()
    if not has_homebrew:
        inst.install_homebrew()
    has_chdman = inst.check_chdman()
    if not has_chdman:
        inst.install_chdman()







