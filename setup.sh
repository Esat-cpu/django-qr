#!/bin/bash

set -e

echo "* Django projesi başlatılıyor..."
docker-compose up --build -d


echo "* Container'ların hazır olması bekleniyor..."

attempts=0
max_attempts=60

while [ $attempts -lt $max_attempts ]; do
    if docker-compose exec web python manage.py migrate 2> /dev/null; then
        echo "* Database migration başarılı!"
        break
    else
        sleep 5
        ((attempts++))
    fi
done

if [ $attempts -eq $max_attempts ]; then
    echo "* Başarısız!"
    exit 1
fi


echo "* Statik dosyalar toplanıyor..."
docker-compose exec web python manage.py collectstatic --noinput


echo "✅ Proje hazır! http://localhost:80 adresinden erişebilirsiniz"
echo "📊 Admin panel: http://localhost:80/admin"
