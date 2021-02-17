#!/bin/bash

curl "http://localhost:8000/journals/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
