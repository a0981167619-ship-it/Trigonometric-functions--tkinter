import tkinter as tk
import math

function=tk.Tk()
function.title('三角函數計算器')
label=tk.Label(text='三角函數計算器',fg="black",font=("標楷體",36))
label.pack(side='top') #位置定位為正上方

entry_A=tk.Entry(function)
entry_B=tk.Entry(function)
entry_C=tk.Entry(function)
entry_symbol=tk.Entry(function)

def sin_sum(A,B,symbol): #計算sin的和角公式
    sinC=math.sin(math.radians(A)+math.radians(B)) #sin的和角公式: sin(A+B)
    sinC=math.sin(math.radians(A))*math.cos(math.radians(B))+math.cos(math.radians(A))*math.sin(math.radians(B)) # sin(A+B)=sinA*cosB+cosA*sinB  //把角度傳換成弧度量再做計算
    return sinC

def result1(): #輸出sin和角的數值
    try:
     angleA=float(entry_A.get())
     angleB=float(entry_B.get())   
     symbol=str(entry_symbol.get()) #輸入+,-,*,/...等符號

     answer=sin_sum(angleA,angleB,symbol)

     answer_result.config(text='sin的和角數值≈'+'  '+str(round(answer,6))) #取六位小數

    except Exception as error:
       print(error) #利用終端機查看錯誤
       answer_result.config(text='請輸入正確的角度數值')

A_label=tk.Label(function,text='A (angle) 單位為°').pack()
entry_A=tk.Entry(function) #製作輸入框
entry_A.pack()

B_label=tk.Label(function,text='B (angle) 單位為°').pack()
entry_B=tk.Entry(function) 
entry_B.pack()

answer_result=tk.Label(function,text='sin(A+B)') #顯示sin的和角數值
answer_result.pack()

tk.Button(function,text='計算sin和角(A+B)',command=result1).pack() #製作按鈕


def sin(A,B,symbol): #計算sin的差角公式
   SinC=math.sin(math.radians(A)-math.radians(B)) #sin的差角公式: sin(A-B)
   SinC=math.sin(math.radians(A))*math.cos(math.radians(B))-math.cos(math.radians(A))*math.sin(math.radians(B)) #sin(A-B)=sinA*cosB-cosA*sinB
   return SinC

def result2(): #輸出sin的差角數值
   try:
      angleA=float(entry_A.get())
      angleB=float(entry_B.get())
      symbol=str(entry_symbol.get())

      Answer=sin(angleA,angleB,symbol)

      Answer_result.config(text='sin的差角數值≈'+'  '+str(round(Answer,6)))

   except Exception as error:
      print(error)
      Answer_result.config(text='請輸入正確的角度數值')

Answer_result=tk.Label(function,text='sin(A-B)') #顯示sin的差角數值
Answer_result.pack()

tk.Button(function,text='計算sin差角(A-B)',command=result2).pack()


def cos(A,B,symbol): #計算cos的和角公式
   cosc=math.cos(math.radians(A)+math.radians(B)) #cos的和角公式: cos(A+B)
   cosc=math.cos(math.radians(A))*math.cos(math.radians(B))-math.sin(math.radians(A))*math.sin(math.radians(B))  #cos(A+B)=cosA*cosB-sinA*sinB
   return cosc

def result3(): #輸出cos的和角數值
   try:
      angleA=float(entry_A.get())
      angleB=float(entry_B.get())
      symbol=str(entry_symbol.get())

      Ans=cos(angleA,angleB,symbol)
      Ans_result.config(text='cos的和角數值≈'+'  '+str(round(Ans,6)))

   except Exception as error:
      print(error)
      Ans_result.config(text='請輸入正確的角度數值')

Ans_result=tk.Label(function,text='cos(A+B)') #顯示cos的和角數值
Ans_result.pack()

tk.Button(function,text='計算cos的和角(A+B)',command=result3).pack()

def  Cos(A,B,symbol):  #計算cos的差角公式
     Cosc=math.cos(math.radians(A)-math.radians(B)) #cos的差角公式: cos(A-B)
     Cosc=math.cos(math.radians(A))*math.cos(math.radians(B))+math.sin(math.radians(A))*math.sin(math.radians(B)) #cos(A-B)=cosA*cosB+sinA*sinB
     return Cosc

def result4(): #輸出cos的差角數值
   try:
      angleA=float(entry_A.get())
      angleB=float(entry_B.get())
      symbol=str(entry_symbol.get())

      consequence=Cos(angleA,angleB,symbol)
      consequence_result.config(text='cos的差角數值≈'+'  '+str(round(consequence,6)))

   except Exception as error:
      print(error)
      consequence_result.config(text='請輸入正確的角度數值')

