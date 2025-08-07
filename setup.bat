@echo off

echo * Django projesi başlatılıyor...
docker-compose up --build -d

echo "* Container'ların hazır olması bekleniyor..."

set /a attempts=0
set /a max_attempts=120

:migration
if %attempts% geq %max_attempts% (
    echo * Başarısız!
    exit /b 1
)

docker-compose exec web python manage.py migrate >nul 2>&1
if %errorlevel% equ 0 (
    echo * Database migration başarılı!
    goto migration_done
)

timeout /t 5 /nobreak >nul
set /a attempts+=1
goto migration

:migration_done
echo * Statik dosyalar toplanıyor...
docker-compose exec web python manage.py collectstatic --noinput

echo.
set /p response=? Django projeniz için superuser oluşturmak ister misiniz? (y/n): 
if /i "%response%"=="y" (
    docker-compose exec web python manage.py createsuperuser
)
if /i "%response%"=="yes" (
    docker-compose exec web python manage.py createsuperuser
)


echo.
echo [] Proje hazır! http://localhost:80 adresinden erişebilirsiniz
echo [] Admin panel: http://localhost:80/admin
pause
