# Arduino with CNN for security lock（Arduino SecurityLock）

I set up Arduino circuit with CNN for security lock. 
After trained CNN, predict web camera streaming images with Arduino.
If key number is macth with prediction, the key will open. it can be used for security lock.
 
 
# preparation

<b>・Arduino Uno
・Servomotor
・switch
・adapter
・DC Jack DIP Kit</b>

## arduino circuit


# How to use

1.gather dateset from web camera

2.train by CNN

3.write key number to key.txt

4.predict web camera streaming images.  If its prediction match with key.txt number, the key can be opened.


# Its stracture

## from create dateset to prediction

## Main security system 

It's logic and making process are written below my blog.

https://trafalbad.hatenadiary.jp/entry/2020/06/01/113828
