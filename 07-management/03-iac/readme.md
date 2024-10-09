# Grafana Infrastructure as Code

## Goals

1. Nginx：單純作為被監測的 Container
2. cAdvisor：收集 Container 資料
3. Node Exporter：收集運行的機器（Node）的資料
4. Prometheus：採集 cAdvisor 與 Node Exporter 的 Metrics
5. Grafana：Lab 操作

### Quick Start

1. 啟動所有服務

   ```bash
   docker-compose up -d
   ```

2. [安裝 Terraform CLI](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)，進入 `tf` 目錄執行以下指令

   ```bash
   # 下載 Grafana Provider 與 Terraform 初始化
   terraform init
   # Apply main.tf 中預先定義好的各種 Grafana 資源
   terraform apply
   ```

3. 登入 Grafana，驗證 `tf/main.tf` 中的 User、Folder、Dashboard、Alert 是否建立完成，並測試 Grafana API
   1. Grafana: <http://localhost:3000>，登入帳號密碼為 `admin/admin`
   2. 進入 Grafana 的 Swagger UI <http://localhost:3000/swagger> 測試各種 API

4. 關閉所有服務

   ```bash
   docker-compose down
   ```
