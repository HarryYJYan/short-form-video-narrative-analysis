"""
Environment Setup Script for Short Form Video Narrative Analysis

This script sets up the Python environment and installs required packages.
"""

import subprocess
import sys

def install_package(package):
    """Install a package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def setup_environment():
    """Set up the analysis environment with required packages."""
    
    # Core data analysis packages
    packages = [
        "pandas>=1.5.0",
        "numpy>=1.21.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0",
        "scipy>=1.9.0",
        "scikit-learn>=1.1.0",
        "jupyter>=1.0.0",
        "ipykernel>=6.0.0"
    ]
    
    print("Setting up environment for Short Form Video Narrative Analysis...")
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            install_package(package)
            print(f"✓ {package} installed successfully")
        except Exception as e:
            print(f"✗ Failed to install {package}: {e}")
    
    print("\nEnvironment setup complete!")
    print("\nTo start Jupyter notebook, run:")
    print("jupyter notebook")

if __name__ == "__main__":
    setup_environment()
