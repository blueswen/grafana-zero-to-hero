# Service Performance Monitoring

![Lab Architecture](lab-arch.png)

## Goals

1. Applications：各種搭配 OpenTelemetry SDK 的服務，透過 [Zero-code Instrumentation](https://opentelemetry.io/docs/zero-code/) 自動生成與發送 Trace 資訊到 OpenTelemetry Collector
   1. fastapi：Python FastAPI 服務
   2. spring-boot：Java Spring Boot 服務
   3. express：Node.js Express 服務
2. Grafana：Lab 操作
3. Prometheus：採集 OpenTelemetry Collector 的 Metrics
4. OpenTelemetry Collector
   1. 接收 Traces 資料，將 Traces 資料轉送至 Jaeger Collector 與 Tempo，並透過 Span Metrics Connector 產生 Metrics
   2. 接收 Span Metrics Connector 產生的 Metrics 資料，並揭露於自己的 8889 Port 供 Prometheus 爬取
5. Jaeger Components
   1. Jaeger Collector：接收 OpenTelemetry Collector 發送的 Traces 資料
   2. Jaeger Query：提供 UI 查看 Trace Data，並從 Prometheus 取得 Metrics 資料供 Jaeger SPM 使用
   3. Cassandra：儲存 Trace Data
   4. Cassandra Schema：初始化 Cassandra DB
6. Tempo：接收 OpenTelemetry Collector 發送的 Traces 資料
7. k6：使用 [k6](https://k6.io/) 持續對 Applications 發送 Request

## Quick Start

1. 啟動所有服務

   ```bash
   docker-compose up -d
   ```

2. 檢視服務
   1. Grafana: <http://localhost:3000>，登入帳號密碼為 `admin/admin`
      1. 點擊左上 Menu > Dashboards > Provision Dashboards 即可選擇預先建立的 Dashboard
   2. Jaeger Query: <http://localhost:16686/monitor>
      1. Jaeger Query 需要等待 Cassandra 初始化完成後才能正常運作
   3. k6 會根據 `k6/k6-script.js` 持續執行對 Applications 發送 Request 60 分鐘，如果已經停止可以透過 `docker-compose restart k6` 重新啟動
3. 關閉所有服務

   ```bash
   docker-compose down
   ```
