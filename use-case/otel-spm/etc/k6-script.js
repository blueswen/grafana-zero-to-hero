import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
  var server_list = ["fastapi:8000", "spring-boot:8080", "express:3001"]
  var endpoint_list = ["/", "/io_task", "/cpu_task", "/random_sleep", "/random_status", "/chain", "/error_test"]
  server_list.forEach(function(server) {
    endpoint_list.forEach(function(endpoint) {
      http.get("http://" + server + endpoint);
    });
  });
  sleep(0.5);
}
