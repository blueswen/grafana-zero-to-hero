# Data Source Basic

## Components

1. cAdvisor：收集 Container 資料，產生 Prometheus Metrics
2. Node Exporter：收集機器資料，產生 Prometheus Metrics
3. Prometheus：爬取並儲存 Prometheus Metrics
4. Grafana：查詢 Prometheus 上的 Metrics

## Goals

1. 查看預先建立好的 Prometheus Data Source 設定方式
2. 操作 Explore 查閱預先建立好的 Prometheus 與 TestData Data Source

## Quick Start

1. 啟動所有服務

   ```bash
   docker compose up -d
   ```

2. 檢視服務
   1. Grafana: <http://localhost:3000>，登入帳號密碼為 `admin/admin`

3. 關閉所有服務

   ```bash
   docker compose down
   ```
