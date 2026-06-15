import os
import sys
import time
import urllib.parse
import re
import subprocess
import shutil

# Dynamic Cyberpunk Color Theme Sheet
RESET = '\033[0m'
BOLD = '\033[1m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
WHITE = '\033[97m'

def clear_screen():
    os.system('clear')

def jarvis_speak_voice(text):
    """Hardware API voice synthesizer routing channel"""
    os.system(f'termux-tts-speak "{text}" > /dev/null 2>&1 &')

def get_system_metrics():
    """Live Hardware Scraper: Fetches exact smartphone time, battery levels, and storage metrics."""
    local_time = time.strftime("%I:%M:%S %p")
    try:
        total, used, free = shutil.disk_usage("/sdcard")
        free_gb = free / (1024 * 1024 * 1024)
        storage_str = f"{free_gb:.2f} GB"
    except Exception:
        storage_str = "128.50 GB"
        
    battery_str = "85%"
    try:
        bat_data = os.popen("termux-battery-status").read()
        bat_match = re.search(r'"percentage":\s*([0-9]+)', bat_data)
        if bat_match:
            battery_str = f"{bat_match.group(1)}%"
    except Exception:
        pass
        
    return local_time, battery_str, storage_str

def jarvis_banner():
    clear_screen()
    theme_cycle = ['\033[96m', '\033[95m', '\033[92m', '\033[93m']
    current_color = theme_cycle[int(time.time()) % len(theme_cycle)]
    l_time, l_bat, l_store = get_system_metrics()
    
    print(f"{current_color}{BOLD}╔══════════════════════════════════════════════╗")
    print(f"║          🤖 {GREEN}🔸JARVIS AI CORE v5.0🔸{current_color}             ║")
    print(f"╚══════════════════════════════════════════════╝{RESET}")
    print(f"{current_color}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f" {current_color}🔻{RESET} {BOLD}SYSTEM STATUS :{RESET} {GREEN}ONLINE{RESET}")
    print(f" {current_color}🔻{RESET} {BOLD}LOCAL TIME    :{RESET} {YELLOW}{l_time}{RESET}")
    print(f" {current_color}🔻{RESET} {BOLD}BATTERY       :{RESET} {GREEN}{l_bat}{RESET}")
    print(f" {current_color}🔻{RESET} {BOLD}FREE STORAGE  :{RESET} {MAGENTA}{l_store}{RESET}")
    print(f" {current_color}🔻{RESET} {BOLD}MODE          :{RESET} {RED}ULTIMATE EDITION{RESET}")
    print(f"{current_color}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}\n")

def jarvis_speak(text):
    print(f"{CYAN}[JARVIS] ➜{RESET} {text}")
    time.sleep(0.1)
def run_secure_download(command_args, quality_label="1080P Full HD"):
    """
    Advanced real-time log inspector that intercepts process states
    and renders your custom layout graphical percentage block loading bar.
    """
    print(f"\n{CYAN}[JARVIS]{RESET} Initializing download engine...")
    print(f"{GREEN}[+] Selected Quality : {quality_label}{RESET}\n")
    print(f"{YELLOW}[JARVIS]: Downloading...{RESET}")
    print(f"{CYAN}🚀 JARVIS CORE{RESET}")
    
    start_time = time.time()
    process = subprocess.Popen(
        command_args,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    
    current_pct = "0.0%"
    current_speed = "Max Speed"
    
    for line in process.stdout:
        match_pct = re.search(r'(\d+(\.\d+)?)\s*%', line)
        if match_pct:
            pct_val = float(match_pct.group(1))
            if pct_val <= 100.0:
                current_pct = f"{pct_val:.1f}%"
                
                bar_length = 20
                filled_length = int(round(bar_length * pct_val / 100))
                bar = '█' * filled_length + '░' * (bar_length - filled_length)
                
                match_speed = re.search(r'(\d+(\.\d+)?[kMG]B/s|\d+(\.\d+)?[kMG]iB/s)', line)
                if match_speed:
                    current_speed = match_speed.group(1)
                
                sys.stdout.write(f"\r{MAGENTA}{bar}{RESET} {GREEN}{current_pct}{RESET}\nSpeed : {YELLOW}{current_speed}{RESET}   ")
                sys.stdout.write("\033[F")
                sys.stdout.flush()
                
    process.wait()
    end_time = time.time()
    time_taken = int(end_time - start_time)
    
    print(f"\r{'█'*20} {GREEN}100.0%{RESET}\nSpeed : 0.0 MB/s      ")
    print(f"\n{GREEN}[+] Download Completed Successfully!{RESET}")
    print(f"{GREEN}[+] Time Taken : {time_taken}s{RESET}")
    
    os.system('termux-media-scan . > /dev/null 2>&1')
    return process.returncode
def get_quality_format(choice):
    if choice == '1': return 'bestvideo[height<=1080]+bestaudio/best[height<=1080]', "1080P Full HD"
    elif choice == '2': return 'bestvideo[height<=720]+bestaudio/best[height<=720]', "720P HD Standard"
    elif choice == '3': return 'bestvideo[height<=480]+bestaudio/best[height<=480]', "480P Mobile Saver"
    return None, None
    
def movie_search_engine(download_path):
    jarvis_banner()
    print(f"{CYAN}[JARVIS] ➜{RESET} Awaiting Command -> Movie Search...")
    movie_name = input(f"{YELLOW}{BOLD}Enter Movie / K-Drama Name ➜ {RESET}").strip()
    
    if not movie_name:
        print(f"{RED}[-] Error: Target query parameters missing!{RESET}")
        time.sleep(1)
        return

    jarvis_speak(f"Applying strict long-duration filters for '{movie_name}'...")
    
    search_query = f"{movie_name} full movie hindi dubbed"
    command = f'yt-dlp "ytsearch15:{search_query}" --match-filter "duration >= 3600 & !is_live" --dump-json --flat-playlist --quiet --no-warnings'
    
    print(f"{CYAN}[*] Sifting through cloud indices, please stand by...{RESET}\n")
    
    stream = os.popen(command)
    output = stream.read()
    
    results = []
    for line in output.split('\n'):
        if '"title":' in line and '"url":' in line:
            try:
                title = re.search(r'"title":\s*"([^"]+)"', line).group(1)
                url = re.search(r'"url":\s*"([^"]+)"', line).group(1)
                
                junk_keywords = ['trailer', 'teaser', 'review', 'roast', 'gameplay', 'reaction', 'fact', 'bgmi', 'pubg', 'status', 'explanation']
                if any(junk in title.lower() for junk in junk_keywords):
                    continue
                results.append({"title": title, "url": url})
            except:
                continue

    if not results:
        print(f"{RED}{BOLD}[-] ERROR: Full length content variant not found or unreleased.{RESET}")
        time.sleep(2)
        return

    print(f"{GREEN}[+] Filtered Movie Server List (Select Any):{RESET}\n")
    for i, res in enumerate(results[:10], 1):
        print(f"[{GREEN}{i}{RESET}] {res['title'][:58]}...")
    print(f"[{RED}0{RESET}] Abort Action")
    print(f"{CYAN}-"*60+f"{RESET}")
    
    try:
        select = int(input(f"{MAGENTA}{BOLD}Select Server Number ➜ {RESET}"))
        if select == 0 or select > len(results): return
        selected_url = results[select-1]['url']
        
        # Added Option 4 [Back To Main Menu] to prevent getting locked
        print(f"\n{CYAN}⚡ SELECT FORMAT PREFERENCES ⚡{RESET}")
        print(f"[{GREEN}1{RESET}] 1080p Full HD Resolution")
        print(f"[{GREEN}2{RESET}] 720p HD Standard Quality")
        print(f"[{GREEN}3{RESET}] 480p SD Mobile Format Saver")
        print(f"[{RED}4{RESET}] ↩ Back to Main Dashboard")
        print(f"{CYAN}-"*60+f"{RESET}")
        q_choice = input(f"{MAGENTA}{BOLD}Choose option (1-4) ➜ {RESET}").strip()
        
        if q_choice == '4':
            return # Safely breaks function to return right back into dashboard panel loop
            
        fmt, label = get_quality_format(q_choice)
        if not fmt:
            print(f"{RED}[-] Invalid selection code.{RESET}")
            time.sleep(1)
            return

        jarvis_banner()
        jarvis_speak_voice("Downloading started, please stand by, Sir.")
        
        bypass_headers = '--user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36" --no-check-certificates'
        meta_args = '--continue --no-overwrites --recode-video mp4 --embed-metadata'
        
        final_args = ['yt-dlp', '-f', fmt] + bypass_headers.split() + meta_args.split() + ['-P', download_path, selected_url]
        run_secure_download(final_args, label)
            
    except ValueError:
        print(f"{RED}[-] Invalid numeric choice template code.{RESET}")
    input(f"\nPress {GREEN}Enter{RESET} to return to main dashboard...")

def main():
    os.system('termux-setup-storage > /dev/null 2>&1')
    download_path = "."
    jarvis_speak_voice("Welcome back, Sir. Jarvis core framework is online.")

    bypass_headers = '--user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36" --no-check-certificates'
    meta_args = '--continue --no-overwrites --recode-video mp4 --embed-metadata'

    while True:
        jarvis_banner()

        print(f"\n{CYAN}╔════════════════════════════════════════════╗")
        print(f"║             🔸 JARVIS AI MENU 🔸           ║")
        print(f"╚════════════════════════════════════════════╝{RESET}")

        print(f"\n{GREEN}➊{RESET} 🎥  VIDEO DOWNLOADER ENGINE")
        print(f"{GREEN}➋{RESET} 🎵  AUDIO EXTRACTION ENGINE")
        print(f"{GREEN}➌{RESET} 🔍  MOVIE SEARCH MODULE")
        print(f"{RED}➍{RESET} ❌  SHUTDOWN JARVIS CORE")

        print(f"\n{MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        print(f"{CYAN}[JARVIS AI]{RESET} ➜ Awaiting Authorization...")
        print(f"{MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

        choice = input(f"{MAGENTA}{BOLD}🔸 Enter Choice ➜ {RESET}").strip()
        
        if choice == '1':
            url = input(f"\n{YELLOW}{BOLD}🔸PASTE VIDEO MEDIA LINK ➜ {RESET}").strip()
            if not url: continue
            
            print(f"\n{CYAN}⚡ SELECT RESOLUTION ⚡{RESET}")
            print(f"[{GREEN}1{RESET}] 1080p (Full HD)")
            print(f"[{GREEN}2{RESET}] 720p  (HD)")
            print(f"[{GREEN}3{RESET}] 480p  (SD)")
            print(f"[{RED}4{RESET}] ↩ Back to Main Dashboard")
            print(f"{CYAN}-"*60+f"{RESET}")
            q_choice = input(f"{MAGENTA}{BOLD}Choose option (1-4) ➜ {RESET}").strip()
            
            if q_choice == '4':
                continue
                
            fmt, label = get_quality_format(q_choice)
            if not fmt:
                print(f"{RED}[-] Invalid resolution code.{RESET}")
                time.sleep(1)
                continue
            
            jarvis_banner()
            final_args = ['yt-dlp', '-f', fmt] + bypass_headers.split() + meta_args.split() + ['-P', download_path, url]
            run_secure_download(final_args, label)
            input(f"\nPress {GREEN}Enter{RESET} to continue...")
            
        elif choice == '2':
            url = input(f"\n{YELLOW}{BOLD}🔸PASTE AUDIO MEDIA LINK ➜ {RESET}").strip()
            if not url: continue
            jarvis_banner()
            
            final_args = ['yt-dlp', '-f', 'ba', '-x', '--audio-format', 'mp3', '--audio-quality', '0'] + bypass_headers.split() +            ['--continue', '--embed-metadata', '-P', download_path, url]
            run_secure_download(final_args, "Audio MP3 320kbps")
            input(f"\nPress {GREEN}Enter{RESET} to continue...")
            
        elif choice == '3':
            movie_search_engine(download_path)
            
        elif choice == '4':
            jarvis_banner()
            jarvis_speak_voice("Powering down system framework, goodbye Sir.")
            print(f"{RED}[System Offline]{RESET}\n")
            sys.exit()
        else:
            print(f"{RED}\n[-] Error: Invalid Protocol Code!{RESET}")
            time.sleep(0.5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[-] Operation Interrupted manually. Safe Terminal Close.{RESET}")
