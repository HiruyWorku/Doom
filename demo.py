#!/usr/bin/env python3
"""
Demo script for Doom - Spotify Mood Detector
This script runs a demo version with mock data - no API credentials needed!
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
        sys.exit(1)
    
    # Check if app_demo.py exists
    app_file = os.path.join(src_dir, 'app_demo.py')
    if not os.path.exists(app_file):
        print("❌ Error: app_demo.py not found!")
        sys.exit(1)
    
    # Change to src directory
    os.chdir(src_dir)
    
    print("🎵 Doom - Spotify Mood Detector DEMO")
    print("=" * 50)
    print("🎭 This is a demo version with mock data")
    print("🔑 No Spotify API credentials required!")
    print("=" * 50)
    print("📍 Landing page: http://localhost:5000")
    print("📍 Demo dashboard: http://localhost:5000/demo")
    print("=" * 50)
    print("📸 Perfect for taking screenshots!")
    print("=" * 50)
    
    try:
        # Run the demo Flask application
        subprocess.run([sys.executable, 'app_demo.py'], check=True)
    except KeyboardInterrupt:
        print("\n👋 Demo stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running demo: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 