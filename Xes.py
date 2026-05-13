#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════╗
║           X E S - C O N T R O L   v 3 . 0           ║
║         Advanced Access Control Framework           ║
║           "Total Breach Protocol"                    ║
╚══════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import random
import string
import json
import hashlib
import base64
from getpass import getpass
from datetime import datetime

# ============================================
# COLOR SYSTEM
# ============================================
R = '\033[91m'    # Red
G = '\033[92m'    # Green
Y = '\033[93m'    # Yellow
B = '\033[94m'    # Blue
M = '\033[95m'    # Magenta
C = '\033[96m'    # Cyan
W = '\033[97m'    # White
DG = '\033[90m'   # Dark Gray
LR = '\033[38;5;196m'  # Bright Red
LG = '\033[38;5;46m'   # Bright Green
X = '\033[0m'     # Reset
BO = '\033[1m'    # Bold
BL = '\033[5m'    # Blink
UL = '\033[4m'    # Underline
INV = '\033[7m'   # Inverse

# ============================================
# UTILITY FUNCTIONS
# ============================================
def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def timestamp():
    return datetime.now().strftime("%H:%M:%S")

# ============================================
# ANIMATIONS
# ============================================
def skull_animation():
    skulls = [
        f"""{LR}
        .-"-._.-"-._.-
       /     .-.     \\
      /   ,'   `.   \\
     ;   /       \\   ;
     |  |         |  |
     |  |  0   0  |  |
     |  |    _    |  |
     ;   \\  ___  /   ;
      \\   `.___.'   /
       \\           /
        `-._   _.-'
            `"`
        {X}""",
        f"""{LR}
        .-"-._.-"-._.-
       /     .-.     \\
      /   ,'   `.   \\
     ;   /       \\   ;
     |  |  X   X  |  |
     |  |    _    |  |
     ;   \\  ___  /   ;
      \\   `.___.'   /
       \\           /
        `-._   _.-'
            `"`
        {X}"""
    ]
    for _ in range(6):
        clear()
        print(skulls[_ % 2])
        print(f"{R}{BL}⚠ BREACHING ACCESS CONTROL ⚠{X}")
        time.sleep(0.3)

def matrix_rain(lines=15, delay=0.015):
    chars = "ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃ0123456789!@#$%^&*"
    for _ in range(lines):
        rain = ''.join(random.choice(chars) for _ in range(50))
        shade = random.randint(90, 97)
        print(f"\033[38;5;{shade}m{rain}{X}")
        time.sleep(delay)

def progress_bar(task="BREACHING", duration=2.5, steps=35):
    print(f"\n{Y}[*] {task}...{X}")
    for i in range(steps + 1):
        filled = '█' * i
        empty = '░' * (steps - i)
        percent = int((i / steps) * 100)
        color = G if i < steps * 0.7 else Y if i < steps * 0.9 else LR
        sys.stdout.write(f"\r{color}[{filled}{empty}] {percent}%{X}")
        sys.stdout.flush()
        time.sleep(duration / steps)
    print(f"\n{LR}[✓] {task} COMPLETE!{X}\n")

def typewriter(text, color=G, speed=0.02):
    for char in text:
        sys.stdout.write(f"{color}{char}{X}")
        sys.stdout.flush()
        time.sleep(speed)
    print()

def spinner(seconds=1.5, text="Processing"):
    frames = ['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏']
    end = time.time() + seconds
    while time.time() < end:
        for frame in frames:
            sys.stdout.write(f"\r{Y}{frame} {text}...{X}")
            sys.stdout.flush()
            time.sleep(0.04)
    sys.stdout.write(f"\r{G}✓ {text} Complete!{X}     \n")

def glitch_effect(text, iterations=3):
    for _ in range(iterations):
        glitched = ''.join(random.choice([c.upper(), c.lower(), random.choice('!@#$%')]) if random.random() > 0.7 else c for c in text)
        sys.stdout.write(f"\r{R}{glitched}{X}")
        sys.stdout.flush()
        time.sleep(0.08)
    sys.stdout.write(f"\r{G}{text}{X}     \n")

