# a= "7"
# b= "7"
# print(a+b)


# 1. İki str tipli dəyişəni toplama prosesi 
# necə baş verir ?
# ad = 'rick'
# soyad = ' sanchez'
# print(ad + soyad)
# rick sanchez

# 2. İki int tipli dəyişəni toplama prosesi 
# necə baş verir ?
# a = 3
# b= 4
# print(a+b)

# 3. Bir int və bir str tipli dəyişəni toplama 
# prosesi necə baş verir ?

# 4. Dəyişənin tipini hansı metodla təyin 
# edirik ?
# print(type())

# 5. len() funksiyasını araşdırın...

# 6. print(“salam” * 8) 
# nəticəsi nə olacaq ?
#  8 defe salam yazacaq

# print(5 * 5 * "2")
# # kodun nəticəsi nə olacaq ?
# 2222222222222222222222222

# 8. a dəyərinə kompleks bir ədəd 
# mənimsədin. Və ekrana onun tipini çıxarın 
# (kodu buraya yapışdırarsınız)
# a = 7j-1
# print(type(a))
# <class 'complex'>

# 9. int tipli ədədlə float tipli ədədi 
# toplayarkən alınan ədədin tipi nə olar ?
# float

# 10. Pythonda şərhlər haqqında ümumi 
# məlumat verin.
# Bütün cavabları hər sualın altından qeyd edin.

# len() uzunlugu olcur 
# mylist = ["apple", "banana", "cherry"]
# x = len(mylist)
# print(x)
# 3



# 1. “Azerbaycan” sozunu bir deyisene 
# menimsedin. Onun basdan baslayaraq 
# cut yerde duran herflerini bir biri ile 
# birlesdirib basqa bir deyisene 
# menimsedin. Ve sonra onun 
# uzunlugunu cap edin.
# soz_2 = "Azerbaycan"
# print((soz_2[2::2]))
# soz_3 = soz_2[2::2]
# print(len(soz_3))
# ebya
# 4
# new_word = 'Baku'
# print(new_word[-1::-1])

# soz_3 = 'Hovsan'
# print(soz_3[:5:3])

# 2.print(True==5)  ne qaytaracaq? 
# (kodu yazmadan dusunun bunu, sonra 
# editorda yazaraq yoxlayin)
# print(True==5) --> False

# 3. Multiline str tipli bir deyisen 
# tanimlayin, daha sonra onun 
# elementlerini vergule isaresine gore 
# ayrilmaqla list-e cevirin.
# soz_list ='''There is no one who loves pain itself, 
# who seeks after it and wants to have it, 
# simply because it is pain.'''
# soz_list1= soz_list.split(',')
# print(soz_list1)
# ['There is no one who loves pain itself', ' who seeks after it and wants to have it', ' simply because it is pain.']

# 4. “Respublika” sozunu bir deyisene 
# menimsedin, ve daha sonra yeni bir 
# deyisene indekslemeden istifade 
# ederek, bu sozunun tersinesini 
# yazdirin.
# name = "Respublika"
# name1 = name[-1::-1] 
# print(name1) --> akilbupseR 

# 5. word = ‘’ Baki” 
# print(word * 4)
# Ele edinki ekrana verilen neticede 
# solda bosluq yaranmasin.
# word = "   Baki" 
# print((word * 4).strip())


 
# 6. soz = “Alma”
# print(soz[::])
# ekrana ne cap olunacaq ve sebebini 
# izah edin.
# soz = "Alma"
# print(soz[::]) --> Alma = cunki basdan sona qeder verilib

# 7. Deyisenleri adlandirarken diqqet 
# yetirmeli oldugumuz butun meqamlari 
# qeyd edin.
# evvelde reqm ve simvollar ola bilmez 

# 8. mylist = [‘alma’, ‘armud’, ‘nar’]
# Bu listi str tipe cevirin ve aralarina 
# bosluq atin, alinan sozun birinci herfini 
# ve sonuncu herfini birlesdirin.
# mylist = ["alma", "armud", "nar"]
# soz = " ".join(mylist) 
# print(soz[0]+soz[-1])


# 9. “Azerbaycan” sozunde ‘a’ herfinden
# nece defe istifade olundugunu 
# gosteren python kodu yazin.
# name = "Azerbaycan"
# print(name.count("a")) --> 2

# 10. print(False or True or False or False 
# and True) neticesi ne olacaq ? --> True


