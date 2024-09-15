# Dashboard 與 Monitoring 的最佳實踐

![Lab Architecture](lab-arch.png)

## Goals

此 Lab 會建立

1. Application：被監控的服務
2. cAdvisor：收集 Container 資料
3. Node Exporter：收集運行的機器（Node）的資料
4. Prometheus：採集 Application、cAdvisor、Node Exporter 的 Metrics
5. Grafana：查詢與顯示 Prometheus 採集到的 Metrics
6. k6：使用 [k6](https://k6.io/) 對 Application 持續發送 Request

## Quick Start

1. 啟動所有服務

   ```bash
   docker-compose up -d
   ```

2. 檢視服務
   1. Grafana：[http://localhost:3000](http://localhost:3000)，登入帳號密碼為 `admin/admin`
      1. 點擊左上 Menu > Dashboards > Provision Dashboards 再選擇 Monitoring Best Practice、cAdvisor exporter 或 Node Exporter Full，即可看到預先建立的 Dashboard
   2. Application：[http://localhost:8000/docs](http://localhost:8000/docs)，可以查看 API 文件，並透過 Swagger UI 測試 API
3. 模擬發送 Request，預設啟動時會持續發送 10 分鐘，若要再次發送可重新啟動 k6 container

   ```bash
   docker-compose start k6
   ```

4. 關閉所有服務

   ```bash
   docker-compose down
   ```

## Note

Grafana 資料會儲存在 `data` 目錄中，如果要將 Grafana 還原至初始狀態，可以將 `data` 目錄刪除。