def countdown(seconds=3):
    for i in range(seconds, 0, -1):
        print(f"{LR}{BL}  ⏱ {i}...{X}", end='\r')
        time.sleep(1)
    print(f"{LR}{BL}  ⚡ EXECUTING!{X}     ")

def access_granted_anim():
    print(f"\n{LR}╔══════════════════════════════════╗")
    typewriter("║   🔓 ACCESS GRANTED 🔓   ║", LR, 0.03)
    print(f"{LR}╚══════════════════════════════════╝{X}\n")

def access_denied_anim():
    print(f"\n{R}╔══════════════════════════════════╗")
    typewriter("║   🔒 ACCESS DENIED 🔒    ║", R, 0.03)
    print(f"{R}╚══════════════════════════════════╝{X}\n")

# ============================================
# BANNER
# ============================================
def show_banner():
    clear()
    print(f"""
{LR}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  {BO}{W}██╗  ██╗███████╗███████╗     ██████╗ ██████╗ ███╗   ██╗{LR}  ║
║  {BO}{W}╚██╗██╔╝██╔════╝██╔════╝    ██╔════╝██╔═══██╗████╗  ██║{LR}  ║
║  {BO}{W} ╚███╔╝ █████╗  ███████╗    ██║     ██║   ██║██╔██╗ ██║{LR}  ║
║  {BO}{W} ██╔██╗ ██╔══╝  ╚════██║    ██║     ██║   ██║██║╚██╗██║{LR}  ║
║  {BO}{W}██╔╝ ██╗███████╗███████║    ╚██████╗╚██████╔╝██║ ╚████║{LR}  ║
║  {BO}{W}╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝{LR}  ║
║                                                              ║
║        {DG}ADVANCED ACCESS CONTROL FRAMEWORK v3.0{R}               ║
║        {DG}"Total Breach Protocol - No Barrier Unbroken"{R}         ║
╚══════════════════════════════════════════════════════════════╝{X}
""")

# ============================================
# SIMULATED USER DATABASE
# ============================================
USERS_DB = {
    "admin": {"password": "admin123", "role": "ROOT", "access_level": 5},
    "root": {"password": "toor", "role": "ROOT", "access_level": 5},
    "user": {"password": "password", "role": "USER", "access_level": 1},
    "guest": {"password": "guest", "role": "GUEST", "access_level": 0},
}

ACCESS_LOGS = []

def log_access(action, detail, status):
    ACCESS_LOGS.append({
        "time": timestamp(),
        "action": action,
        "detail": detail,
        "status": status
    })

# ============================================
# PASSWORD GENERATOR
# ============================================
def generate_password(length=16, complexity="high"):
    if complexity == "low":
        chars = string.ascii_letters + string.digits
    elif complexity == "medium":
        chars = string.ascii_letters + string.digits + "!@#$%"
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
    
    return ''.join(random.choice(chars) for _ in range(length))

# ============================================
# ACCESS CONTROL SIMULATOR
# ============================================
def simulate_breach(target, method):
    print(f"\n{Y}[!] Target: {target}{X}")
    print(f"{Y}[!] Method: {method}{X}")
    time.sleep(0.3)
    
    skull_animation()
    progress_bar(f"BREACHING {target.upper()}", 2, 30)
    
    # Simulate success rate
    success_rate = random.randint(60, 95)
    print(f"{C}[*] Success Probability: {success_rate}%{X}")
    spinner(1, "Finalizing breach")
    
    if success_rate > 75:
        access_granted_anim()
        log_access("BREACH", target, "SUCCESS")
        return True
    else:
        access_denied_anim()
        log_access("BREACH", target, "FAILED")
        return False

