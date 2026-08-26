# IPv4 Validator

Validates whether a string is a properly formatted IPv4 address (no octet above 255, no leading zeros) using regular expressions.

## Usage

```
$ python numb3rs.py
IPv4 Address: 172.16.254.1
True

$ python numb3rs.py
IPv4 Address: 1.2.3.400
False
```

## Run the tests

```
pytest
```
