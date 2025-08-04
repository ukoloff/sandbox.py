# SIP 40000

Миграция телефонных номеров
с 4-значных
на 5-значные (Синара)

1. Замена extension на всех SIP-телефонах [main.py](main.py)
2. Загрузка новых extension и DID на PBX (Bulk Handler) [upgrade.py](upgrade.py)
3. Замена `otherTelephone` (и возможно `telephoneNumber`) в Active Directory
