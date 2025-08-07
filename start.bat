@echo off

echo * Django projesi başlatılıyor...
docker-compose up -d

echo * Container'lar hazırlanıyor...
timeout /t 3 /nobreak >nul

echo ✅ Proje hazır! http://localhost:80
echo 📊 Admin: http://localhost:80/admin
pause
