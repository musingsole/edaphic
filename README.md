# edaphic

PyCom flavored Micropython tooling, operation libraries, task scheduler. Requires Linux (developed on Ubuntu), Python 3. Full expansion requirements

# Install

```
pip3 install edaphic
```

# Micropython Operational Platform

# Build Platform Framework

```
python3 -m edaphic build {board name}
```

## Limiting Memory Usage

```
python3 -m edaphic build {board name} --expansions {expansion_list} --include {lib_include_list} --exclude {lib_exclude_list}
```

# Installing Firmware on Board

```
# TODO: Can you identify available MicroPython clients on the network?
python3 -m edaphic firmware install
```

## Options

```
python3 -m edaphic firmware install --all --address {ip address | serial port} --rjoin --wipe --hard
```

### all

### address

A network IP address or serial device port of the device to install

### rjoin

### wipe

### hard

This option will trigger a full wipe of the device, device firmware upgrade, followed by installation of the edaphic system to the device. Requires the [address](#address) indicating serial device.

## Task Scheduler

## Operation Libraries

## Expansion Libaries
