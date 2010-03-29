def age(t):
    if (t < 50): return u'seconds ago'
    if (t < 100): return u'a minute ago'
    if (t < 300): return u'minutes ago'
    if (t < 3300): return u'%d minutes ago' % int(t / 60)
    if (t < 7200): return u'an hour ago'
    if (t < 82800): return u'%d hours ago' % int(t / 3600)
    if (t < 172800): return u'a day ago'
    return u'%d days ago' % int(t / 86400)
