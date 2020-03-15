from tkinter import *
import webbrowser
root = Tk()
text = Text(root,width = 30,height = 5)
text.pack()
text.insert(INSERT,'I love Fishc.com')
text.tag_add('link',1.7,1.16)
text.tag_config('link',foreground = 'blue',underline = True)

def show_hand_cursor(event):
    text.config(cursor = 'arrow')
def show_arrow_cursor(event):
   text.config(cursor = 'xterm')
def click(event):
    webbrowser.open('http://www.fishc.com')


text.tag_bind('link','<Enter>',show_hand_cursor)
text.tag_bind('link','<Leave>',show_arrow_cursor)
text.tag_bind('link','<Button-1>',click)

mainloop()
fd=tkinter.filedialog.askopenfilename()
f=open(fd).read()
f=f.lower()
for i in ",.':":
    f=f.replace(i,'')
words=f.split()

stwlist=[]
r=open( 'stopwords.txt',encoding='utf-8').readlines()
for i in r:
    i=i.strip()
    stwlist.append(i)



word_ = {}
for word in words:
    if word.strip() not in stwlist:
        if len(word) > 1:
            if word != '\t':
                if word != '\r\n':
                    #计算词频
                    if word in word_:
                        word_[word] += 1
                    else:
                        word_[word] = 1

#将词汇和词频以元组的形式保存
word_freq = []
for word,freq in word_.items():
    word_freq.append((word,freq))


#进行降序排列
word_freq.sort(key = lambda x:x[1],reverse = True)




