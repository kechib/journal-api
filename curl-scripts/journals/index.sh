#!/bin/bash

curl "http://localhost:8000/journals/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
