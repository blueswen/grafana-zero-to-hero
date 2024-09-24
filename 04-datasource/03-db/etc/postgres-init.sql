CREATE TABLE services (
    service_id SERIAL PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    service_status VARCHAR(20) NOT NULL,
    ip_address VARCHAR(45) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 插入一些範例資料
INSERT INTO services (service_name, service_status, ip_address) 
VALUES 
('auth-service', 'running', '192.168.1.10'),
('payment-service', 'stopped', '192.168.1.11'),
('order-service', 'running', '192.168.1.12');

CREATE TABLE service_metrics (
    metric_id SERIAL PRIMARY KEY,
    service_id INT REFERENCES services(service_id),
    cpu_usage DECIMAL(5, 2), -- CPU 使用率
    memory_usage DECIMAL(5, 2), -- 記憶體使用率（以百分比表示）
    timestamp TIMESTAMP NOT NULL
);

-- 插入一些範例數據，模擬每分鐘的監控數據
INSERT INTO service_metrics (service_id, cpu_usage, memory_usage, timestamp)
VALUES 
(1, 75.3, 60.5, '2024-09-21 10:00:00'),
(1, 78.1, 62.1, '2024-09-21 10:01:00'),
(1, 80.0, 65.4, '2024-09-21 10:02:00'),
(2, 40.0, 35.7, '2024-09-21 10:00:00'),
(2, 42.5, 38.2, '2024-09-21 10:01:00'),
(3, 55.6, 50.3, '2024-09-21 10:00:00'),
(3, 58.3, 52.1, '2024-09-21 10:01:00');
