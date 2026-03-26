# Building a Custom Android Kernel

How to cross-compile a custom Android kernel on Linux.

---

## Prerequisites

```bash
# Ubuntu/Debian
sudo apt install git build-essential libncurses-dev bison flex   libssl-dev libelf-dev bc python3 python3-pip zip unzip curl wget

# Install Android NDK (for cross-compilation toolchain)
# Download from: https://developer.android.com/ndk/downloads
```

---

## Get kernel source

```bash
# From LineageOS (example: Pixel 7)
git clone https://github.com/LineageOS/android_kernel_google_gs201 -b lineage-21

# Or from Google
git clone https://android.googlesource.com/kernel/gs -b android13-5.15

# Check your device's codename for the right repo
```

---

## Get toolchain

```bash
# Google's Clang toolchain (recommended for modern kernels)
git clone --depth=1 https://github.com/ClangBuiltLinux/tc-build
cd tc-build
./build-llvm.py
cd ..

# Or use prebuilt
git clone --depth=1 https://github.com/ZyCromerZ/Clang-17 clang-17
```

---

## Build script (minimal)

```bash
#!/bin/bash
# build.sh — simple kernel build script

KERNEL_DIR=$(pwd)
CLANG_DIR="$HOME/clang-17"
OUT_DIR="$KERNEL_DIR/out"
ARCH="arm64"
DEFCONFIG="vendor/kalama_GKI.config"  # change for your device

export PATH="$CLANG_DIR/bin:$PATH"
export CROSS_COMPILE=aarch64-linux-gnu-
export CROSS_COMPILE_ARM32=arm-linux-gnueabi-
export CLANG_TRIPLE=aarch64-linux-gnu-
export CC=clang
export ARCH=$ARCH

# Generate config
make O=$OUT_DIR ARCH=$ARCH $DEFCONFIG

# Optional: open menuconfig to customize
# make O=$OUT_DIR ARCH=$ARCH menuconfig

# Build
make O=$OUT_DIR ARCH=$ARCH -j$(nproc) 2>&1 | tee build.log

echo "Kernel: $OUT_DIR/arch/arm64/boot/Image.gz-dtb"
```

---

## Package into AnyKernel3 zip

```bash
git clone https://github.com/osm0sis/AnyKernel3
cp out/arch/arm64/boot/Image.gz-dtb AnyKernel3/
cd AnyKernel3
# Edit anykernel.sh with your device codename
zip -r9 custom-kernel.zip * -x .git
```

---

## Flash

```bash
# Via custom recovery (TWRP)
adb sideload custom-kernel.zip

# Via fastboot (if ROM supports it)
fastboot flash boot out/arch/arm64/boot/boot.img
```

---

## Common build errors

| Error | Fix |
|-------|-----|
| `No rule to make target` | Wrong defconfig name |
| `clang: not found` | PATH not set correctly |
| `include/linux/compiler.h: No such file` | Missing kernel headers, check submodules |
| `scripts/dtc/dtc: Permission denied` | `chmod +x scripts/dtc/dtc` |
| Out of memory | Reduce `-j` value or add swap |
