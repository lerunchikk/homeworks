def analyze_logins(logs):
     result = {}
     for username,success in logs:
         if username not in result:
             result[username] = {"success":0, "failed": 0}

         if success:
             result[username]["success"]+=1
         else:
            result[username]["failed"]+=1
     return result

logs = [
     ("alice", True),
     ("bob", False),
     ("alice", True),
     ("alice", False),
     ("bob", True),
     ("charlie", False),
     ]
result = analyze_logins(logs)
print(result)