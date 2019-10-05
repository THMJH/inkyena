from Wes import Wes

latins = "i e a o u p b t d ky gy k g f s sh shr ts ch chr hy h m n ng l w y"
latinl = latins.split(" ")

weslis = [Wes(y, x) for x, y in enumerate(latinl)]
weslisGreedy = sorted(weslis, key=lambda x: -len(x.latinrep))
