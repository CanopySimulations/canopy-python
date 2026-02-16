#!/usr/bin/env bash
set -euo pipefail

url="${1:-https://api.canopysimulations.com}"
url="$url/swagger/v1/swagger.json"

echo "Generated URL:"
echo "  $url"
echo
read -p "Proceed? (y/n): " answer
if [ "$answer" != "y" ]; then
echo "Cancelled."
exit 1
fi
echo "Continuing..."

java -jar openapi-generator-cli.jar generate -g python-legacy -i "$url" -o ./gen --package-name "canopy.openapi"
rm -rf repo/canopy/openapi
rm -rf repo/docs
cp -r gen/canopy/openapi repo/canopy
cp -r gen/docs repo
cp -r gen/README.md repo/OPENAPI_README.md

rm -rf gen
java -jar openapi-generator-cli.jar generate -g python-legacy -i "$url" -o ./gen --package-name "canopy.openapi" --library asyncio
mv gen/canopy/openapi gen/canopy/openapi_asyncio
rm -rf gen/canopy/openapi_asyncio/api
rm -rf gen/canopy/openapi_asyncio/models
rm -f gen/canopy/openapi_asyncio/configuration.py
rm -f gen/canopy/openapi_asyncio/exceptions.py
sed -i 's/from canopy\.openapi import rest/from canopy.openapi_asyncio import rest/g' gen/canopy/openapi_asyncio/api_client.py
sed -i '/from canopy.*/d' gen/canopy/openapi_asyncio/__init__.py
sed -i '/# import /d' gen/canopy/openapi_asyncio/__init__.py
echo 'from canopy.openapi_asyncio.api_client import ApiClient' >> gen/canopy/openapi_asyncio/__init__.py
cp -r gen/canopy/openapi_asyncio repo/canopy
