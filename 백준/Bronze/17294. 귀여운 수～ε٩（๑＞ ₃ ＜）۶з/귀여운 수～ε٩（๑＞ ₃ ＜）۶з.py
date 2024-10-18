k = input()
cute = True;
for i in range(1, len(k) - 1):
    if int(k[i]) - int(k[i - 1]) != int(k[i + 1]) - int(k[i]):
        cute = False;
        break;
if cute:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")