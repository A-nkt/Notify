from notification import Notification
import scrape as srp


file = srp.about_coconala(read_csv="init.csv")

if len(file) == 0:
    Notification.line_notify(text="None.")

for i in range(len(file)):
    text = '\n' + "新規案件をお知らせします！" + '\n' + '案件：' + file.loc[i, '案件名'] + '\n' + '価格：' + file.loc[i, '価格'] + '\n' + file.loc[i, 'Link'] + '\n'
    Notification.line_notify(text=text)
