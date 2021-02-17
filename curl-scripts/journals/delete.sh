#!/bin/bash

curl "http://localhost:8000/journals/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
