set nocompatible

call plug#begin('~/.vim/plugged')
Plug 'vim-syntastic/syntastic'
Plug 'nathanaelkane/vim-indent-guides'
"Plug 'noahfrederick/vim-hemisu'
Plug 'sickill/vim-monokai'

call plug#end()

syntax enable
colorscheme monokai
set relativenumber
set cursorline
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
" Auto resize windows
autocmd VimResized * wincmd =

nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l
set wildmode=list:longest,full
set completeopt=menu,longest,preview
set showcmd