consequence_result=tk.Label(function,text='cos(A-B)') #顯示cos的差角數值
consequence_result.pack()

tk.Button(function,text='計算cos的差角(A-B)',command=result4).pack()

def tan(A,B,symbol): #計算tan的和角公式
   tanc=math.tan(math.radians(A)+math.radians(B)) #tan的和角公式: tan(A+B)
   tanc=math.tan(math.radians(A))+math.tan(math.radians(B))/1-math.tan(math.radians(A))*math.tan(math.radians(B)) #tan(A+B)=tanA+tanB/1-tanA*tanB
   return tanc

def result5():
    try:
     angleA=float(entry_A.get())
     angleB=float(entry_B.get())
     symbol=str(entry_symbol.get())

     if (angleA+angleB-90)%180==0:  #tan=90、270、450...角度時,沒有斜率
                    consequence_result.config(text='tan(A+B)未定義')
     else:
          consequent=tan(angleA,angleB,symbol)
          consequent_result.config(text='tan的和角數值≈'+'  '+str(consequent,6))
       
    except Exception as error:
       print(error)
       consequent_result.config(text='請輸入正確的角度數值')


consequent_result=tk.Label(function,text='tan(A+B)') #顯示tan的和角數值
consequent_result.pack()

tk.Button(function,text='計算tan的和角(A+B)',command=result5).pack()

def Tan(A,B,symbol):  #計算tan的差角公式
    Tanc=math.tan(math.radians(A)-math.radians(B))  #tan的差角公式: tan(A-B)
    Tanc=(math.tan(math.radians(A))-math.tan(math.radians(B)))/(1+math.tan(math.radians(A))*math.tan(math.radians(B)))
    return Tanc

def result6(): #輸出tan的差角數值
    try:
        angleA=float(entry_A.get())
        angleB=float(entry_B.get())
        symbol=str(entry_symbol.get())

        if (angleA-angleB-90)%180==0:
            outcome_result.config(text='tan(A-B)未定義')
        else:
          outcome=Tan(angleA,angleB,symbol)
          outcome_result.config(text='tan的差角數值≈'+'  '+str(round(outcome,6)))

    except Exception as error:
        print(error)
        outcome_result.config(text='請輸入正確的角度數值')

outcome_result=tk.Label(function,text='tan(A-B)')  #顯示tan的差角數值
outcome_result.pack()

tk.Button(function,text='計算tan的差角數值(A-B)',command=result6).pack()

def sin_2theta(C): #計算sin的二倍角公式
    sin=2*math.sin(math.radians(C))*math.cos(math.radians(C))  #sin的二倍角公式: 1.2sinθcosθ  2. 2tanθ/1+tan**2θ
    return sin

def result7(): #輸出sin的二倍角數值
    try:
     angleC=float(entry_C.get())
     sequel=sin_2theta(angleC)
     sequel_result.config(text='sin2θ的數值≈'+'  '+str(round(sequel,6)))

    except Exception as error:
        print(error)
        sequel_result.config(text='請輸入正確的角度數值')

C_label=tk.Label(function,text='angle (單位為°)').pack()
entry_C=tk.Entry(function)
entry_C.pack()

sequel_result=tk.Label(function,text='sin2θ')  #顯示sin二倍角的值
sequel_result.pack()    

tk.Button(function,text='計算sin的二倍角2θ',command=result7).pack()

def cos_2theta(C): #計算cos的二倍角公式
    cos=math.cos(math.radians(C))**2-math.sin(math.radians(C))**2  #cos的二倍角公式= 1.cos**2-sin**2    2.1-2sin**2θ   3. 2cos**2θ-1  4. 1-tan**2θ/1+tan**2θ
    return cos

def result8(): #輸出cos的二倍角數值
    try:
        angleC=float(entry_C.get())
        upshot=cos_2theta(angleC)
        upshot_result.config(text='cos2θ的數值≈'+'  '+str(round(upshot,6)))

    except Exception as error:
      print(error)
      upshot_result.config(text='請輸入正確的角度數值')

upshot_result=tk.Label(function,text='cos2θ')
upshot_result.pack()

tk.Button(function,text='計算cos的二倍角2θ',command=result8).pack()

def tan_2theta(C): #計算tan的二倍角公式
    tan=2*(math.tan(math.radians(C)))/(1-math.tan(math.radians(C))**2)  #tan的二倍角公式= 1.2tanθ/1-tan**2θ  2. sin2θ/cos2θ(商數關係)
    return tan

def result9(): #輸出tan的二倍角數值
    try:
        angleC=float(entry_C.get())
        if (angleC-45)%90==0: #tan=90、270、450時斜率未定義
            educt_result.config(text='未定義')
        else:
         educt=round(tan_2theta(angleC),6)
         if educt==-0.0:
             educt=0.0
         educt_result.config(text='tan2θ的數值≈'+'  '+str(educt))
    except Exception as error:
        print(error)
        educt_result.config(text='請輸入正確的角度數值')

