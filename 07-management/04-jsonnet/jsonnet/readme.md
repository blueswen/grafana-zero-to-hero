# Jsonnet

## Requirements

1. [Jsonnet](https://github.com/google/go-jsonnet)
2. [jsonnet-bundler](https://github.com/jsonnet-bundler/jsonnet-bundler/)

## Quick Start

```bash
# Install packages
jb install github.com/grafana/grafonnet-lib@main
# Generate Grafana Dashboard
jsonnet -J vendor dashboard.libsonnet
# Generate Grafana Dashboard to output directory
mkdir output
jsonnet -J vendor dashboard.libsonnet > output/dashboard.json
```
