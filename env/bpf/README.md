

## bcc

```
git clone git@github.com:iovisor/bcc.git
mkdir build && cd build
export LLVM_ROOT=/usr/lib/llvm-12/
cmake .. -DENABLE_SHARED=1
make -j8
make install

cmake -DPYTHON_CMD=python3 .. # build python3 binding
pushd src/python/
make
sudo make install
popd
```

use python3
```
rm /usr/bin/python
ln -s python3 /usr/bin/python
```

## bpftrace

```
git clone git@github.com:iovisor/bpftrace.git
git submodule update --init --recursive
mkdir build && cd build
../build-libs.sh
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j8
sudo make install
```
