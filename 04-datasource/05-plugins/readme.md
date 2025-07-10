# Data Source Plugins

## Goals

此 Lab 會建立

1. Redis：Redis 資料庫 Service
2. Application：基礎的 API 供 Infinity Data Source 抓取資料
3. Grafana：Grafana Service
   1. Data Source
      - SQLite
      - Google Sheets
      - Redis
      - Infinity
   2. Dashboard
      - Plugins: 使用 SQLite、Google Sheets、Redis Data Source
      - Infinity：使用 Infinity Data Source

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
