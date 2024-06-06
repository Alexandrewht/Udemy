'''
 locale para internacionalização
 https://docs.python.org/3/library/locale.html
 https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
'''
import calendar
import locale

locale.setlocale(locale.LC_ALL, '')  # usando locale padrão do computador

print(calendar.calendar(2024))

#  no powershell, para buscar o idioma do computador:
#  Get-WinSystemLocale
#  no windows é
print(locale.getlocale())