def filter(cond): map(select(cond));

filter(.value|tonumber > .8)