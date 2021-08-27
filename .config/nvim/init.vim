noh
syntax on
set showcmd
set termguicolors
set number
set cursorline
set expandtab
set noshiftround
set lazyredraw
set magic
set hlsearch
set incsearch
set ignorecase
set smartcase
set encoding=utf-8
set modelines=0
set formatoptions=tqn1
set tabstop=4
set shiftwidth=4
set softtabstop=4
set cmdheight=1
set laststatus=2
set backspace=indent,eol,start
set matchpairs+=<:>
set noshowmode
set scrolloff=8
set list
set listchars=tab:\│\ 
hi tabgroup ctermbg=NONE ctermfg=0 cterm=NONE
match tabgroup /\t/

nmap <C-S> :w<CR>
nmap <C-_> :noh<CR>
nmap <S-Left> v<Left>
nmap <S-Right> v<Right>
nmap <C-Up> 8k
nmap <C-Down> 8j
nmap <C-O> o<Esc>
nmap <C-Z> u
nmap <C-Y> <C-R>
nmap <C-F> /
nmap <C-H> i<C-W><Esc>
nmap <C-T> :tabnew 
nmap <A-Right> :tabnext<CR>
nmap <A-Left> :tabprevious<CR>
nmap <F3> :set invnumber<CR>
nmap <F4> :q<CR>
nmap <F5> :%s/    /\t/g<CR>
nmap <F6> :%s/  / /g<CR>
imap <C-S> <Esc>:w<CR>
imap <C-_> <Esc>:noh<CR>a
imap <S-Left> <Esc>lv<Left>
imap <S-Right> <Esc>lv<Right>
imap <C-Up> <Esc>8ka
imap <C-Down> <Esc>8ja
imap <C-O> <Esc>o
imap <C-Z> <Esc>ua
imap <C-Y> <Esc><C-R>a
imap <C-F> <Esc>/
imap <C-H> <C-W>
imap <C-V> <Esc>pa
imap <C-T> <Esc>:tabnew 
imap <A-Right> <Esc>:tabnext<CR>a
imap <A-Left> <Esc>:tabprevious<CR>a
imap <F3> <Esc>:set invnumber<CR>a
imap <F4> <Esc>:q<CR>
imap <F5> <Esc>:%s//\t/g<CR>a
imap <F6> :%s/  / /g<CR>a
vmap <C-Up> 8k
vmap <C-Down> 8j
inoremap <C-Space> <C-N>
inoremap <C-@> <C-Space>
command NoPaste :set nopaste
command ShredComment :g/^\(#\|$\)/d
command RealTab :%s/    /\t/g
command SpellEnglish :set spell spelllang=en_us
command SpellIndonesian :set spell spelllang=id
command SpellOff :set nospell
command ReduceSpace :%s/  / /g

colorscheme onedark
lua require'colorizer'.setup()
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list=1
let g:syntastic_auto_loc_list=1
let g:syntastic_check_on_open=1
let g:syntastic_check_on_wq=0
let g:syntastic_loc_list_height=4
let g:airline_theme='onedark'
let g:airline#extensions#whitespace#enabled=0
let g:airline_detect_spell=1
let g:airline_detect_spelllang=1
let g:airline_section_c=''
let g:airline_section_x='%f'
let g:airline_section_y='%{&filetype}'
let g:airline_section_z='%{&fileformat}'
let g:mucomplete#enable_auto_at_startup=1
set completeopt+=menuone
set completeopt+=noselect
set shortmess+=c
set belloff+=ctrlg
imap <unique> <F8> <plug>(MUcompleteCycFwd)
imap <unique> <F9> <plug>(MUcompleteCycBwd)
command OneDarkFallback :let g:onedark_termcolors=16
autocmd VimEnter * ColorizerAttachToBuffer
