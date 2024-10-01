# Plugins

## Goals

此 Lab 會建立

1. Redis：Redis 服務
2. app-plugin：demo 用 app plugin 的編譯環境與 dev 運行環境，修改內容可以即時生效，首次運行會需要下載 Package，App Plugin 不會馬上顯示
3. Grafana：操作 Redis Application、Grafana Resources Exporter、Demo App

### Quick Start

1. 啟動所有服務

   ```bash
   docker-compose up -d
   ```

2. 檢視服務
   1. Grafana: <http://localhost:3000>，登入帳號密碼為 `admin/admin`
      1. 點擊左上 Menu > Administration > Plugins and data > Plugins 搜尋 Redis Application、Resources Exporter、Demo-App 安裝並啟用
      2. 啟用後可以在 Menu 選單中看到 Apps 類別，可以再選擇想要查看的 Application

3. 關閉所有服務

   ```bash
   docker-compose down
   ```
