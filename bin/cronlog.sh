#!/usr/bin/env bash
# A simple wrapper to redirect cron STDOUT & STDERR to docker logs
set -eo pipefail
PATH=/usr/local/bin:/usr/bin:/bin:/sbin:/app/bin:$PATH
cd /app
bash "$@">/proc/1/fd/1 2>/proc/1/fd/2
