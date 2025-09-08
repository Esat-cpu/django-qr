@echo off

echo * Django projesi baslatiliyor...
docker-compose up --build -d || exit /b 1

echo "* Container'larin hazir olmasi bekleniyor..."

set /a attempts=0
set /a max_attempts=120

:migration
if %attempts% geq %max_attempts% (
    echo * Basarisiz!
    exit /b 1
)

docker-compose exec web python manage.py migrate >nul 2>&1
if %errorlevel% equ 0 (
    echo * Database migration basarili!
    goto migration_done
)

timeout /t 5 /nobreak >nul
set /a attempts+=1
goto migration

:migration_done
echo * Statik dosyalar toplaniyor...
docker-compose exec web python manage.py collectstatic --noinput

echo.
set /p response=? Django projeniz icin superuser olusturmak ister misiniz? (y/n): 
if /i "%response%"=="y" (
    docker-compose exec web python manage.py createsuperuser
)
if /i "%response%"=="yes" (
    docker-compose exec web python manage.py createsuperuser
)


echo.
echo * Proje hazir! http://localhost:80 adresinden erisebilirsiniz
echo * Admin panel: http://localhost:80/admin
pause
