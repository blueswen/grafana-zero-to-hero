# Grafana Dashboard

## Goals

此 Lab 會建立

1. cAdvisor：收集 Container 資料
2. Node Exporter：收集運行的機器（Node）的資料
3. Prometheus：採集 Application、cAdvisor、Node Exporter 的 Metrics
4. Grafana：
   1. 操作各種預先建立的 Visualization 示範與練習 Dashboard
   2. 查詢與顯示 Prometheus 採集到的 Metrics

## Quick Start

1. 啟動所有服務

   ```bash
   docker-compose up -d
   ```

2. 檢視服務
   1. Grafana: [http://localhost:3000](http://localhost:3000)，登入帳號密碼為 `admin/admin`
      1. 點擊左上 Menu > Dashboards > Provision Dashboards 即可選擇預先建立的 Dashboard

3. 關閉所有服務

   ```bash
   docker-compose down
   ```

## Note

Grafana 資料會儲存在 `data` 目錄中，如果要將 Grafana 還原至初始狀態，可以將 `data` 目錄刪除。
