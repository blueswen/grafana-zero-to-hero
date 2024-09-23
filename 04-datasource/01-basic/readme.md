# Data Source Basic

## Goals

此 Lab 會建立

1. cAdvisor：收集 Container 資料
2. Node Exporter：收集運行的機器（Node）的資料
3. Prometheus：採集 cAdvisor、Node Exporter 的 Metrics
4. Grafana：
   1. 查看預先建立好的 Prometheus Data Source 設定方式
   2. 操作 Explore 查閱預先建立好的 Prometheus 與 TestData

## Quick Start

1. 啟動所有服務

   ```bash
   docker-compose up -d
   ```

2. 檢視服務
   1. Grafana: <http://localhost:3000>，登入帳號密碼為 `admin/admin`

3. 關閉所有服務

   ```bash
   docker-compose down
   ```
