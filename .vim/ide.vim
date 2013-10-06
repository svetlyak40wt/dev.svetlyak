silent! so ~/.vim/ide/python.vim

function! Resize()
python << EOF
import urllib
import vim
vim.command('normal 0f:wv$h"uy')
encoded = urllib.urlencode(dict(image = vim.eval('@u'), w='600'))
vim.command('normal o[Resized]: http://resizer.co/?' + encoded)
EOF
endfunction

map mm :!make<CR>
map mp :!make production<CR>
nmap ,i :call Resize()<CR>

