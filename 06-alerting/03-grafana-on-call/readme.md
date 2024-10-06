# Grafana OnCall

## Goals

1. Nginx：單純作為被監測的 Container
2. cAdvisor：收集 Container 資料
3. Node Exporter：收集運行的機器（Node）的資料
4. Prometheus：採集 cAdvisor 與 Node Exporter 的 Metrics
5. Grafana：Lab 操作
6. Grafana OnCall Components
   1. engine：Grafana OnCall 主要服務，API 都由此服務處理
   2. celery：執行排程工作
   3. oncall_db_migration：DB 相關處理，只有啟動時執行，非常駐服務
   4. redis：快取資料庫

### Quick Start

1. 將 `.env.template` 複製一份成 `.env` 並更新文件內 IP 的值為當下機器的 IP，以進行後續的 Slack Integration 和 Mobile App 登入設定
2. 啟動所有服務

   ```bash
   docker-compose up -d
   ```

3. 執行以下指令更新 Plugin 設定修復 [stackid Bug](https://github.com/grafana/oncall/issues/4843#issuecomment-2334875281)，IP 需替換成當下機器的 IP

   ```bash
   curl -X POST 'http://admin:admin@localhost:3000/api/plugins/grafana-oncall-app/settings' -H "Content-Type: application/json" -d '{"enabled":true, "jsonData":{"stackId":5, "orgId":100, "onCallApiUrl":"http://<IP>:8080/", "grafanaUrl":"http://<IP>:3000/"}}'
   curl -X POST 'http://admin:admin@localhost:3000/api/plugins/grafana-oncall-app/resources/plugin/install'
   ```

4. 登入 Grafana 設定與操作 Grafana OnCall
   1. Grafana: <http://localhost:3000>，登入帳號密碼為 `admin/admin`
   2. 在 Administration > Plugins and data > Plugins 頁籤搜尋 OnCall，啟用並進行連結，確認設定無誤
   3. 在 Alerts & IRM > OnCall > Integrations 建立 Grafana 的 Integration 與 Grafana Alerting 連動
      1. contact point 選擇 grafana-default-email
      2. 新增後設定一組 Escalation chain 供此 Integration 使用，Escalation chain Steps 可選擇通知 Admin
   4. 在 Alerts & IRM > OnCall > Settings 的 Chat Ops 設定 Slack Integration
   5. 從右上的 User Icon 進入 Profile 的 IRM 選單，設定 Grafana Cloud OnCall API，再透過 QR code 登入 Mobile App
   6. 使用預設的 Alert Rule `Memory Usage` 操作 Grafana OnCall 各項功能，也可以複製該 Alert Rule 測試 Grouping 等功能
5. 關閉所有服務

   ```bash
   docker-compose down
   ```