# 11. Azerbaycanda yerli firildaqci 
# “sirketler” peyda olub – cumlesini bir 
# deyisene menimsedin ve bu deyiseni 
# bosluga gore list-e cevirin.
# soz1 = "Azerbaycanda yerli firildaqci 'sirketler' peyda olub"
# soz1 = soz1.split(' ')
# print(soz1)
# print(type(soz1))
# ['Azerbaycanda', 'yerli', 'firildaqci', "'sirketler'", 'peyda', 'olub']
# <class 'list'>
# boyuk_eded = int(input("ededi qebul edin:"))
# kicik_eded = int(input("ededi qebul edin:"))
# print(boyuk_eded % kicik_eded)

# kimlik_bilgisi=input("milliyetinizi daxil edin").split()
# print(kimlik_bilgisi)
# reqem = int(input("reqeemi daxil edin")) 
# print(reqem**3%2)
# eded4 = 48
# eded4 = eded4 / 2
# eded4 /= 2
# print(eded4)
# eded5 = 8
# eded5 = eded5 % 3
# eded5 %= 3
# print(eded5)
# eded2 = 45
# eded2 = eded2 // 4 # ededin edede bolunmesinden alinan tam hisseni gosterir
# eded2 //= 4
# print(eded2)



# 1.İstifadeciden 3 eded alın. 1ci ededi 2ciye tam hissesini almaqla bölün. Alınan 
# neticenin 3cü edede bölünmesinden alınan qalığın en birinci ededden neçe defe kiçik 
# olduğunu çap edin.
# num1 = int(input("ededi daxil edin: "))
# num2 = int(input("eddi daxil edin: "))
# num3 = int(input("ededi daxil edin: "))
# num4 = num1 // num2 
# num5 = num4 % (num3)
# print(num1 / num5)


# 2.İstifadeciden bir cumle daxil etmesini teleb edin. Sonra bu cumlenin uzunluğunu bir 
# deyisene menimsedin. 
# Daha sonra bu cumleni list-e cevirin ve listin uzunluğunu tapıb, yeni bir deyisene 
# menimsedin. Cumlenin uzunluğunun list-in uzunluğundan deqiq olaraq neçe defe böyük
# olduğunu çap edin.
# list1 = (input("cumleni daxil edin: "))
# list1_uzunluq = (len(list1))
# yeni_list = list1.split()
# yeni_list_uzunliq = (len(yeni_list))
# print(list1_uzunluq / yeni_list_uzunliq)


# 3. İstifadeciden 2 eded daxil etmesini teleb edin. Birinci ededin ikinci edede 
# bölünmesinden alınan tam hisseni tapın (*QEYD: "//" - dan istifadə etməyin).


# eded1=int(input("ededleri daxil edin:"))
# eded2=int(input("ededleri daxil edin:"))
# yeni_eded = eded1 / eded2
# yeni_str_eded = str(yeni_eded)
# print(yeni_str_eded[0])

# 4. sum() funksiyasını araşdırın. (5ci ve 10cu məsələdə bu funksiyadan istifadə 
# etməlisiniz).


# ededleri daxil edin:15
# ededleri daxil edin:2
# 1

# 5. İstifadəçidən ədədlər daxil etməsini tələb edin, ədədlərin sayı ixtiyari sayda ola bilər, 
# daha sonra bu ədədlərin ədədi ortasını ekrana çap edin.??


# 6. x = 5
# y = 4
# Elə edin ki, nəticədə ekrana x və y-i ekrana çap etdikdə dəyərləri dəyişmiş olsun, yəni x 
# = 4, y = 5 olsun. (Əllə x = 4, y = 5 yazmaq olmaz )
# x = 5
# y = 4

# 7.İstifadəçidən 2 ədəd ikirəqəmli daxil etməsini tələb edin. Hər bir ədədin təkliyi ilə 
# onluğunu toplayın və birbirlərinə bölünməsindən alınan qalığı çap edin.

# eded1 = int(input("ededleri daxil edin:"))
# eded2 = int(input("ededleri daxil edin:"))
# yeni_str_eded1 = str(eded1)
# yeni_str_eded2 = str(eded2)

# print(int(yeni_str_eded1 [0]) + int(yeni_str_eded2[0]))
# print(eded1 + eded2)
# print(eded1 % eded2) yalniz onluq ve tekliyi toplamaq nece olur ?




# 8. Ədədin cüt və yaxud tək olmağını hansı operatorla və necə bilmək olar ?

# eded1=int(input("ededleri daxil edin:"))
# print(int(eded1 % 2))

# 9.İstifadəçidən ədəd daxil etməsini tələb edin, daha sonra ədəddəki rəqəmlərin sayını 
# həmin ədədə ustu quvveti yazmaqla ekrana cap edin.

# eded1=int(input("ededleri daxil edin:"))

# sum() --> verilen ededleri toplayir
# a = (1, 2, 3, 4, 5)
# x = sum(a)
# print(x)

