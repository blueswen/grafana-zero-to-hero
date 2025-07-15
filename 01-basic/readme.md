# Grafana 基礎操作

![Lab Architecture](lab-arch.png)

## Components

1. cAdvisor：收集 Container 資料，產生 Prometheus Metrics
2. Node Exporter：收集機器資料，產生 Prometheus Metrics
3. Nginx：範例應用程式
4. Prometheus：爬取並儲存 Prometheus Metrics
5. Grafana：查詢 Prometheus 上的 Metrics

## Goals

1. 熟悉 Grafana 基本操作與介面
2. 操作內建 Dashboard： Basic Dashboard、Cadvisor exporter、Node Exporter Full

## Quick Start

1. 啟動所有服務

   ```bash
   docker compose up -d
   ```

2. 檢視服務

   1. Grafana：[http://localhost:3000](http://localhost:3000)，登入帳號密碼為 `admin/admin`
      1. 點擊左上 Menu > Dashboards > Provision Dashboards 再選擇 Basic Dashboard、cAdvisor exporter 或 Node Exporter Full，即可看到預先建立的 Dashboard
   2. nginx：[http://localhost](http://localhost)，可以顯示 IP 與時間

3. 關閉所有服務

   ```bash
   docker compose down
   ```

## Note

Grafana 資料會儲存在 `data` 目錄中，如果要將 Grafana 還原至初始狀態，可以將 `data` 目錄刪除。
