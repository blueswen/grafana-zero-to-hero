terraform {
  required_providers {
    grafana = {
      source  = "grafana/grafana"
      version = "3.9.0"
    }
  }
}

provider "grafana" {
  url  = "http://localhost:3000"
  auth = "admin:admin"
}

resource "grafana_data_source" "prometheus" {
  name = "prometheus"
  type = "prometheus"
  url = "http://prometheus:9090"
}

resource "grafana_folder" "my_folder" {
  title = "My Folder"
  uid   = "my-folder-uid"
}

resource "grafana_dashboard" "my_dashboard" {
  folder = grafana_folder.my_folder.uid
  config_json = jsonencode({
    "title" : "My Dashboard",
    "uid" : "my-dashboard-uid"
  })
}
