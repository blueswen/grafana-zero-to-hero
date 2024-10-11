# Gatus

## Goals

1. Prometheus：採集 Gatus 的 Metrics
2. Grafana：Lab 操作
3. Gatus：對指定網站定時檢查，並提供 Status Page

### Quick Start

1. 啟動所有服務

   ```bash
   docker-compose up -d
   ```

2. 檢視服務
   1. Gatus: <http://localhost:8080>，檢視 Gatuts Status Page
   2. Grafana: <http://localhost:3000>，登入帳號密碼為 `admin/admin`
      1. 點擊左上 Menu > Dashboards > Provision Dashboards 即可選擇預先建立的 Dashboard

3. 關閉所有服務

   ```bash
   docker-compose down
   ```