educt_result=tk.Label(function,text='tan2θ')
educt_result.pack()

tk.Button(function,text='計算tan的二倍角2θ',command=result9).pack()

def sin_half_theta(C): #計算sin的半角公式
    sin_half=math.sqrt((1-math.cos(math.radians(C)))/2)  #sin的半角公式: 1-cosθ/2開根號
    return sin_half

def result_10(): #輸出sin的半角數值
    try:
      angleC=float(entry_C.get())
      consequence2=sin_half_theta(angleC)
      consequence2_result.config(text='sin的半角數值≈'+'  '+str(round(consequence2,6)))

    except Exception as error:
        print(error)
        consequence2_result.config(text='請輸入正確的角度數值')

consequence2_result=tk.Label(function,text='sinθ/2')
consequence2_result.pack()

tk.Button(function,text='計算sin的半角θ/2',command=result_10).pack()

def cos_half_theta(C):  #計算cos的半角公式
    cos_half=math.sqrt((1+math.cos(math.radians(C)))/2) #cos的半角公式:1+cosθ/2開根號
    return cos_half

def result_11(): #輸出cos的半角數值
    try:
        angleC=float(entry_C.get())
        educt2=cos_half_theta(angleC)
        educt2_result.config(text='cos的半角數值≈'+'  '+str(round(educt2,6)))

    except Exception as error:
        print(error)
        educt2_result.config(text='請輸入正確的角度數值')

educt2_result=tk.Label(function,text='cosθ/2')
educt2_result.pack()

tk.Button(function,text='計算cos的半角θ/2',command=result_11).pack()

def tan_half_theta(C): #計算tan的半角公式
    tan_half=(1-math.cos(math.radians(C)))/(math.sin(math.radians(C))) #tan的半角公式: 1-cosθ/sinθ  2.sinθ/1+cosθ
    return tan_half

def result_12(): #輸出tan的半角數值
    try:
        angleC=float(entry_C.get())
        if (angleC-180)%360==0:
            slay_result.config(text='未定義')
        else:
          slay=tan_half_theta(angleC)
          slay_result.config(text='tan的半角數值≈'+'  '+str(round(slay,6)))

    except Exception as error:
        print(error)
        slay_result.config(text='請輸入正確的角度數值')

slay_result=tk.Label(function,text='tanθ/2')
slay_result.pack()

tk.Button(function,text='計算tan的半角θ/2',command=result_12).pack()

def sin3_theta(C): #計算sin的三倍角公式
    sin_3=3*(math.sin(math.radians(C)))-4*(math.sin(math.radians(C))**3)   #sin的三倍角公式: 3sinθ-4sin**3θ  口訣:陽光照在富士山上
    return sin_3

def result_13(): #輸出sin的三倍角數值
    try:
        angleC=float(entry_C.get())
        outcome2=sin3_theta(angleC)
        outcome2_result.config(text='sin的三倍角數值≈'+'  '+str(round(outcome2,6)))

    except Exception as error:
        print(error)
        outcome2_result.config(text='請輸入正確的角度數值')

outcome2_result=tk.Label(function,text='sin3θ')
outcome2_result.pack()
tk.Button(function,text='計算sin的三倍角3θ',command=result_13).pack()

def cos3_theta(C): #計算cos的三倍角公式
    cos_3=(4*(math.cos(math.radians(C)))**3)-3*(math.cos(math.radians(C))) #cos的三倍角公式: 4cos3θ**3-3cosθ  口訣: 塊三:四塊三減三塊(台語)
    return cos_3

def result_14(): #輸出cos的三倍角數值
    try:
        angleC=float(entry_C.get())
        effect=cos3_theta(angleC)
        effect_result.config(text='cos的三倍角數值≈'+'  '+str(round(effect,6)))

    except Exception as error:
        print(error)
        effect_result.config(text='請輸入正確的角度數值')

effect_result=tk.Label(function,text='cos3θ')
effect_result.pack()

tk.Button(function,text='計算cos的三倍角3θ',command=result_14).pack()

def sin_t(C):
    sint=math.sin(math.radians(C))
    return sint

def result_15():
    try:
        angleC=float(entry_C.get())
        effect2=sin_t(angleC)
        effect2_result.config(text='sin的數值≈'+'  '+str(round(effect2,6)))

    except Exception as error:
        print(error)
        effect2_result.config(text='請輸入正確的角度數值')

effect2_result=tk.Label(function,text='sinθ')
effect2_result.pack()

tk.Button(function,text='計算sinθ',command=result_15).pack()
function.mainloop()











