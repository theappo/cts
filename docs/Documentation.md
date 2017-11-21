#Documentation

---

## GateWay.py

- **GateWay()**
1. constructor

- **check_blacklist(user_id)**
1. user_id is a `string`
2. return `True` if user_id in the blacklist table, otherwise return `False`

- **verify_user(user_id, password)**
1. user_id and password are `string`
2. return `True` if (user_id, password) is in the user table, otherwise return `False`
