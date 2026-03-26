# ⚙️ Android Kernel Guide

Everything about Android kernels — building, flashing, tuning, and KernelSU.

---

## What is the Android kernel?

Android runs on a modified Linux kernel. The kernel manages:
- CPU scheduling and frequency scaling
- Memory management
- I/O and storage drivers
- Display, camera, and sensor drivers
- Network stack

Custom kernels can improve performance, battery life, add features, or enable root (KernelSU).

---

## Key concepts

| Term | Meaning |
|------|---------|
| **Governor** | Controls how the CPU scales frequency based on load |
| **Scheduler** | Decides which tasks get CPU time and when |
| **Overclock** | Run CPU/GPU above factory speeds |
| **Undervolt** | Run at lower voltage → less heat, better battery |
| **KernelSU** | Root method that lives in the kernel, not userspace |
| **GKI** | Generic Kernel Image — Google's standardized kernel (Android 12+) |

---

## CPU governors

| Governor | Best for | Behavior |
|----------|----------|---------|
| **schedutil** | Daily driver (stock) | Frequency follows scheduler utilization signal |
| **interactive** | Responsiveness | Ramps up fast, holds for a bit before scaling down |
| **performance** | Max performance | Always at max frequency |
| **powersave** | Battery | Always at min frequency |
| **conservative** | Balance | Steps up gradually, steps down fast |
| **ondemand** | Legacy default | Jumps to max on load, scales down slowly |

**Best for most:** `schedutil` (modern) or `interactive` (older kernels)

---

## I/O schedulers

| Scheduler | Best for |
|-----------|---------|
| **cfq** | Spinning HDD (legacy) |
| **deadline** | SSDs / eMMC |
| **noop** | Flash storage (simplest) |
| **bfq** | Responsiveness (desktop-style) |
| **mq-deadline** | Modern multi-queue SSDs |

```bash
# Check current scheduler
cat /sys/block/sda/queue/scheduler

# Change scheduler (requires root)
echo "deadline" > /sys/block/sda/queue/scheduler
```

---

## Popular custom kernels (by device)

| Device | Kernel | Features |
|--------|--------|---------|
| Pixel 6/7 | [Raviole Kernel](https://github.com/GrapheneOS/kernel_google_gs101) | GrapheneOS hardened |
| OnePlus 9 Pro | Sultan Kernel | OC, UV, KCAL |
| Samsung S21 | Kirisakura | Gaming optimized |
| Xiaomi POCO F3 | Mochi Kernel | OC, UV, BT fixes |
| Generic | [KernelSU](https://kernelsu.org) | Kernel-level root |

---

## Sections

- [KernelSU](docs/kernelsu.md) — Kernel-level root, how it works vs Magisk
- [Building a Kernel](docs/building.md) — Cross-compile from source on Linux
- [Tuning Guide](docs/tuning.md) — Governors, schedulers, thermal, I/O tweaks
- [GKI](docs/gki.md) — Generic Kernel Image explained

---

*See also: [ROM Haven wiki](https://romhaven.wikioasis.org) · [android-rom-guide](https://github.com/OutrageousStorm/android-rom-guide)*
