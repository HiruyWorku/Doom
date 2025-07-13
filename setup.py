#!/usr/bin/env python3
"""
Setup script for Doom - Spotify Mood Detector
This script helps users set up the environment and dependencies.
"""

import os
import sys
import subprocess
import shutil

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def check_pip():
    """Check if pip is available"""
    try:
        subprocess.run([sys.executable, '-m', 'pip', '--version'], 
                      check=True, capture_output=True)
        print("✅ pip is available")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Error: pip is not available!")
        return False

def install_dependencies():
    """Install Python dependencies"""
    print("\n📦 Installing Python dependencies...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                      check=True)
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def create_env_file():
    """Create .env file from template"""
    env_file = '.env'
    env_example = 'env.example'
    
    if os.path.exists(env_file):
        print("✅ .env file already exists")
        return True
    
    if not os.path.exists(env_example):
        print("❌ Error: env.example file not found!")
        return False
    
    try:
        shutil.copy(env_example, env_file)
        print("✅ Created .env file from template")
        print("📝 Please edit .env file with your Spotify API credentials")
        return True
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False

def check_structure():
    """Check if project structure is correct"""
    required_files = [
        'src/app.py',
        'src/templates/index.html',
        'src/templates/dashboard.html',
        'src/static/css/style.css',
        'src/static/js/dashboard.js',
        'requirements.txt',
        'README.md'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Missing required files:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        return False
    
    print("✅ Project structure is correct")
    return True

def main():
    print("🎵 Doom - Spotify Mood Detector Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check pip
    if not check_pip():
        sys.exit(1)
    
    # Check project structure
    if not check_structure():
        print("\n❌ Setup failed: Project structure is incomplete")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Setup failed: Could not install dependencies")
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        print("\n❌ Setup failed: Could not create .env file")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit .env file with your Spotify API credentials")
    print("2. Get Spotify API credentials from https://developer.spotify.com/dashboard")
    print("3. Run the application with: python run.py")
    print("\n📖 For more information, see README.md")

if __name__ == '__main__':
    main() 