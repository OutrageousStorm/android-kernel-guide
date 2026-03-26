# KernelSU — Kernel-Level Root

KernelSU is a root solution for Android that works at the kernel level, unlike Magisk which operates in userspace.

**Official site:** https://kernelsu.org  
**GitHub:** https://github.com/tiann/KernelSU

---

## How it works

```
Traditional root (Magisk):
  App requests root → Magisk daemon in userspace → grants su shell
  Detection: check for /sbin/su, Magisk files, process list

KernelSU:
  App requests root → kernel module intercepts syscall → grants privilege
  Detection: much harder — no userspace artifacts
```

KernelSU patches the kernel's `do_execve` and `vfs_read` functions to intercept privilege requests directly in the kernel, before userspace can observe them.

---

## KernelSU vs Magisk

| Feature | Magisk | KernelSU |
|---------|--------|----------|
| Root method | Userspace daemon | Kernel module |
| Detection resistance | Moderate (Shamiko needed) | High (kernel-level hiding) |
| Module support | Extensive (thousands) | Growing (compatible subset) |
| Zygisk support | Native | Via ZygiskNext module |
| GKI support | Yes | Yes (primary target) |
| Non-GKI support | Yes | Requires kernel source |
| SafetyNet/Play Integrity | Needs fix module | Needs fix module |

---

## Installation

### GKI devices (Android 12+ with GKI kernel)

1. Download the KernelSU boot image for your device from https://kernelsu.org
2. Flash via fastboot:
```bash
fastboot flash boot kernelsu-boot.img
```

### Non-GKI devices (older, needs kernel compilation)

1. Get your device's kernel source from the OEM or LineageOS
2. Apply KernelSU patch:
```bash
curl -LSs "https://raw.githubusercontent.com/tiann/KernelSU/main/kernel/setup.sh" | bash -
```
3. Compile kernel
4. Flash via recovery or fastboot

---

## Module system

KernelSU supports a Magisk-compatible module format. Most Magisk modules work with KernelSU if they don't rely on Magisk-specific APIs.

For Zygisk modules (Shamiko, LSPosed, etc.) install **ZygiskNext** first:
- GitHub: https://github.com/Dr-TSNG/ZygiskNext

---

## WebUI modules

KernelSU 0.7.0+ supports modules with a web-based UI — modules can expose a local web interface accessible from the KernelSU manager app. This is unique to KernelSU.

---

## Supported devices (GKI)

Any device running Android 12+ with a GKI-compliant kernel (5.10+). This includes:
- Pixel 6 and newer
- Samsung Galaxy S22 and newer (Exynos variants)
- OnePlus 10 and newer
- Xiaomi 12 and newer
- Most 2022+ flagships
