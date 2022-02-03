import ChinaAmapIt as ch
import googleMapIt as gg
import sys
if len(sys.argv) == 1:
    gg.googleSearch()
elif sys.argv[1] == '-ch':
    ch.amap_search(sys.argv[2:])
elif sys.argv[1] == '-go':
    gg.google_search(sys.argv[2:])
else:
    gg.google_search()