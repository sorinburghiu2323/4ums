## Backend guide

Make your migrations whenever necessary with:

```
python manage.py makemigrations
```

### Standards
- Upon endpoint creation, document it in the .yaml file.
- Use proper python coding conventions and document your code. (e.g: each method should have a docstring)
- Create your utility modules to be used throughout the code in /Utils.
- Create your endpoint controllers in /Controllers.