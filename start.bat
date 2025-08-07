@echo off

echo * Django projesi baslatiliyor...
docker-compose up -d

echo * Container'lar hazirlaniyor...
timeout /t 3 /nobreak >nul

echo * Proje hazir! http://localhost:80
echo * Admin: http://localhost:80/admin
pause
