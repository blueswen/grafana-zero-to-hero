# User Management

## Goals

1. Nginx：單純作為被監測的 Container
2. cAdvisor：收集 Container 資料
3. Node Exporter：收集運行的機器（Node）的資料
4. Prometheus：採集 cAdvisor 與 Node Exporter 的 Metrics
5. Grafana：Lab 操作
6. lldap：測試用 LDAP Server

### Quick Start

1. 啟動所有服務

   ```bash
   docker-compose up -d
   ```

2. 登入 lldap 建立 LDAP 帳號供 Grafana 串接登入使用
   1. lldap: <http://localhost:17170>，登入帳號密碼為 `admin/password`
   2. 建立數組帳號
   3. 建立 Group：grafana_admin、grafana_editor，並將前面建立的帳號加入 Group 中
3. 登入 Grafana 設定與操作各種權限設定
   1. Grafana: <http://localhost:3000>，登入帳號密碼為 `admin/admin`
   2. 進入 Administration > Authentication 頁籤中選擇 LDAP，確認 lldap 上新增的帳號可以被查詢到
   3. 開啟無痕視窗用 lldap 新增的帳號登入
   4. 測試 Role、Team、Organization 等功能
4. 關閉所有服務

   ```bash
   docker-compose down
   ```
