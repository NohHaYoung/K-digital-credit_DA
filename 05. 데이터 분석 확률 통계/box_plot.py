from elice_utils import EliceUtils
import numpy as np
import matplotlib.pyplot as plt
elice_utils = EliceUtils()  

#카페인 함유량
coffee = np.array([202,177,121,148,89,121,137,158])

#상자그림
fig, ax = plt.subplots()
## 여기에 코드를 작성해주세요
plt.boxplot(coffee)

##
plt.show()
fig.savefig("box_plot.png")
elice_utils.send_image("box_plot.png")