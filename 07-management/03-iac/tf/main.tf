terraform {
  required_providers {
    grafana = {
      source  = "grafana/grafana"
      version = "3.25.4"
    }
  }
}

# Authenticate to Grafana
provider "grafana" {
  url  = var.grafana_url
  auth = var.grafana_auth
}

# Create user
resource "grafana_user" "viewer01" {
  name     = "viewer01"
  email    = "viewer01@example.com"
  login    = "viewer01"
  password = "testtest"
}

resource "grafana_user" "editor01" {
  name     = "editor01"
  email    = "editor01@example.com"
  login    = "editor01"
  password = "testtest"
}

# Role

resource "grafana_organization" "main" {
  name         = "Main Org."
  admin_user   = "admin"
  admins = [
    "admin@localhost"
  ]
  editors = [
    "editor01@example.com"
  ]
  viewers = [
    "viewer01@example.com"
  ]
  depends_on = [ grafana_user.editor01, grafana_user.viewer01 ]
}

# Data source
resource "grafana_data_source" "prometheus" {
  name = "prometheus"
  type = "prometheus"
  url = "http://prometheus:9090"
}

resource "grafana_data_source" "testdata" {
  name = "testdata"
  type = "testdata"
}

# Folder
resource "grafana_folder" "tf" {
  title = "Terraform Folder"
}

# Dashboard
resource "grafana_dashboard" "basic" {
  config_json = file("dashboards/Basic Dashboard.json")
  folder = grafana_folder.tf.id
  overwrite = true
}

resource "grafana_dashboard" "cadvisor" {
  config_json = file("dashboards/Cadvisor exporter.json")
  folder = grafana_folder.tf.id
  overwrite = true
}

resource "grafana_dashboard" "node_exporter" {
  config_json = file("dashboards/Node Exporter Full.json")
  folder = grafana_folder.tf.id
  overwrite = true
}

# Alerting
resource "grafana_rule_group" "alert_gorup" {
  name             = "1m-group"
  folder_uid       = grafana_folder.tf.uid
  interval_seconds = 60
  org_id           = 1
  rule {
    annotations = {
      __dashboardUid__ = grafana_dashboard.cadvisor.uid
      __panelId__      = "9"
      description      = ""
      runbook_url      = ""
      summary          = ""
    }
    condition      = "C"
    exec_err_state = "Error"
    for            = "3m0s"
    is_paused      = false
    labels = {
      "" = ""
    }
    name          = "Memory Usage"
    no_data_state = "NoData"
    data {
      datasource_uid = "prometheus"
      model = jsonencode({
        datasource = {
          type = "prometheus"
          uid  = "prometheus"
        }
        expr         = "sum(container_memory_rss{instance=~\".*\",name=~\".*\",name=~\".+\"}) by (name)"
        interval     = ""
        intervalMs   = 15000
        legendFormat = "{{name}}"
        refId        = "A"
      })
      ref_id = "A"
      relative_time_range {
        from = 21600
        to   = 0
      }
    }
    data {
      datasource_uid = "__expr__"
      model = jsonencode({
        conditions = [{
          evaluator = {
            params = []
            type   = "gt"
          }
          operator = {
            type = "and"
          }
          query = {
            params = ["B"]
          }
          reducer = {
            params = []
            type   = "last"
          }
          type = "query"
        }]
        datasource = {
          type = "__expr__"
          uid  = "__expr__"
        }
        expression = "A"
        reducer    = "last"
        refId      = "B"
        type       = "reduce"
      })
      ref_id = "B"
      relative_time_range {
        from = 0
        to   = 0
      }
    }
    data {
      datasource_uid = "__expr__"
      model = jsonencode({
        conditions = [{
          evaluator = {
            params = [50000000]
            type   = "gt"
          }
          operator = {
            type = "and"
          }
          query = {
            params = ["C"]
          }
          reducer = {
            params = []
            type   = "last"
          }
          type = "query"
        }]
        datasource = {
          type = "__expr__"
          uid  = "__expr__"
        }
        expression = "B"
        refId      = "C"
        type       = "threshold"
      })
      ref_id = "C"
      relative_time_range {
        from = 0
        to   = 0
      }
    }
    notification_settings {
      contact_point = "grafana-default-email"
    }
  }
}
