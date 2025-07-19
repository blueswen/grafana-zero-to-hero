# Grafana Dashboard as Code

## Jsonnet

### Goals

1. 使用 Jsonnet 編譯生成 Grafana Dashboard

### Quick Start

1. 啟動所有服務

   ```bash
   docker compose up -d
   ```

2. 編譯 Jsonnet 撰寫的 Dasboard
   1. 安裝 [Jsonnet](https://github.com/google/go-jsonnet) 與 [jsonnet-bundler](https://github.com/jsonnet-bundler/jsonnet-bundler/)
   2. 進入 `jsonnet` 目錄，執行以下指令安裝 [grafonnet](https://github.com/grafana/grafonnet) 並編譯 Dashboard 生成 JSON 檔案

      ```bash
      jb install github.com/grafana/grafonnet-lib@main
      mkdir output
      jsonnet -J vendor dashboard.libsonnet > output/dashboard.json
      ```

3. 登入 Grafana 匯入生成的 Dashboard
   1. Grafana: <http://localhost>，登入帳號密碼為 `admin/admi`
4. 關閉所有服務

   ```bash
   docker compose down
   ```

## Grizzly

> [!WARNING]  
> [Grizzly](https://github.com/grafana/grizzly) 已經於 2025-05-12 標記為 Deprecation，相關功能會由 [grafanactl](https://github.com/grafana/grafanactl) 取代，以下 Grizzly 相關內容僅用於參考

### Goals

1. 於 Grizzly Container 操作 `grr` 指令

### Quick Start

1. 啟動所有服務

   ```bash
   docker compose -f docker-compose.grizzly.yaml up -d
   ```

2. 編譯 Jsonnet 撰寫的 Dasboard
   1. 安裝 [Jsonnet](https://github.com/google/go-jsonnet) 與 [jsonnet-bundler](https://github.com/jsonnet-bundler/jsonnet-bundler/)
   2. 進入 `jsonnet` 目錄，執行以下指令安裝 grafonnet 並編譯 Dashboard 生成 JSON 檔案

      ```bash
      jb install github.com/grafana/grafonnet-lib@main
      mkdir output
      jsonnet -J vendor dashboard.libsonnet > output/dashboard.json
      ```

3. 登入 Grafana 匯入生成的 Dashboard
   1. Grafana: <http://localhost>，登入帳號密碼為 `admin/admi`
4. 進入 Grizzly Container 操作 `grr` 指令
   1. push：推送編譯後生成的 Dashboard 到 Grafana 中

      ```bash
      grr config create-context destination
      grr config set grafana.url http://grafana:3000
      grr config set grafana.user admin
      grr config set grafana.token admin
      grr config set targets Dashboard
      grr push output/
      ```

   2. watch：監視 `jsonnet` 目錄下檔案是否有異動，發生異動時重新編譯 `dashboard.libsonnet` 後同步至 Grafana 中，可以嘗試編輯 `dashboard.libsonnet` 確認效果

      ```bash
      grr watch ./ dashboard.libsonnet
      ```

5. 關閉所有服務

   ```bash
   docker compose -f docker-compose.grizzly.yaml down
   ```

## Note

Grafana 資料會儲存在 `data` 目錄中，如果要將 Grafana 還原至初始狀態，可以將 `data` 目錄刪除。
