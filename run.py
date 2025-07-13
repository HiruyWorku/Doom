#!/usr/bin/env python3
"""
Simple run script for the Doom Spotify Mood Detector application.
This script changes to the src directory and runs the Flask app.
"""

import os
import sys
import subprocess

def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(script_dir, 'src')
    
    # Check if src directory exists
    if not os.path.exists(src_dir):
        print("❌ Error: src directory not found!")
        print("Make sure you're running this from the project root directory.")
        sys.exit(1)
    
    # Check if app.py exists in src directory
    app_file = os.path.join(src_dir, 'app.py')
    if not os.path.exists(app_file):
        print("❌ Error: app.py not found in src directory!")
        print("Make sure the application files are properly set up.")
        sys.exit(1)
    
    # Change to src directory
    os.chdir(src_dir)
    
    print("🚀 Starting Doom - Spotify Mood Detector...")
    print("📍 Application will be available at: http://localhost:5000")
    print("📝 Make sure you have set up your .env file with Spotify credentials!")
    print("=" * 60)
    
    try:
        # Run the Flask application
        subprocess.run([sys.executable, 'app.py'], check=True)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running application: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ Error: Python executable not found!")
        print("Make sure Python is installed and in your PATH.")
        sys.exit(1)

if __name__ == '__main__':
    main() 