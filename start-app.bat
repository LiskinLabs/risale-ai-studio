@echo off
cd /d "%~dp0apps\readest-app"
npx dotenv -e .env.web -- npx next dev -p 3000
