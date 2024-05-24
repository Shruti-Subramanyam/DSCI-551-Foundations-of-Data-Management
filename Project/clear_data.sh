farmers=$(curl -s -X 'GET' 'http://localhost/farmer/' -H 'accept: application/json')

echo "$farmers" | jq -r '.[] | ._id' | while read -r id; do
  curl -X 'DELETE' "http://localhost/farmer/${id}" -H 'accept: application/json'
done
