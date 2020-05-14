import wikipedia

wikipedia.set_lang('ja')
page = wikipedia.page('XXXXXXXXXXXXXXXXXXXXXXXXX')
print(page.title)
print(page.summary)
