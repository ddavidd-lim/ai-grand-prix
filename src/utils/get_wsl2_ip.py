import subprocess


def get_wsl2_ip():
    result = subprocess.run(
        ["wsl", "hostname", "-I"],
        capture_output=True, text=True
    )
    
    
    return result.stdout.strip().split()[0]