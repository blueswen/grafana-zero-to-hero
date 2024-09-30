# DB Plugins

## Goals

此 Lab 會建立

1. PostgreSQL：PostgreSQL 資料庫 Service
2. PostgreSQL Exporter：負責採集 PostgreSQL 的指標並揭露
3. MySQL：MySQL 資料庫 Service
4. MySQL Server Exporter：負責採集 MySQL 的指標並揭露
5. Prometheus：採集 PostgreSQL Exporter、MySQL Server Exporter 的 Metrics
6. Grafana：
   1. 查看預先建立好的 PostgreSQL 與 MySQL Data Source 設定方式
   2. 操作 Explore 查閱預先建立好的 PostgreSQL 與 MySQL
   3. 查看 PostgreSQL 與 MySQL 的 Monitoring Dashboard 與 Visualization 示範 Dashboard

### Quick Start

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
