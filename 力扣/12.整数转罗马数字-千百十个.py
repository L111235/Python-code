def iTR(num):
    #dr={0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
    dr={0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}

    q=num//1000#千位
    b=(num-1000*q)//100#百位
    s=(num-1000*q-100*b)//10#十位
    g=num-1000*q-100*b-10*s#个位
        
    #qr=q*dr[1000]#罗马千位
    qr=q*'M'
        
    if b==9:#罗马百位
        #br=dr[900]
        br='CM'
    elif 4<b<9:
        #br=dr[500]+(b-5)*dr[100]
        br='D'+(b-5)*'C'
    elif b==4:
        #br=dr[400]
        br='CD'
    elif b<4:
        #br=b*dr[100]
        br=b*'C'
            
    if s==9:#罗马十位
        #sr=dr[90]
        sr='XC'
    elif 4<s<9:
        #sr=dr[50]+(s-5)*dr[10]
        sr='L'+(s-5)*'X'
    elif s==4:
        #sr=dr[40]
        sr='XL'
    elif s<4:
        #sr=s*dr[10]
        sr=s*'X'
        
    gr=dr[g]#罗马个位
        
    res=qr+br+sr+gr
        
    return res

num=1994
print(iTR(num))