#!/usr/bin/env python3
"""Extract and analyze Android kernel config from running device"""
import subprocess, re

def adb(cmd):
    r = subprocess.run(['adb', 'shell'] + cmd.split(), capture_output=True, text=True)
    return r.stdout.strip()

def get_kernel_config():
    raw = adb("cat /proc/config.gz")
    if not raw:
        raw = adb("zcat /proc/config.gz")
    
    configs = {}
    for line in raw.split('\n'):
        if '=' in line:
            k, v = line.split('=', 1)
            configs[k.strip()] = v.strip()
    return configs

print("Kernel configurations:")
for k, v in get_kernel_config().items():
    if 'SECURITY' in k or 'EXPLOIT' in k or 'HARDENING' in k:
        print(f"  {k}={v}")
