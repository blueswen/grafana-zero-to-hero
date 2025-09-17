# Business Suite

## Components

1. Grafana：預設安裝 Business Suite Plugins

## Goals

1. 使用 Explore 功能查詢 Business Input Data Source
2. 操作內建 Business Suite Dashboard

### Quick Start

1. 啟動所有服務

   ```bash
   docker compose up -d
   ```

2. 檢視服務
   1. Grafana: <http://localhost:3000>，登入帳號密碼為 `admin/admin`
      1. 點擊左上 Menu > Dashboards > Provision Dashboards 即可選擇預先建立的 Dashboard
3. 關閉所有服務並清除 Data Volume

   ```bash
   docker compose down -v
   ```
