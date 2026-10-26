@echo off
setlocal
where node >nul 2>nul
if errorlevel 1 (echo Node.js 20+ required. Install Node.js before running RCC. 1>&2 & exit /b 1)
node "%~dp0..\bin\rcc-consortium" %*
exit /b %ERRORLEVEL%
