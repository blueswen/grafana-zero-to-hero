# SQL Expression

## Components

1. cAdvisor：收集 Container 資料，產生 Prometheus Metrics
2. Node Exporter：收集機器資料，產生 Prometheus Metrics
3. Prometheus：爬取並儲存 Prometheus Metrics
4. Grafana：查詢 Prometheus 上的 Metrics


## Goals

1. 利用 SQL Expressions 功能合併 TestData 與 Prometheus Data Source 查詢結果
2. 操作內建 Dashboard：SQL Expression、Cadvisor exporter 與 Node Exporter Full Dashboard

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
