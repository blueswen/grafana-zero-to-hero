import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
  var server_list = ["localhost:8000"];
  var mode = __ENV.MODE || "default";
  if (mode === "compose") {
    server_list = ["app-a:8000", "app-b:8000", "app-c:8000"];
  }
  var endpoint_list = ["/", "/io_task", "/cpu_task", "/random_status", "/random_sleep", "/chain"]
  server_list.forEach(function(server) {
    endpoint_list.forEach(function(endpoint) {
      http.get("http://" + server + endpoint);
    });
  });
  sleep(0.5);
}