# mylist = ['salam', 'salam']
# mytuple = ('salam','sagol')
# print(mylist)
# print(mytuple)
# new_list = tuple(mylist)
# print(new_list)
# LISTler tekrar qebul edirler

# mylist = [1,2,3,4,5]
# mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# print(mylist[-1:-3:-1])
# print(mylist[::2])
# num1 = 9
# num2 = 3
# print(num1/num2) # tam ve kesr hisseni bir yerde gosterir
# print(num1//num2) # tam hisseni gosterir
# print(num1 % num2) # ededin edede bolunmesinden alinan qaligi
# print(num1 ** num2) # ustlu quvveti gosterir


# x = 5
# y = 4
# 
# x = x + y  # 9
# y = x - y  # 5
# x = x - y  # 4

# x = 10
# y = 5
# x = x + y # 15
# y = x - y # 10
# x = x - y # 5
# print(x,y) 
# a = 9
# b = 5
# a = a + b 
# b = a - b 
# a = a - b
# print(a,b)

# mylist = [1,2,3,4,5]
# print(sum(mylist))

# mylist = [1,2,3,4,5]    
# a = (max(mylist))
# b = (min(mylist))
# print(a+b)

# mylist = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# mylist.sort()
# mylist[-1:-5:-1]
# print(mylist[-1:-6:-1])
      
# 4. list-in icinde deyerlerin olub-olmamagini 
# nece yoxlamaq olar ? Meselen list bosdurmu 
# yoxsa icinde element varmi?
# mylist = [] 
# print(len(mylist))

# 5. mylist = [1,2,3]
# mylist_2 = mylist
# Bu koda ele birsey elave edin ki, mylist_2- 
# listinde nese deyisiklik etdikde mylist – də 
# hecbir deysiklik olmasin.

# mylist = [1,2,3]
# mylist_1 = mylist.copy()
# mylist_1.append(15)
# print(mylist_1)


# 6. listlerde 
# del mylist 
# ve 
# clear mylist 
# arasindaki ferq nedir ?
# del listi silir amma clear listin icerisini silir


# 7. listlerde pop metodunun diger silme 
# metodlarindan ferqi nedir?
# pop silindikden sonra deyeri qaytarir

# 8. Listlerin str-lerden ferqli cehetlerini 
# sadalayin ve numune misallar uzerinde 
# gosterin


# 9.mystr = “SALAM”
# print(list(mystr))
# kodunun neticesi ne olacaq? (birinci dusunun 
# texminler edin, daha sonra yazib yoxlayin)
# mystr = 'SALAM'
# print(list(mystr))
# ['S', 'A', 'L', 'A', 'M']

# 10. newlist = [“CCC”, “C”, “CC”, “CCCC”]
# print(newlist.count(“c”))
# kodunun neticesi ne olacaq? (kodu editora 
# yapisdirib cavabi tapmayin, coxlu texminler 

# newlist = ["CCC", "C", "CC", "CCCC"]
# print(newlist.count("C"))
# 1



# 1. İstifadəçidən bir ədəd alın və bu ədəf istənilən rəqəmli ola bilər, məsələn 5, 47, yaxud
# 352. Neçə rəqəmli olursa olsun onu rəqəmlərinin cəmini ekrana verin.

# eded1 = input("ededleri daxil edin:").split()
# print(eded1)



# 2. İstifadəçidən rəqəmlər alın və təkrarkarı yox edin. Daha sonra azalan sıra düzüb list 
# şəklində ekrana verin



# 3. Bos bir dictionary yaradın. Daha sonra istifadəçidən ad, soyad, doğum tarixi kimi 
# dəyərlər alın və uyğun olaraq key, value şəklində dictionary-ə save edin.



# 4.mylist = [1,2,4,5]
# mylist_2 = [1,3,5,9]
# Bu iki listdə eyni olan elementləri tapan kod yazın



# 5.list və tuple-lar arasındakı sürət fərqini izah edin.

# 6. myset = {1,2,3,4}
# myset.discard(0)
# kodunun nəticəsi nə olacaq ?
# myset = {1,2,3,4}
# myset.discard(0)
# print(myset)

# 7.istifadəçidən hərflər alın, daha sonra təkrar hərfləri silin. Sıralayın(əlifbanın əksinə). 
# Daha sonra strə cevirib ekrana çap edin

# herfler = input("herfleri daxil edin: ").split()
# herfler1 = set(herfler)
# x = list(herfler1)
# x.sort(reverse=True)
# print(x) 
 
# 1. mylist = [1,2,3,4,5]
# list-in elementlərini while dövrü ilə ekrana çap edin.
# mylist = [1,2,3,4,5]
# i = 0
# while i < 5:
#  i = i + 1
#  print(mylist)

