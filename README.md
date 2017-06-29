# Validex

A (very) simple field validation library for semi-common problems that will
raise an exception if a field does not match a specific pattern.

*Note:* this is NOT a fully-functional form validation library, like
[marshmallow](https://github.com/marshmallow-code/marshmallow). Instead, it is
a collection of simple field validators that you could use to validate specific
field data within one of those frameworks.

Each validation package includes a functional validator, which returns the
original data if it is valid, or `None` if it is not. Each validation package
also provides a custom validator class, which can be configured to raise a
`ValidationError` under specific circumstances.

## Validating Passwords

**Functional validation:**

```python
>>> from validex.passwords import validate_password
>>> validate_password('invalid password')
None
>>> validate_password('V4lidPa$$word')
'V4lidPa$$word'
```

**Object-based validation:**

```python
>>> from validex.passwords import PasswordValidator
>>> validator = PasswordValidator(minimum=12, deny_symbols('$/_-'))
>>> validator('V4lidPassw#rd')
'V4lidPassw#rd'
>>> validator('Inv4lid_Pa$$word')
# Raises exception
```