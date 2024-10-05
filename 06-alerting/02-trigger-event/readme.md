# Alert Rules

![Lab Architecture](lab-arch.png)

## Goals

1. Nginx：單純作為被監測的 Container
2. cAdvisor：收集 Container 資料
3. Node Exporter：收集運行的機器（Node）的資料
4. Prometheus：採集 cAdvisor 與 Node Exporter 的 Metrics
5. Grafana：Lab 操作
6. Kafka Components
   1. Kafka：Kafka Server 接收訊息與供下游服務訂閱
   2. Zookeeper：Kafka 的依賴
   3. Kafka REST Proxy：提供 HTTP API Interface 操作 Kafka Server
   4. Redpanda Console：Kafka Server Web UI，用於檢視 Kafka Server 內容
   5. Application：模擬訂閱 Alerting 的下游服務
7. n8n：提供 Webhook 的自動化流程工具

### Quick Start

1. 啟動所有服務

   ```bash
   docker-compose up -d
   ```

2. 設定 Contact Point 與測試 Alert
   1. Grafana: <http://localhost:3000>，登入帳號密碼為 `admin/admin`
   2. Webhook
      1. 登入 n8n: [http://localhost:5678](http://localhost:5678)，建立帳號與設定一組起點為 Webhook 的 Workflow
      2. 在 Grafana 建立 Webhook Contact Point，n8n 的 Webhook URL 在編輯時使用的是 `Test URL`，Workflow 啟用後用的 URL 是 `Production URL`，並將 n8n 提供的 URL Domain 從 `localhost` 改為 `n8n`，在 `Optional Webhook settings` 將 　`HTTP Method` 設定為 `POST`
      3. 使用 Contact Point 的 Test 發送測試訊息驗證
   3. Kafka
      1. 在 Grafana 建立 Kafka REST Proxy Contact Point，URL 設定為 `http://rest-proxy:8082`，Topic 設定為 `grafana-alerting`
      2. 使用 Contact Point 的 Test 發送測試訊息驗證
      3. 開啟 Redpanda Console: <http://localhost:8080/> 在 Topic 頁籤中選擇 `grafana-alerting` Topic 查看測試訊息
      4. 檢視 Application 的 Container Log 查看 Topic 被訂閱後 Consume 印出的內容

3. 關閉所有服務

   ```bash
   docker-compose down
   ```
