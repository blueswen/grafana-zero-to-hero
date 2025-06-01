# Alert Rules

## Goals

1. Nginx：單純作為被監測的 Container
2. cAdvisor：收集 Container 資料
3. Node Exporter：收集運行的機器（Node）的資料
4. Prometheus：採集 cAdvisor 與 Node Exporter 的 Metrics
5. Grafana：Lab 操作，查看 Alert Rules、Contact Points、Notification Policies 設定
6. Grafana Renderer：搭配 Alerting 截取 Panel 圖片

### Quick Start

1. 複製 `etc/grafana/grafana.ini.template` 為 `etc/grafana/grafana.ini` 並更新其中 smtp 的 username 與 password，password 需使用 Google Account 的應用程式密碼
2. 更新 `etc/grafana/alerting/contact-points.yaml` 中的 `example@email.com` 為自己的 Email
3. 啟動所有服務

   ```bash
   docker-compose up -d
   ```

4. 檢視服務與 Alert 設定
   1. Grafana: <http://localhost:3000>，登入帳號密碼為 `admin/admin`
   2. 預先透過 Provisioning 設定的 Alert Rules、Contact Points、Notification Policies，無法直接從 UI 更改，但可以透過 Duplicate 或 View 檢視設定內容

5. 關閉所有服務

   ```bash
   docker-compose down
   ```
