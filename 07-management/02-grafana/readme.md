# Grafana Self Monitoring and High Availability

## Goals

1. cAdvisor：收集 Container 資料
2. Node Exporter：收集運行的機器（Node）的資料
3. Prometheus：採集 cAdvisor、Node Exporter 與 Grafana 的 Metrics
4. Tempo：收集 Grafana 送出的 Trace 資訊
5. Nginx：Grafana 服務的入口，擔任 Load Balancer 將 Request 分散到 Grafana Instance 上
6. Grafana：grafana-node-1 和 grafana-node-2 兩個 Instance
7. Postgres：Grafana Instance 共用的資料庫
8. Redis：Grafana Instance 用來同步告警狀態的資料庫

### Quick Start

1. 啟動所有服務

   ```bash
   docker-compose up -d
   ```

2. 登入 Grafana 操作 Dashboard、Explore 功能與測試 Alert 是否有 HA 架構及不會重複發送
   1. Grafana: <http://localhost>，登入帳號密碼為 `admin/admin`
   2. 點擊左上 Menu > Dashboards > Provision Dashboards 查看 Grafana Stats 多個 Grafana Instance 的狀態
   3. 使用 Explore 查看 Grafana 產生的 Trace 資訊
   4. 停止一個 Grafana Container，確認 Grafana 仍可以正常檢視與發送 Alert
3. 關閉所有服務

   ```bash
   docker-compose down
   ```

## 參考資料

1. [Grafana alerting high availability examples](https://github.com/grafana/alerting-ha-docker-examples/tree/main)
