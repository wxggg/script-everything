#!/bin/sh

# For Focal (20.04.1 LTS)
sudo apt install -y bison build-essential cmake flex git libedit-dev \
  libllvm12 llvm-12-dev libclang-12-dev python zlib1g-dev libelf-dev libfl-dev python3-distutils

sudo apt install -y arping netperf iperf

sudo apt-get install -y libbpfcc-dev

sudo apt-get install -y \
  bison \
  cmake \
  flex \
  g++ \
  git \
  libelf-dev \
  zlib1g-dev \
  libfl-dev \
  systemtap-sdt-dev \
  binutils-dev \
  libcereal-dev \
  llvm-12-dev \
  llvm-12-runtime \
  libclang-12-dev \
  clang-12 \
  libpcap-dev \
  libgtest-dev \
  libgmock-dev \
  asciidoctor
