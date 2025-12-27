#!/usr/bin/env python
"""
Simple script to run the Django development server
"""
import os
import sys
import subprocess

def main():
    # Activate virtual environment and run server
    venv_python = os.path.join('portfolio_env', 'bin', 'python')
    
    if not os.path.exists(venv_python):
        print("Virtual environment not found. Please run:")
        print("python3 -m venv portfolio_env")
        print("source portfolio_env/bin/activate")
        print("pip install -r requirements.txt")
        return
    
    print("Starting Django development server...")
    print("Admin panel: http://127.0.0.1:8000/admin/")
    print("Username: admin")
    print("Password: admin")
    print("\nPress Ctrl+C to stop the server")
    
    try:
        subprocess.run([venv_python, 'manage.py', 'runserver'], check=True)
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except subprocess.CalledProcessError as e:
        print(f"Error running server: {e}")

if __name__ == '__main__':
    main()