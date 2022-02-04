# Now the program working only with flags -gg for google maps
# and -ch for Amap maps

import ChinaAmapIt as ch
import googleMapIt as gg
import sys



if sys.argv[1] == '-ch':
    ch.amap_search(sys.argv[2:])
elif sys.argv[1] == '-go':
    gg.google_search(sys.argv[2:])
