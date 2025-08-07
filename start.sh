#!/bin/bash
set -e

echo "* Django projesi başlatılıyor..."
docker-compose up -d

echo "* Container'lar hazırlanıyor..."
sleep 3

echo "✅ Proje hazır! http://localhost:80"
echo "📊 Admin panel: http://localhost:80/admin"
