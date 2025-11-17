"""
Login System - AI Generated Code
This is a basic login system implementation.
"""

import hashlib
import json
import os
from datetime import datetime, timedelta

# User database (in production, use a real database)
users_db = {}

# Session storage (in production, use Redis or similar)
active_sessions = {}

def hash_password(password):
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    """Register a new user"""
    if username in users_db:
        return False, "Username already exists"
    
    # Hash the password before storing
    hashed_password = hash_password(password)
    users_db[username] = {
        'password': hashed_password,
        'created_at': datetime.now().isoformat()
    }
    return True, "User registered successfully"

def login(username, password):
    """Login user"""
    if username not in users_db:
        return False, "Invalid username or password"
    
    # Verify password
    hashed_password = hash_password(password)
    if users_db[username]['password'] == hashed_password:
        # Create session
        session_id = hashlib.md5(f"{username}{datetime.now()}".encode()).hexdigest()
        active_sessions[session_id] = {
            'username': username,
            'created_at': datetime.now().isoformat(),
            'expires_at': (datetime.now() + timedelta(hours=1)).isoformat()
        }
        return True, f"Login successful. Session ID: {session_id}"
    else:
        return False, "Invalid username or password"

def verify_session(session_id):
    """Verify if session is valid"""
    if session_id not in active_sessions:
        return False, "Invalid session"
    
    session = active_sessions[session_id]
    expires_at = datetime.fromisoformat(session['expires_at'])
    
    if datetime.now() > expires_at:
        del active_sessions[session_id]
        return False, "Session expired"
    
    return True, session['username']

def logout(session_id):
    """Logout user"""
    if session_id in active_sessions:
        del active_sessions[session_id]
        return True, "Logged out successfully"
    return False, "Invalid session"

def change_password(username, old_password, new_password):
    """Change user password"""
    if username not in users_db:
        return False, "User not found"
    
    # Verify old password
    hashed_old_password = hash_password(old_password)
    if users_db[username]['password'] != hashed_old_password:
        return False, "Incorrect old password"
    
    # Update to new password
    hashed_new_password = hash_password(new_password)
    users_db[username]['password'] = hashed_new_password
    users_db[username]['password_changed_at'] = datetime.now().isoformat()
    return True, "Password changed successfully"

def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("        LOGIN SYSTEM MENU")
    print("="*40)
    print("1. Register")
    print("2. Login")
    print("3. Change Password")
    print("4. Logout")
    print("5. Exit")
    print("="*40)

# Main menu-driven interface
if __name__ == "__main__":
    current_session = None  # Store current session ID
    
    print("=== Welcome to Login System ===")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        # Switch case equivalent using if-elif
        if choice == "1":  # Register
            print("\n--- REGISTER ---")
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            
            if not username or not password:
                print("Error: Username and password cannot be empty!")
            else:
                success, message = register_user(username, password)
                print(f"Result: {message}")
        
        elif choice == "2":  # Login
            print("\n--- LOGIN ---")
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            
            if not username or not password:
                print("Error: Username and password cannot be empty!")
            else:
                success, message = login(username, password)
                print(f"Result: {message}")
                
                if success:
                    # Extract session ID from message
                    current_session = message.split(": ")[1]
                    print(f"Current session: {current_session}")
        
        elif choice == "3":  # Change Password
            print("\n--- CHANGE PASSWORD ---")
            
            if current_session is None:
                print("Error: You must be logged in to change password!")
                print("Please login first (option 2).")
            else:
                # Verify session is still valid
                valid, username = verify_session(current_session)
                if not valid:
                    print(f"Error: {username}")
                    print("Your session has expired. Please login again.")
                    current_session = None
                else:
                    old_password = input("Enter old password: ").strip()
                    new_password = input("Enter new password: ").strip()
                    confirm_password = input("Confirm new password: ").strip()
                    
                    if not old_password or not new_password:
                        print("Error: Passwords cannot be empty!")
                    elif new_password != confirm_password:
                        print("Error: New passwords do not match!")
                    else:
                        success, message = change_password(username, old_password, new_password)
                        print(f"Result: {message}")
        
        elif choice == "4":  # Logout
            print("\n--- LOGOUT ---")
            
            if current_session is None:
                print("Error: No active session found!")
                print("You are not logged in.")
            else:
                success, message = logout(current_session)
                print(f"Result: {message}")
                if success:
                    current_session = None
        
        elif choice == "5":  # Exit
            print("\n--- EXIT ---")
            if current_session:
                logout(current_session)
                print("Logged out before exit.")
            print("Thank you for using the Login System. Goodbye!")
            break
        
        else:
            print("\nError: Invalid choice! Please enter a number between 1-5.")

