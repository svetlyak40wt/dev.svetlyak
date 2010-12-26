Title: Vim plugin to post to blogspot
Slug: how-to-write-vim-plugins-in-python
Date: 2008-09-09 01:29
Tags: vim,python
Category: texts
Lang: en
Description: 

I am looking for handy tool to write small posts in this blogspot blog now. I have tried Drivel and BloGTK under Ubuntu linux. But Drivel can't add tags to my posts, and BloGTK does not work at all. So, I start to search a plugin for my favorite text editor vim.

And I found it on the «[The Geek Wannabe][1]» blog. This small plugin allows you to write new post and edit existing posts on the blogspot.com. But it does not work with the Unicode. Now I am patching this plugin to fix all unicode issues and I'll be glad to present these patches to the original plugin's author.

While, this patch is looks like this:

    :::diff
    --- ftplugin/blogger/blogger.vim 2006-12-20 21:59:31.000000000 +0300
    +++ /home/art/.vim/ftplugin/blogger/blogger.vim 2008-09-09 12:32:29.000000000 +0400
    @@ -1,3 +1,4 @@
    +" By http://djcraven5.blogspot.com/2006/12/vim-bloggerbeta-plugin-release.html
     " Vim-BloggerBeta Preamble"{{{
     " Make sure the Vim was compiled with +python before loading the script...
     if !has("python")
    @@ -185,7 +186,7 @@
         else:
             response, content = h.request(uri, "GET")
         if response['status'] == '200':
    -         postsFromXML(content)
    +        postsFromXML(content)
         else:
             print "Error getting post feed."
     
    @@ -203,9 +204,9 @@
             num = 5
         for i in range(num):
             if BLOGGER_POSTS[i]['draft']:
    -            print str(i+1) + ':', BLOGGER_POSTS[i]['title'] + '        **DRAFT**'
    +            print '%d: %s **DRAFT**' % (i+1, BLOGGER_POSTS[i]['title'])
             else:
    -            print str(i+1) + ':', BLOGGER_POSTS[i]['title']
    +            print '%d: %s' % (i+1, BLOGGER_POSTS[i]['title'])
         vim.command('let choice = input("Enter number or ENTER: ")')
         pychoice = vim.eval('choice')
         if pychoice.isdigit():
    @@ -498,7 +499,7 @@
             for node in entryNode.getElementsByTagName('link'):
                 post[node.getAttribute('rel')+"_url"] = node.getAttribute('href')
             titleNode = entryNode.getElementsByTagName('title')[0]
    -        post['title'] = _getTextDataFromNode(titleNode)
    +        post['title'] = _getTextDataFromNode(titleNode).encode('utf-8')
             contentNode = entryNode.getElementsByTagName('content')[0]
             post['content'] = _getTextDataFromNode(contentNode)
             idNode = entryNode.getElementsByTagName('id')[0]
    

   [1]: http://djcraven5.blogspot.com/2006/12/vim-bloggerbeta-plugin-release.html