import tkinter as tk
import math

function=tk.Tk()
function.title('三角函數計算器')
label=tk.Label(text='三角函數計算器',fg="black",font=("標楷體",36))
label.pack(side='top') #位置定位為正上方

entry_A=tk.Entry(function)
entry_B=tk.Entry(function)
entry_symbol=tk.Entry(function)

def sin(A,B,symbol): #計算sin的和角公式
    sinC=math.sin(math.radians(A)+math.radians(B)) #sin的和角公式: sin(A+B)
    sinC=math.sin(math.radians(A))*math.cos(math.radians(B))+math.cos(math.radians(A))*math.sin(math.radians(B)) # sin(A+B)=sinA*cosB+cosA*sinB  //把角度傳換成弧度量再做計算
    return sinC

def result(): #輸出sin和角的數值
    try:
     angleA=float(entry_A.get())
     angleB=float(entry_B.get())   
     symbol=str(entry_symbol.get()) #輸入+,-,*,/...等符號

     answer=sin(angleA,angleB,symbol)

     answer_result.config(text='sin的和角數值為:'+' '+str(round(answer,6))) #取六位小數

    except Exception as error:
       print(error) #利用終端機查看錯誤
       answer_result.config(text='請輸入正確的角度')

A_label=tk.Label(function,text='A (angle)').pack()
entry_A=tk.Entry(function) #製作輸入框
entry_A.pack()

B_label=tk.Label(function,text='B (angle)').pack()
entry_B=tk.Entry(function) 
entry_B.pack()

answer_result=tk.Label(function,text='sin(A+B)') #顯示結果
answer_result.pack()

tk.Button(function,text='計算sin和角(A+B)',command=result).pack() #製作按鈕

function.mainloop()
       

