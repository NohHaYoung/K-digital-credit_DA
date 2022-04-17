from elice_utils import EliceUtils
import matplotlib.pyplot as plt
import pandas as pd
elice_utils = EliceUtils()    
# body.csv 읽어오기 
body = pd.read_csv("body.csv")

# Q1. 산점도 
##1-1 키와 몸무게간 산점도 
fig, ax = plt.subplots()
## 여기에 코드를 작성해 주세요
plt.scatter(body['height'], body['weight'])

##
plt.show()
fig.savefig("height_weight_plot.png")
elice_utils.send_image("height_weight_plot.png")

##1-2 키와 체지방량 산점도 
fig, ax = plt.subplots()
## 여기에 코드를 작성해 주세요
plt.scatter(body['height'], body['body_fat'])

##
plt.show()
fig.savefig("height_fat_plot.png")
elice_utils.send_image("height_fat_plot.png")

##1-3 키와 다리길이 산점도 
fig, ax = plt.subplots()
## 여기에 코드를 작성해 주세요
plt.scatter(body['height'], body['leglen'])

##
plt.show()
fig.savefig("height_leglen_plot.png")
elice_utils.send_image("height_leglen_plot.png")


##1-4 키와 모발 산점도 
fig, ax = plt.subplots()
## 여기에 코드를 작성해 주세요
plt.scatter(body['height'], body['hair'])

##
plt.show()
fig.savefig("height_hair_plot.png")
elice_utils.send_image("height_hair_plot.png")