# Arduino with CNN for security lock（Arduino SecurityLock）

I set up Arduino circuit with CNN for security lock. 

After trained CNN, predict web camera streaming images with Arduino.

If key number is macth with prediction, the key will open. it can be used for security lock.
 
 
 
 
# Preparation<hr>

<blockquote>
 <b>・Arduino Uno
 
・Servomotor

・Switch

・Adapter

・DC Jack DIP Kit</b></blockquote>


## Arduino circuit

![Arduino_diagram](https://user-images.githubusercontent.com/48679574/83414058-ce642100-a457-11ea-9ce0-b172a8db2035.jpg)






# How to use<hr>

1.Gather dateset from web camera

2.Train by CNN

3.Write key number to key.txt

4.Predict web camera streaming images.  If its prediction match with key.txt number, the key can be opened.




# Its stracture<hr>

## From create dateset to prediction

![train_cycle](https://user-images.githubusercontent.com/48679574/83414073-d6bc5c00-a457-11ea-8b9d-bef101042a5b.jpg)





## Main security system 
![opensystem](https://user-images.githubusercontent.com/48679574/83414084-dcb23d00-a457-11ea-80cc-77e76a4f2bfd.jpg)


It's logic and making process are written below my blog.

https://trafalbad.hatenadiary.jp/entry/2020/06/01/113828
