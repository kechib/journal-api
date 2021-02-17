#!/bin/bash

curl "http://localhost:8000/journals/${ID}/" \
  --include \
  --request PATCH \
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
