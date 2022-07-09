import math; #імпортування математичної бібліотеки для модуля
def averageArrayNumber(arr1): #функція для пошуку числа в масиві, найближчого до середнього значення
 newArr = [int(x) for x in arr1]; #конвертація str масива в int
 nextArr = []; #створення додаткового масиву, в який будуть подаватись "середнє значення масиву - newArr[element]" 
 sum= 0;
 for x in newArr: #пошук суми всіх значень масиву
    sum+=x;
 res =sum/len(newArr); #пошук середнього знаечння елементів масиву 
 count = 0;
 while(count<len(newArr)): # заповнення нового масиву значеннями "середнє значення масиву - newArr[element]" 
    nextArr.insert(count,abs(res-newArr[count])); #вставка елементів в новий масив з використанням модуля
    count+=1;
 count1 = 0;
 res1 = nextArr[0]; # фіксуємо 0 елемент масиву, з яким ми будемо порівнювати кожен наступний елемент, поки не знайдемо менший за цей елемент
 while(count1<len(nextArr)): #пошук найменшого елемента в новому масиві
  
    if(res1>=nextArr[count1]):
        res1 = nextArr[count1];
    count1+=1;
 index1 = nextArr.index(res1);
 return("Average Number in Array is", newArr[index1]); #повертаємо число з масиву, яке є найближчим до середнього значення

def maxArrayNumber(arr1): #функція для пошуку найбільшого числа в масиві
 newArr = [int(x) for x in arr1]; #конвертація масиву з str в int
 res = newArr[0]; # фіксуємо 0 елемент масиву, з яким ми будемо порівнювати кожен наступний елемент, поки не знайдемо більший за цей елемент
 count = 0;
 while(count<len(newArr)): #пошук найбільшого значення масиву
  
    if(res<=newArr[count]):
        res = newArr[count]; #якщо ми знайшли елемент, більший за початковий, то присвоюєму в змінну res новий елемент
    count+=1;
 return 'Max ArrayNumber is',res; #повернення найбільшого елемента масиву

def minArrayNumber(arr1): #функція для пошуку найбільшого числа в масиві
 newArr = [int(x) for x in arr1]; #конвертація масиву з str в int
 res = newArr[0]; # фіксуємо 0 елемент масиву, з яким ми будемо порівнювати кожен наступний елемент, поки не знайдемо менший за цей елемент
 count = 0;
 while(count<len(newArr)): #пошук найменшого значення масиву
  
    if(res>=newArr[count]):
        res = newArr[count]; #якщо ми знайшли елемент, більший за початковий, то присвоюєму в змінну res новий елемент
    count+=1;
 return 'Min ArrayNumber is',res; #повернення найменшого елемента масиву


myFile = open("text.txt"); #відкриття файлу з масивом
FileContent = myFile.read(); #зчитування вмісту
arr1 = FileContent.split(',') #вміст подається у вигляді однієї строки. Ми розбиваєму цю строку і формуємо масив зі строчних елементів
print("Do you want to find MIN or MAX or AVERAGE number in Array? Enter 'Min' or 'Max' or 'Average'" );

a = input(); #просимо ввести користувача дію, яку він хоче виконати і запускаємо відповідну функцію нижче

if a == "min" or a == "MIN" or a =="Min":
 maxArrayNumber(arr1);

elif a == "max" or a == "MAX" or a == "Max":
    minArrayNumber(arr1);

elif a == "average" or a =="AVERAGE" or a == "Average":
    averageArrayNumber(arr1);
