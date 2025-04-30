from libretranslatepy import LibreTranslateAPI

a='For this God is our God for ever and ever: he will be our guide even unto death. (Psalms 48:14)'

lt = LibreTranslateAPI("https://libretranslate.com/")

print(lt.translate(a, "en", "uk"))
# LibreTranslate es impresionante!

print(lt.detect(a))
# [{"confidence": 0.6, "language": "en"}]

print(lt.languages())
# [{"code":"en", "name":"English"}, {"code":"es", "name":"Spanish"}]