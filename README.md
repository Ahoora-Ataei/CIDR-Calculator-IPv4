<p align="center">
  <img src="./image/api.svg" alt="CIDR Calculator">
</p>

# CIDR Calculator

A simple Python CLI tool that takes an IPv4 address in CIDR notation and returns its network details, including the network address, broadcast address, first and last usable IPs, and total usable hosts.

<p align="center">
  <img src="./image/work.svg" alt="How CIDR Calculator works">
</p>

## Features

* Supports all IPv4 prefixes from `/0` to `/32`
* Correct handling of special cases (`/31` and `/32`)
* Displays network address and broadcast address
* Displays first and last usable IP
* Calculates total usable hosts
* Input validation with friendly error messages
* Interactive command-line interface

## Requirements

* Python 3.x
* No external packages required

The project uses Python's built-in `ipaddress` module.

## Usage

Run the program with:

```bash
python cidr_calculator.py
