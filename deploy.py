#!/usr/bin/env python
"""
Deployment script for the portfolio Django application
"""
import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print(f"STDOUT: {e.stdout}")
        if e.stderr:
            print(f"STDERR: {e.stderr}")
        return False

def main():
    print("🚀 Portfolio Django Application Deployment")
    print("=" * 50)
    
    # Check if virtual environment exists
    if not os.path.exists('portfolio_env'):
        print("Creating virtual environment...")
        if not run_command('python3 -m venv portfolio_env', 'Virtual environment creation'):
            return
    
    # Install dependencies
    if not run_command('source portfolio_env/bin/activate && pip install -r requirements.txt', 'Installing dependencies'):
        return
    
    # Run migrations
    if not run_command('source portfolio_env/bin/activate && python manage.py makemigrations', 'Creating migrations'):
        return
    
    if not run_command('source portfolio_env/bin/activate && python manage.py migrate', 'Running migrations'):
        return
    
    # Collect static files
    if not run_command('source portfolio_env/bin/activate && python manage.py collectstatic --noinput', 'Collecting static files'):
        return
    
    # Create superuser if it doesn't exist
    print("\n📝 Creating superuser (if needed)...")
    try:
        subprocess.run('source portfolio_env/bin/activate && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username=\'admin\').exists() or User.objects.create_superuser(\'admin\', \'admin@example.com\', \'admin\')" | python manage.py shell', 
                      shell=True, check=True, capture_output=True)
        print("✅ Superuser ready")
    except subprocess.CalledProcessError:
        print("ℹ️  Superuser already exists or creation failed")
    
    # Populate initial data
    if not run_command('source portfolio_env/bin/activate && python seed_data.py', 'Seeding initial data'):
        print("ℹ️  Data seeding failed (might already exist)")
    
    print("\n🎉 Deployment completed successfully!")
    print("\n📋 Next steps:")
    print("1. Run the server: python run_server.py")
    print("2. Visit: http://127.0.0.1:8000/")
    print("3. Admin panel: http://127.0.0.1:8000/admin/")
    print("4. Login with: admin / admin")
    print("\n💡 Don't forget to change the admin password in production!")

if __name__ == '__main__':
    main()