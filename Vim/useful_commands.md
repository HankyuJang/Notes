# Commands for editing a file


### comment or uncomment area

`V + ',' + 'c' + [space]`

### open several files

`:e [tab]`

### switch from several files 

`:b1` - Change to the file that opened at first
`:b2` - Change to the file that opened at first

### copy paste

`y$` - yank to the end of the line
`yiw` - yank the current word (remove whitespace)
`yaw` - yank the current word (include whitespace)

### Repeat the last procedure from 'insert'

`.`

### Replace words

Changing set -> get for global(g) `set` and confirm(c) one by one

`:%s/set/get/gc`

Changing set -> get for a specific area

`V` then, `:s/set/get/gc`

### Mark

register using ", then go to the mark using '

### movement in the line

move by `_`

`f _`
