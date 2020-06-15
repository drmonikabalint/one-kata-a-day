def domain_name(url):
    #for i in url:
      spltAr = url.split("://");
      i = (0,1)[len(spltAr)>1];
      dm = spltAr[i].split("?")[0].split('/')[0].split(':')[0].split('.')[0].lower();
      if dm[0:3] =='www':
          return spltAr[i].split("?")[0].split('/')[0].split(':')[0].split('.')[1].lower();
      else:
          return dm
