import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
  var server_list = ["app:8000"];
//   var server_list = ["localhost:8000"];
  var endpoint_list = ["/"]
  server_list.forEach(function(server) {
    endpoint_list.forEach(function(endpoint) {
      http.get("http://" + server + endpoint);
    });
  });
  sleep(2);
}
