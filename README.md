# Stein index

```pycon
>>> from index import add_to_index
>>> add_to_index('Gott', 'ESGA 5', '11')
>>> add_to_index('Gott', 'PE', '11', 'r') # Not exact term, but related discussion
>>> add_to_index('Husserl, Edmund' , 'ESGA', 'vi', 'p') # Referencing personal names
```

## References

The references to Stein's works are gathered in `references.yml` in CSL YAML format. Using a citeproc processor these can be converted to a styled bibliography:

```shell
$ python refs.py
```

Output is stored in `references.html`
