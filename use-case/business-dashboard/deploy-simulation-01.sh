echo "Simulating service deployment..."

now=$(date +%s)

# 建立 Grafana 部署註解
curl -X POST http://localhost:8080/grafana/api/annotations \
-u admin:admin \
-H "Content-Type: application/json" \
-d "{
    \"dashboardUID\":\"business-dashboard\",
    \"time\": ${now}000,
    \"timeEnd\": ${now}000,
    \"tags\":[\"deployment\"],
    \"text\":\"First deployment\"
}"

echo ""

# 設定 paymentFailure 為 75%
curl -X POST http://localhost:8080/feature/api/write-to-file \
-H "Content-Type: application/json" \
-d '{
    "data": {
        "$schema": "https://flagd.dev/schema/v0/flags.json",
        "flags": {
            "productCatalogFailure": {
                "description": "Fail product catalog service on a specific product",
                "state": "ENABLED",
                "variants": {"on": true, "off": false},
                "defaultVariant": "off"
            },
            "recommendationCacheFailure": {
                "description": "Fail recommendation service cache",
                "state": "ENABLED",
                "variants": {"on": true, "off": false},
                "defaultVariant": "on"
            },
            "adManualGc": {
                "description": "Triggers full manual garbage collections in the ad service",
                "state": "ENABLED",
                "variants": {"on": true, "off": false},
                "defaultVariant": "off"
            },
            "adHighCpu": {
                "description": "Triggers high cpu load in the ad service",
                "state": "ENABLED",
                "variants": {"on": true, "off": false},
                "defaultVariant": "off"
            },
            "adFailure": {
                "description": "Fail ad service",
                "state": "ENABLED",
                "variants": {"on": true, "off": false},
                "defaultVariant": "off"
            },
            "kafkaQueueProblems": {
                "description": "Overloads Kafka 佇列 while simultaneously introducing a consumer side delay leading to a lag spike",
                "state": "ENABLED",
                "variants": {"on": 100, "off": 0},
                "defaultVariant": "off"
            },
            "cartFailure": {
                "description": "Fail cart service",
                "state": "ENABLED",
                "variants": {"on": true, "off": false},
                "defaultVariant": "off"
            },
            "paymentFailure": {
                "description": "Fail payment service charge requests n%",
                "state": "ENABLED",
                "variants": {
                    "100%": 1,
                    "90%": 0.95,
                    "75%": 0.75,
                    "50%": 0.5,
                    "25%": 0.25,
                    "10%": 0.1,
                    "off": 0
                },
                "defaultVariant": "75%"
            },
            "paymentUnreachable": {
                "description": "Payment service is unavailable",
                "state": "ENABLED",
                "variants": {"on": true, "off": false},
                "defaultVariant": "off"
            },
            "loadGeneratorFloodHomepage": {
                "description": "Flood the frontend with a large amount of requests.",
                "state": "ENABLED",
                "variants": {"on": 100, "off": 0},
                "defaultVariant": "on"
            },
            "imageSlowLoad": {
                "description": "slow loading images in the frontend",
                "state": "ENABLED",
                "variants": {"10sec": 10000, "5sec": 5000, "off": 0},
                "defaultVariant": "off"
            }
        }
    }
}'

echo ""

echo "Deployment simulation completed."