# ============================================
# BRUTE FORCE SIMULATOR
# ============================================
def brute_force_attack(target_user):
    print(f"\n{LR}{BL}⚡ BRUTE FORCE ATTACK INITIATED ⚡{X}\n")
    time.sleep(0.5)
    
    common_passwords = ["123456", "password", "admin", "qwerty", "letmein", "monkey", "dragon", "master", "123456789"]
    
    for i, pwd in enumerate(common_passwords):
        sys.stdout.write(f"\r{DG}[ATTEMPT {i+1}/{len(common_passwords)}] Trying: {pwd}...{X}")
        sys.stdout.flush()
        time.sleep(0.15)
        
        if target_user in USERS_DB and USERS_DB[target_user]["password"] == pwd:
            print(f"\n\n{G}╔══════════════════════════════╗")
            print(f"║   🔓 PASSWORD FOUND! 🔓   ║")
            print(f"║   User: {target_user:<18}║")
            print(f"║   Pass: {pwd:<18}║")
            print(f"╚══════════════════════════════╝{X}\n")
            log_access("BRUTEFORCE", target_user, "PASSWORD FOUND")
            return pwd
    
    print(f"\n\n{R}[✗] Password not in common list.{X}\n")
    log_access("BRUTEFORCE", target_user, "FAILED")
    return None

# ============================================
# PERMISSION ESCALATION
# ============================================
def permission_escalation(current_level):
    print(f"\n{Y}[*] Current Access Level: {current_level}{X}")
    print(f"{Y}[*] Attempting Privilege Escalation...{X}\n")
    
    matrix_rain(8, 0.01)
    countdown(3)
    progress_bar("ESCALATING PRIVILEGES", 2, 25)
    
    new_level = min(5, current_level + random.randint(1, 3))
    
    levels = ["GUEST", "USER", "OPERATOR", "ADMIN", "ROOT"]
    print(f"\n{G}╔══════════════════════════════════╗")
    typewriter(f"║  PRIVILEGE ESCALATED!      ║", G, 0.02)
    typewriter(f"║  {levels[current_level]:<8} → {levels[new_level]:<8}         ║", G, 0.02)
    print(f"{G}╚══════════════════════════════════╝{X}\n")
    log_access("ESCALATION", f"Level {current_level} → {new_level}", "SUCCESS")
    return new_level

# ============================================
# TOKEN GENERATOR / FORGER
# ============================================
def forge_token(user):
    print(f"\n{Y}[*] Forging Access Token...{X}")
    spinner(1, "Generating payload")
    
    token_data = f"{user}:{timestamp()}:{random.randint(1000,9999)}"
    token = base64.b64encode(token_data.encode()).decode()
    token_hash = hashlib.sha256(token.encode()).hexdigest()[:16]
    
    print(f"{C}╔═══ FORGED TOKEN ═══╗{X}")
    print(f"{C}║ {G}{token_hash}{C} ║{X}")
    print(f"{C}╚════════════════════╝{X}")
    log_access("TOKEN_FORGE", user, "SUCCESS")
    return token_hash

# ============================================
# BACKDOOR INSTALLER
# ============================================
def install_backdoor():
    print(f"\n{LR}{BL}⚠ INSTALLING BACKDOOR ⚠{X}\n")
    
    steps = ["Establishing persistence", "Creating hidden user", "Opening reverse shell port", "Disabling logs", "Encrypting backdoor"]
    
    for step in steps:
        spinner(0.8, step)
        time.sleep(0.2)
    
    port = random.randint(4444, 9999)
    print(f"\n{G}╔══════════════════════════════════╗")
    typewriter(f"║   BACKDOOR INSTALLED!      ║", G, 0.02)
    typewriter(f"║   Port: {port}              ║", G, 0.02)
    typewriter(f"║   Status: LISTENING        ║", G, 0.02)
    print(f"{G}╚══════════════════════════════════╝{X}\n")
    log_access("BACKDOOR", f"Port {port}", "INSTALLED")
    return port

