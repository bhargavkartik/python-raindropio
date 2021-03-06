import os
from raindropio import *

api = API(os.environ["RAINDROP_TOKEN"])

c = User.get(api)

print("id:", c.id)
print("config:", c.config)
print("email:", c.email)
print("email_MD5:", c.email_MD5)
print("files:", c.files)
print("fullName:", c.fullName)
print("groups:", c.groups)
print("password:", c.password)
print("pro:", c.pro)
print("registered:", c.registered)

print("broken_level:", c.config.broken_level)
print("font_color :", c.config.font_color)
print("font_size:", c.config.font_size)
print("last_collection:", c.config.last_collection)
print("raindrops_view:", c.config.raindrops_view)

print("title:", c.groups[0].title)
print("hidden:", c.groups[0].hidden)
print("sort:", c.groups[0].sort)
print("collections:", c.groups[0].collectionids)
