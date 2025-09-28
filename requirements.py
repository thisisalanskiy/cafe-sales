import importlib
import sys
import os

class check_requirements:
    def __init__(self, requirements_file="requirements.txt"):
        self.requirements_file = requirements_file
        self.missing_packages = []
    
    def check_requirements_file(self):
        """Ensure the requirements file exists."""
        if not os.path.exists(self.requirements_file):
            raise FileNotFoundError(f"Error: '{self.requirements_file}' not found. If you have the file, place it with the rest of the files.")
        
        try:
            with open(self.requirements_file, "r") as file:
                self.requirements = [line.strip() for line in file if line.strip()]
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred while reading '{self.requirements_file}': {e}")
    
    def check_installed_packages(self):
        """Check if required packages are installed."""
        for package in self.requirements:
            package_name = package.split("==")[0]  # Extract package name if version is specified
            if not self.is_package_installed(package_name):
                self.missing_packages.append(package)
    
    def is_package_installed(self, package_name):
        """Check if a package is installed in the current environment."""
        spec = importlib.util.find_spec(package_name)
        return spec is not None
    
    def install_missing_packages(self):
        """Install missing packages using pip."""
        if self.missing_packages:
            for package in self.missing_packages:
                exit_code = os.system(f"pip install {package}")
                if exit_code != 0:
                    raise RuntimeError(f"Failed to install {package}")
        
    def run(self):
        """Execute the full check process."""
        try:
            print("Running requirements check...")
            self.check_requirements_file()
            print(f"Looking for required packages in the '{self.requirements_file}' file...")
            self.check_installed_packages()
            if self.missing_packages:
                print(f"Installing missing packages from the '{self.requirements_file}' file...")
                self.install_missing_packages()
                print("All missing packages have been installed.")
            else:
                print("All required packages are already installed.\nPlease proceed to the next section of the analysis :)")
        except FileNotFoundError as e:
            print(e)
        except RuntimeError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