# ============================================
# LOG VIEWER
# ============================================
def view_logs():
    print(f"\n{C}╔═══════════════════[ ACCESS LOGS ]═══════════════════╗{X}")
    if not ACCESS_LOGS:
        print(f"{C}║          No logs recorded yet.                     ║{X}")
    else:
        for log in ACCESS_LOGS:
            status_color = G if log['status'] == 'SUCCESS' or log['status'] == 'INSTALLED' or log['status'] == 'PASSWORD FOUND' else R
            print(f"{C}║ {DG}{log['time']} {W}{log['action']:<12} {DG}{log['detail']:<15} {status_color}{log['status']}{C} ║{X}")
    print(f"{C}╚════════════════════════════════════════════════════╝{X}\n")

# ============================================
# MENU
# ============================================
def show_menu():
    print(f"""
{Y}╔══════════════[ XES-CONTROL COMMANDS ]══════════════════╗
║                                                         ║
║  {W}01. Simulate Access Breach{R} 💀{Y}                           ║
║  {W}02. Brute Force Attack (Password Crack){R} 🔨{Y}              ║
║  {W}03. Privilege Escalation{R} 📈{Y}                             ║
║  {W}04. Forge Access Token{R} 🎫{Y}                               ║
║  {W}05. Install Backdoor{R} 🚪{Y}                                 ║
║  {W}06. Generate Strong Password{R} 🔑{Y}                         ║
║  {W}07. Password Strength Checker{R} 📊{Y}                        ║
║  {W}08. Hash Password (MD5/SHA256){R} 🔐{Y}                       ║
║  {W}09. View Access Logs{R} 📋{Y}                                 ║
║  {W}10. Clear All Logs/Tracks{R} 🧹{Y}                            ║
║                                                         ║
║  {DG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Y}  ║
║  {W}help  → Show Help                                    {Y}║
║  {W}clear → Clear Screen                                 {Y}║
║  {W}0     → Exit                                         {Y}║
║                                                         ║
╚═════════════════════════════════════════════════════════╝{X}
""")