# 2. mylist = [1,2,3,4,5,6]
# list-in elementlərini while dövrü ilə ekrana çap edin, 
# lakin elə edin ki, 5 çap olunmasın.
# mylist = [1,2,3,4,5,6]
# i = 6
# while i > 0:
#     i -= 1 
# if i == 5:
#   continue
# print(i)

# 3. mylist = ['a', 'b', 'c', 'd']
# list-in elementlərini ekrana çap edin, amma 'c' 
# olduqda dövr dayansın.
# 4. 1-dən 100ə qədər cüt ədədləri çap edin.
# 5. 100-dən 1-ə qədər tək ədədləri çap edin.
# 6. İstifadəçidən 3 ədəd alın, hansı daha böyükdürsə 
# onu ekrana çap edin.
# 7. mylist = ['1', '2', '3', '4', '5']
# newlist = []
# mylist-in elementlerini int tipe cevrilmis sekilde 
# newlist-e elave edin. (Dovr operatorundan istifade 
# edeceksiniz).
# 8.mylist = ['1', 'salam', '222', 'b4f8', '0']
# list-in içində ədəd tipinə çevrilə bilənləri ekrana çap 
# edin. (Dövr operatoru ilə).




# 1. İstifadəçidən içində ixtiyari dəyərlər olan list alın. Daha 
# sonra list-in elementlərindən ədəd tipdə olanlardan cüt 
# olanlarını ekrana çap edin.
# mylist = input("deyerleri daxil edin: ").split()
# i = 0
# # newlist=[]
# while i < len(mylist):
#     if mylist[i].isdigit():
#     #  newlist = mylist  sa 
#      print(mylist[i],end=" ")
    
       
#     i = i + 1
# ?????
        

# 2. Sadə ədəd - o ədədə deyilir ki, yalnız 1ə və özünə 
# bölünür. Məsələ, 13, 47, 31 və s. Daxil edilən ədədin sadə 
# olub olmadığını yoxlayan kod yazın.
# eded = (int(input("ededleri daxil edin: ")))
# if eded % 2 == 0:
#         print("eded cutdur", eded)
# else:
#     print("eded tekdir",eded)


# 3. İstifadəçi ixtiyari sayda ədəd daxil edəcək. Bu ədədlərin 
# hamısı bir list-in içində toplaşmalıdır. For və while - hər 
# iksii ilə bu listin elementlərini int tipə çevirin.

# mylist = input("ededleri daxil edin: ").split()
# newlist = []

# i = 0
# while i < len(mylist):
#     newlist.append(int(mylist[i]))
#     i = i + 1
# print(newlist)  

# print(type(newlist))
# for i in mylist:
#     newlist.append(int(i))
# print(newlist)    
# [12, 14, 1, 5, 8, 9]
# <class 'list'>

# 4. mylist = ['s', 'a', 'l', 'a' , 'm']
# Dövr operatorları vasitəsilə bu list-in elementlərini bir str 
# tipli dəyişənə birləşdirilmiş kimi mənimsədin. (for və while 
# hər ikisi ilə).

# mylist = ['s', 'a', 'l', 'a' , 'm']
# mystr = ""
# i = 0
# # while i < len(mylist):
#     # print(mylist[i])
#     # i = i + 1

# for i in mylist:
#     mystr = mystr + i
# print(mystr)

# 5. İstifadəçidən 3 ədəd alın, hansı böyükdürsə, onun 
# rəqəmlərini newlist-ə əlavə edin.

# num1 = int(input("1ci ededi daxil edin : "))
# num2 = int(input("2ci ededi daxil edin : "))
# num3 = int(input("3cu ededi daxil edin : "))
# newlist = []
# if num1 > num2 and num1 > num3:
#     newlist.append(num1)
# elif num2 > num1 and num2 > num3:
#     newlist.append(num2)
# elif num3 > num2 and num3 > num1:
#     newlist.append(num3)
# else:
#     print("Ededlerden her hansi birileri birbrine beraberdirler")
# print(newlist)

# 6. İstifadəçidən bir parol alın, parolun uzunluğu 5dən 
# böyük olmadığı təqdirdə parolu soruşmağa dəvam etsin, 
# yəni dövr etsin.

# password = input("parolu  daxil edin : ")

# for i in password:
#  if i == 5:
#   print("password sayi duzgundur" )
# else:
#       print("password sayi duzgun deyil,tekrar daxil edin")

# num1 = input("1ci ededi daxil edin : ")
# newlist = []
# for i in num1:
#  newlist.append(int(i))
# newlist = set(newlist) 
# newlist = list(newlist)
# print(newlist)

while True:
    parol = input("parolu daxil edin: ")
    for i in parol:
      if  i = "alma"
        if " " in i and i>5:
            print("parolu duzgun daxil etdiniz:")
            break

