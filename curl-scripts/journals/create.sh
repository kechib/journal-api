#!/bin/bash

curl "http://localhost:8000/journals/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "journal": {
      "title": "'"${TITLE}"'",
      "content": "'"${CONTENT}"'",
      "feeling": "'"${FEELING}"'"

    }
  }'

echo
