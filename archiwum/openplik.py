import subprocess

file_path = "ścieżka/do/twojego/pliku"

try:
    process = subprocess.Popen(['cmd', '/c', 'start', '', file_path], shell=True)
    exit_code = process.wait() 
    if exit_code != 0:
        raise Exception("Proces zakończył się błędem.")
    print("----------------")
except Exception as e:
    print("Nie udało się uruchomić procesu:", e)
else:
    print("Plik został otwarty pomyślnie.")
    # Dodatkowy kod do wykonania, jeśli proces został uruchomiony poprawnie
