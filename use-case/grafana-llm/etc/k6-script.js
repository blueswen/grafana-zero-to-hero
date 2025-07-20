import http from 'k6/http';
import { randomSeed, sleep } from 'k6';

export function setup() {
  var server = "localhost:8000";
  var mode = __ENV.MODE || "default";
  if (mode === "compose") {
    server = "app-a:8000";
  }
  // a todo list for learning Observability
  var todo_list = [
    {
      "title": "Set up Prometheus",
      "description": "Install Prometheus and configure it to scrape metrics from a basic application or exporter.",
      "completed": false
    },
    {
      "title": "Visualize metrics in Grafana",
      "description": "Connect Prometheus to Grafana and build a simple dashboard to display CPU and memory usage.",
      "completed": false
    },
    {
      "title": "Enable structured logging",
      "description": "Configure the application to emit logs in JSON format and include fields like timestamp, level, and service name.",
      "completed": false
    },
    {
      "title": "Set up Loki for log collection",
      "description": "Deploy Loki and use Loki Docker Driver to collect and send logs from your application or container.",
      "completed": false
    },
    {
      "title": "Integrate OpenTelemetry tracing",
      "description": "Instrument a basic HTTP API using OpenTelemetry SDK to generate traces and spans.",
      "completed": false
    },
    {
      "title": "Export traces to Grafana Tempo",
      "description": "Send tracing data from OpenTelemetry Collector to Tempo and view the traces in Grafana.",
      "completed": false
    },
    {
      "title": "Create an alert rule in Grafana",
      "description": "Define an alert based on metric thresholds (e.g., memory > 80%) and configure a webhook notification.",
      "completed": false
    }
  ]
  var current_todo_list = http.get(`http://${server}/todos`);
  todo_list.forEach(function(todo) {
    if (current_todo_list.body.includes(todo.title)) {
      return;
    }
    http.post(`http://${server}/todos`, JSON.stringify(todo), {
      headers: {
        "Content-Type": "application/json",
      },
    });
  }); 
}

export default function () {
  var server_list = ["localhost:8000", "localhost:8001", "localhost:8002"];
  var mode = __ENV.MODE || "default";
  if (mode === "compose") {
    server_list = ["app-a:8000", "app-b:8000", "app-c:8000"];
  }
  var endpoint_list = ["/", "/io_task", "/cpu_task", "/random_status", "/random_sleep", "/chain"]
  // randomly pick 3 endpoints from the list
  endpoint_list = endpoint_list.sort(() => 0.5 - Math.random()).slice(0, 3);  
  server_list.forEach(function(server) {
    endpoint_list.forEach(function(endpoint) {
      http.get("http://" + server + endpoint);
    });
  });

  var todo_server = "localhost:8000";
  if (mode === "compose") {
    todo_server = "app-a:8000";
  }
  var tasks = ["query_all_todos", "query_all_todos", "query_all_todos", "query_todo", "update_todo"];
  tasks.forEach(function(task) {
    switch (task) {
      case "query_all_todos":
        http.get(`http://${todo_server}/todos/`);
        break;
      case "query_todo":
        http.get(`http://${todo_server}/todos/${Math.floor(Math.random()*10+1)}`);
        break;
      case "update_todo":
        http.put(`http://${todo_server}/todos/${Math.floor(Math.random()*5+1)}`, JSON.stringify({
          "completed": Math.random() >= 0.5
        }), {
          headers: {
            "Content-Type": "application/json",
          },
        });
        break;
    }
  });
  sleep(0.5);
}
