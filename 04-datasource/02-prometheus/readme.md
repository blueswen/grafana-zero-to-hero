# Prometheus

## Goals

此 Lab 會建立

1. Application：被監控的服務
2. cAdvisor：收集 Container 資料
3. Node Exporter：收集運行的機器（Node）的資料
4. Prometheus：採集 cAdvisor、Node Exporter 的 Metrics
5. Grafana：
   1. 查看預先建立好的 Prometheus Data Source 設定方式與 Dashboard

## Quick Start

1. 啟動所有服務

   ```bash
   docker-compose up -d
   ```

2. 檢視服務

   1. Grafana: <http://localhost:3000>，登入帳號密碼為 `admin/admin`
      1. 點擊左上 Menu > Dashboards > Provision Dashboards 即可選擇預先建立的 Dashboard

3. 關閉所有服務

   ```bash
   docker-compose down
   ```
