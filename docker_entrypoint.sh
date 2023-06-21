#!/bin/bash

set -e

exec python light.py &
exec python dark.py 