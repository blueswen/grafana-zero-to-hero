# Infinity

## Goals

此 Lab 會建立

1. Application：基礎的 API 供 Infinity 抓取資料
2. Grafana：查看預先建立好的示範 Dashboard 與 Infinity Data Source

### Quick Start

1. 啟動所有服務

   ```bash
   docker-compose up -d
   ```

2. 安裝 Infinity Data Source Plugin 與檢視服務
   1. Grafana: <http://localhost:3000>，登入帳號密碼為 `admin/admin`
      1. 點擊左上 Menu > Connections > Add new connection，搜尋 Infinity 並安裝
      2. 點擊左上 Menu > Dashboards > Provision Dashboards 即可選擇預先建立的 Dashboard
3. 關閉所有服務

   ```bash
   docker-compose down
   ```
