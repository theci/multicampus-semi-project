from django.shortcuts import render
from .models import Data
from django.db import connection

def gangnam(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)        

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/gangnam.html', {'data_2021':arr[148]})


def gangdong(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)        

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/gangdong.html', {'data_2021':arr[149]})

def gangbuk(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)         

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/gangbuk.html', {'data_2021':arr[150]})

def gangseo(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)         

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/gangseo.html', {'data_2021':arr[151]})

def gwanak(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)         

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/gwanak.html', {'data_2021':arr[152]})

def gwangjin(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)      

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/gwangjin.html', {'data_2021':arr[153]})

def guro(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)        

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/guro.html', {'data_2021':arr[154]})

def geumcheon(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)        

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/geumcheon.html', {'data_2021':arr[155]})

def nowon(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)       

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/nowon.html', {'data_2021':arr[156]})

def dobong(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)       

    except:
        connection.rollback()
        print("Failed selecting in DB")
   
    return render(request, 'myapp/dobong.html', {'data_2021':arr[157]})
    
def dongdaemun(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)       

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/dongdaemun.html', {'data_2021':arr[158]})

def dongjak(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)        

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/dongjak.html', {'data_2021':arr[159]})

def mapo(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)        

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/mapo.html', {'data_2021':arr[160]})

def seodaemun(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)        

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/seodaemun.html', {'data_2021':arr[161]})

def seocho(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)        

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/seocho.html', {'data_2021':arr[162]})

def seongdong(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)         

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/seongdong.html', {'data_2021':arr[163]})

def seongbuk(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)         

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/seongbuk.html', {'data_2021':arr[164]})

def songpa(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)         

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/songpa.html', {'data_2021':arr[165]})

def yangcheon(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)        

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/yangcheon.html', {'data_2021':arr[166]})

def yeongdeungpo(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)         

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/yeongdeungpo.html', {'data_2021':arr[167]})

def yongsan(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row) 
    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/yongsan.html', {'data_2021':arr[168]})


def eunpyeong(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)        

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/eunpyeong.html', {'data_2021':arr[169]})


def jongno(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)       

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/jongno.html', {'data_2021':arr[170]})


def junggu(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)       

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/junggu.html', {'data_2021':arr[171]})

def jungnang(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT * FROM data"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        arr = []
        for data in datas:
            row = {
                'cnt_cctv' : data[3],
                'cnt_light' : data[5],
                'cnt_police' : data[6],
                'female_population' : data[7]
            }
            arr.append(row)        

    except:
        connection.rollback()
        print("Failed selecting in DB")

    return render(request, 'myapp/jungnang.html', {'data_2021':arr[172]})

      
