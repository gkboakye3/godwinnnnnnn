 
#kofi.kwame+dafa@gmail.com
#kofi.kwame@anyemail.com -> kofikwame@anyemail.com
#kofi.kwame+dafa@anyemail.com -> kofikwame@anyemail.com
#kofi.k.w.a.m.e+something@anyemail.com -> kofikwame@anyemail.com
#kofi.k.w.a.m.e@anyemail.com -> kofikwame@anyemail.com


y_email= input('Enter the email:')

def mail():
    if '+' in y_email:
        go=y_email.split('+')
        kk=go[0]
        ll=go[1]
        yy=kk.replace('.', '')
        pp=ll.index('@')
        jj=ll[:pp]
        oo = ll.replace(jj, '')
        email = yy + oo
        return email
    
    else:
        uu=y_email.split('@')
        hh=uu[0]
        rr=uu[1]
        ee=hh.replace('.', '')
        vv= '@' + rr
        qq= ee + vv
        return qq

print(mail())