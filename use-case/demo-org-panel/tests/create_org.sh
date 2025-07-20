# Create multiple organizations using a shell script
orgList=(
  "Alpha Org."
  "Beta Org."
  "Gamma Org."
  "Delta Org."
  "Epsilon Org."
  "Zeta Org."
  "Eta Org."
  "Theta Org."
  "Iota Org."
)

for org in "${orgList[@]}"; do
  curl -X POST -H "Content-Type: application/json" \
       -d "{\"name\": \"$org\"}" \
       http://admin:admin@localhost:3000/api/orgs
done
