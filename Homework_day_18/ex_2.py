"""Есть список логов:
logs = [
"INFO: User logged in",
"ERROR: Database unavailable",
"INFO: User opened profile",
"WARNING: Slow response",
"ERROR: Connection lost",
]
Напишите генератор error_logs(), который возвращает только
сообщения с уровнем ERROR. Использование:
for log in error_logs(logs):
print(log)
Ожидается:
ERROR: Database unavailable
ERROR: Connection lost"""

logs = [
"INFO: User logged in",
"ERROR: Database unavailable",
"INFO: User opened profile",
"WARNING: Slow response",
"ERROR: Connection lost",]

def error_logs(logs):
 for log in logs:
    log.startswith("ERROR")
        yield log

for log in error_logs(logs):
 print(log)

