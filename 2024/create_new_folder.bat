
rem Initialize variables
set "last_file="
set "next_day="

rem Loop through files matching "day*" and find the last alphabetically
for /f "delims=" %%f in ('dir /b day* 2^>nul ^| sort') do (
set "last_file=%%f"
)

echo Last file alphabetically: %last_file%

rem Remove "day" prefix and get the numeric part
set "last_suffix=%last_file:day=%"
echo Last suffix: %last_suffix%

rem Remove leading zeros (if any) for arithmetic operations
for /f "tokens=* delims=0" %%i in ("%last_suffix%") do (
    set last_suffix=%%i
)

rem Increment the numeric part by 1
set /a next_suffix=%last_suffix%+1

rem Format next day with leading zeros (if needed)
if %next_suffix% lss 10 (
    set "next_suffix=0%next_suffix%"
)

rem Create the next day filename
set "next_day=day%next_suffix%"
echo Next day alphabetically: %next_day%

mkdir "%next_day%"

xcopy /e /i /h "%last_file%" "%next_day%\"

rem rem Wait for a key press before exiting
rem echo Press any key to exit...
rem pause >nul