# ============================================
# MAIN
# ============================================
def main():
    show_banner()
    
    # Startup sequence
    print(f"\n{DG}[{timestamp()}] Booting XES-CONTROL Framework...{X}")
    time.sleep(0.5)
    matrix_rain(10, 0.01)
    typewriter("\n[+] Loading exploit modules...", G, 0.02)
    typewriter("[+] Access control database connected.", G, 0.02)
    typewriter("[+] Encryption engines online.", G, 0.02)
    typewriter("[+] All systems ready.", G, 0.02)
    print(f"{LR}{BL}\n    ⚡ XES-CONTROL ACTIVATED ⚡{X}\n")
    time.sleep(0.5)
    
    current_level = 0  # Start as GUEST
    
    while True:
        show_menu()
        
        try:
            choice = input(f"{R}[{W}xes{R}@{W}control{R}]~# {G}").strip()
        except KeyboardInterrupt:
            print(f"\n\n{R}[!] EMERGENCY SHUTDOWN!{X}\n")
            break
            
        if choice == '0':
            print(f"\n{Y}[*] Wiping tracks...{X}")
            spinner(1, "Clearing logs")
            print(f"{G}[✓] All tracks erased. Exit.{X}\n")
            break
            
        elif choice == '1':
            target = input(f"{Y}[?] Target System/IP: {X}")
            print(f"{C}Methods: brute | exploit | bypass | inject{X}")
            method = input(f"{Y}[?] Attack Method: {X}").strip()
            simulate_breach(target, method)
            
        elif choice == '2':
            print(f"{C}Users in DB: admin | root | user | guest{X}")
            target_user = input(f"{Y}[?] Target Username: {X}").strip()
            brute_force_attack(target_user)
            
        elif choice == '3':
            current_level = permission_escalation(current_level)
            
        elif choice == '4':
            user = input(f"{Y}[?] Forge token for user: {X}").strip()
            forge_token(user)
            
        elif choice == '5':
            install_backdoor()
            
        elif choice == '6':
            length = int(input(f"{Y}[?] Password Length (8-32): {X}") or "16")
            print(f"{C}Complexity: low | medium | high{X}")
            comp = input(f"{Y}[?] Complexity: {X}").strip() or "high"
            spinner(0.5, "Generating password")
            pwd = generate_password(length, comp)
            print(f"\n{G}╔═══ GENERATED PASSWORD ═══╗")
            print(f"║  {pwd}  ║")
            print(f"╚══════════════════════════╝{X}\n")
            
        elif choice == '7':
            pwd = getpass(f"{Y}[?] Enter Password (hidden): {X}")
            spinner(0.5, "Analyzing strength")
            
            score = 0
            if len(pwd) >= 8: score += 1
            if len(pwd) >= 12: score += 1
            if any(c.isupper() for c in pwd): score += 1
            if any(c.islower() for c in pwd): score += 1
            if any(c.isdigit() for c in pwd): score += 1
            if any(c in string.punctuation for c in pwd): score += 1
            
            ratings = {0: (R, "VERY WEAK"), 1: (R, "WEAK"), 2: (Y, "FAIR"), 
                       3: (Y, "GOOD"), 4: (G, "STRONG"), 5: (G, "VERY STRONG"), 
                       6: (LG, "EXCELLENT")}
            
            color, rating = ratings.get(score, (R, "UNKNOWN"))
            bar = '█' * score + '░' * (6 - score)
            print(f"\n{color}[{bar}] {rating}{X}\n")
            
        elif choice == '8':
            text = input(f"{Y}[?] Text to Hash: {X}")
            algo = input(f"{Y}[?] Algorithm (md5/sha256): {X}").strip().lower()
            spinner(0.5, "Hashing")
            
            if algo == 'md5':
                result = hashlib.md5(text.encode()).hexdigest()
            else:
                result = hashlib.sha256(text.encode()).hexdigest()
            
            print(f"{G}[✓] {algo.upper()}: {result}{X}\n")
            log_access("HASH", algo.upper(), "GENERATED")
            
        elif choice == '9':
            view_logs()
            
        elif choice == '10':
            print(f"{Y}[*] Wiping all access logs...{X}")
            spinner(1, "Shredding logs")
            ACCESS_LOGS.clear()
            print(f"{G}[✓] All tracks erased.{X}\n")
            
        elif choice.lower() == 'help':
            print(f"""
{C}╔══════════════════[ XES-CONTROL HELP ]══════════════════╗
║                                                        ║
║  XES-CONTROL v3.0 - Access Control Framework           ║
║                                                        ║
║  MODULES:                                              ║
║  01. Breach Simulator  - Simulate system breach        ║
║  02. Brute Force       - Dictionary attack on DB       ║
║  03. Priv Escalation   - Raise access level            ║
║  04. Token Forge       - Generate fake access token    ║
║  05. Backdoor Install  - Simulate persistence          ║
║  06. Password Gen      - Create strong passwords       ║
║  07. Strength Check    - Analyze password security     ║
║  08. Hash Generator    - MD5/SHA256 hash               ║
║  09. View Logs         - See all actions               ║
║  10. Clear Logs        - Wipe tracks                   ║
║                                                        ║
║  ⚠ EDUCATIONAL USE ONLY - ETHICAL HACKING              ║
║                                                        ║
╚════════════════════════════════════════════════════════╝{X}
""")
            
        elif choice.lower() == 'clear':
            show_banner()
            
        else:
            print(f"{R}[✗] Invalid command!{X}\n")

# ============================================
# RUN
# ============================================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] ABORTED - All clear.{X}\n")
    except Exception as e:
        print(f"\n{R}[!] CRASH: {e}{X}\n")
